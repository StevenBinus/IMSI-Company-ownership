package migration

import (
	"fmt"
	"log"
	"user-service/api/config"

	"gorm.io/driver/sqlserver"
	"gorm.io/gen"
	"gorm.io/gorm"
	"gorm.io/gorm/schema"
)

func Generate() {
	config.InitEnvConfigs(false, "")
	g := gen.NewGenerator(gen.Config{
		OutPath: "../api/model/auth",
		Mode:    gen.WithoutContext | gen.WithDefaultQuery | gen.WithQueryInterface, // generate mode
	})

	dsn := fmt.Sprintf(`%s://%s:%s@%s:%v?database=%s`, config.EnvConfigs.DBDriver, config.EnvConfigs.DBUser, config.EnvConfigs.DBPass, config.EnvConfigs.DBHost, config.EnvConfigs.DBPort, config.EnvConfigs.DBName)
	db, err := gorm.Open(sqlserver.Open(dsn), &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			//TablePrefix:   "dbo.", // schema name
			SingularTable: false,
		}})

	if err != nil {
		log.Fatal("Cannot connected database ", err)
		return
	}
	g.UseDB(db) // reuse your gorm db

	// // Generate basic type-safe DAO API for struct `model.User` following conventions
	//g.ApplyBasic(model.UserDetail{})

	// // Generate Type Safe API with Dynamic SQL defined on Querier interface for `model.User` and `model.Company`
	//g.ApplyInterface(func() {}, model.UserDetail{})

	// // Generate the code
	g.GenerateModel("users")
	g.Execute()

}

// gentool -dsn "sqlserver://sa:P@ssw0rd@10.1.32.62:1433?database=dms_microservices_dev" -tables "auth_user"
