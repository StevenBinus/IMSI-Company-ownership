package migration

import (
	"after-sales/api/config"
	masteritementities "after-sales/api/entities/master/item"
	masteroperationentities "after-sales/api/entities/master/operation"
	transactionworkshopentities "after-sales/api/entities/transaction/workshop"
	"log"

	"fmt"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func MigrateGG() {
	config.InitEnvConfigs(false, "")
	log.Println("Auto Migrating...")
	log.Println(config.EnvConfigs.DBName)

	dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%d sslmode=disable TimeZone=Asia/Shanghai",
		config.EnvConfigs.DBHost, config.EnvConfigs.DBUser, config.EnvConfigs.DBPass, config.EnvConfigs.DBName, config.EnvConfigs.DBPort)
	log.Println(dsn)
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})

	if err != nil {
		log.Panic("Migration Failed")
	}

	db.AutoMigrate( // sesuai urutan foreign key
		&masteroperationentities.OperationGroup{},
		&masteroperationentities.OperationSection{},
		&masteroperationentities.OperationKey{},
		&masteroperationentities.OperationModelMapping{},
		&masteroperationentities.OperationEntries{},
		&masteroperationentities.OperationCode{},
		&masteritementities.ItemClass{},
		&masteritementities.Item{},
		// &transactionentities.SupplySlip{},
		// &transactionentities.SupplySlipDetail{},
		// &transactionentities.WorkOrderItem{},
		// &transactionentities.WorkOrderOperation{},
		// &transactionentities.ServiceLog{},
		&transactionworkshopentities.BookingEstimation{},
	)

	fmt.Println("Migration Process Success...")
}
