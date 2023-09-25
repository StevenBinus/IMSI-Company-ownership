package migration

import (
	"finance/api/config"
	masterentities "finance/api/entities/master"
	"fmt"

	"gorm.io/driver/sqlserver"
	"gorm.io/gorm"
	"gorm.io/gorm/schema"
)

func Migrate() {
	config.InitEnvConfigs(false, "")
	logEntry := fmt.Sprintf("Auto Migrating...")

	dsn := fmt.Sprintf(
		`%s://%s:%s@%s:%v?database=%s`,
		config.EnvConfigs.DBDriver,
		config.EnvConfigs.DBUser,
		config.EnvConfigs.DBPass,
		config.EnvConfigs.DBHost,
		config.EnvConfigs.DBPort,
		config.EnvConfigs.DBName,
	)

	db, err := gorm.Open(sqlserver.Open(dsn), &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			//TablePrefix:   "dbo.", // schema name
			SingularTable: false,
		}, DisableForeignKeyConstraintWhenMigrating: false})

	db.AutoMigrate(
		// &masterentities.MtrCurrency{},
		// &masterentities.Event{},
		// &accountreceivableentities.AccountReceivableUnit{},
		// &accountreceivableentities.AccountReceivableUnitDetail{},
		&masterentities.Bank{},
		&masterentities.BankBranch{},
		&masterentities.BankContact{},
		// &masterentities.ExchangeRateType{},
	)

	if db != nil && db.Error != nil {
		fmt.Sprintf("%s %s with error %s", logEntry, "Failed", db.Error)
		panic(err)
	}

	fmt.Sprintf("%s %s", logEntry, "Success")
}
