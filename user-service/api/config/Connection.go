package config

import (
	"context"
	"errors"
	"fmt"
	"net/url"
	"time"

	goredis "github.com/redis/go-redis/v9"
	log "github.com/sirupsen/logrus"
	"gorm.io/driver/sqlserver"
	"gorm.io/gorm"
	"gorm.io/gorm/schema"
)

type Database struct {
	Client *goredis.Client
}

var (
	ErrNil = errors.New("no matching record found in redis database")
	Ctx    = context.TODO()
)

func InitDB() (*gorm.DB, *Database) {
	val := url.Values{}
	val.Add("parseTime", "True")
	val.Add("loc", "Asia/Jakarta")
	/*
		dsn := fmt.Sprintf(`host=%s user=%s password=%s dbname=%s port=%d sslmode=disable TimeZone=Asia/Shanghai`,
			EnvConfigs.DBHost, EnvConfigs.DBUser, EnvConfigs.DBPass, EnvConfigs.DBName, EnvConfigs.DBPort)
		db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{
			NamingStrategy: schema.NamingStrategy{
				//TablePrefix:   "dbo.", // schema name
				SingularTable: false,
			}})
		if err != nil {
			log.Fatal("Cannot connected database ", err)
			return nil, nil
		}
	*/
	dsn := fmt.Sprintf(`%s://%s:%s@%s:%v?database=%s`, EnvConfigs.DBDriver, EnvConfigs.DBUser, EnvConfigs.DBPass, EnvConfigs.DBHost, EnvConfigs.DBPort, EnvConfigs.DBName)

	db, err := gorm.Open(sqlserver.Open(dsn), &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			//TablePrefix:   "dbo.", // schema name
			SingularTable: false,
		}})
	if err != nil {
		log.Fatal("Cannot connected database ", err)
		return nil, nil
	}

	sqlDB, err := db.DB()

	err = sqlDB.Ping()

	if err != nil {
		log.Fatal("Request Timeout ", err)
		return nil, nil
	}

	sqlDB.SetMaxIdleConns(10)
	sqlDB.SetConnMaxIdleTime(time.Minute * 3)
	sqlDB.SetMaxOpenConns(10)
	sqlDB.SetConnMaxLifetime(time.Minute * 3)

	log.Info("Connected Database " + EnvConfigs.DBDriver)

	client := goredis.NewClient(&goredis.Options{
		Addr:     fmt.Sprintf("%s:%v", EnvConfigs.RedisHost, EnvConfigs.RedisPort),
		Username: EnvConfigs.RedisUsername,
		Password: EnvConfigs.RedisPassword,
		DB:       0,
	})
	if err := client.Ping(Ctx).Err(); err != nil {
		log.Fatal("Redis Error", err)
		return nil, nil
	}

	// rh.SetGoRedisClientWithContext(context.Background(), client)

	return db, &Database{
		Client: client,
	}
}
