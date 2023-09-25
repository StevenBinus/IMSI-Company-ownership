package migration

import (
	"fmt"
	"user-service/api/config"
	userentities "user-service/api/entities"

	// approvalentities "user-service/api/entities/approval/approval-template"

	"gorm.io/driver/sqlserver"
	"gorm.io/gorm"
	"gorm.io/gorm/schema"
)

func Migrate() {
	config.InitEnvConfigs(false, "")
	logEntry := fmt.Sprintf("Auto Migrating...")
	// dsn := fmt.Sprintf(`%s://%s:%s@%s:%v?database=%s&connection+timeout=30`, config.config.config.EnvConfigs.DBDriver, config.config.config.EnvConfigs.DBUser, config.config.config.EnvConfigs.DBPass, config.config.config.EnvConfigs.DBHost, config.config.config.EnvConfigs.DBPort, config.config.config.EnvConfigs.DBName)
	dsn := fmt.Sprintf(`%s://%s:%s@%s:%v?database=%s`, config.EnvConfigs.DBDriver, config.EnvConfigs.DBUser, config.EnvConfigs.DBPass, config.EnvConfigs.DBHost, config.EnvConfigs.DBPort, config.EnvConfigs.DBName)
	db, err := gorm.Open(sqlserver.Open(dsn), &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			//TablePrefix:   "dbo.", // schema name
			SingularTable: false,
		}})
	db.AutoMigrate(
		// approverentities.Approver{},
		// approverentities.ApproverDetails{},
		// &approvalentities.Approval{},
		// &approvalentities.ApprovalAmount{},
		// &approvalentities.ApprovalMapping{},
		&userentities.Role{},
	) //<--- Line 84
	if db != nil && db.Error != nil {
		//We have an error
		fmt.Sprintf("%s %s with error %s", logEntry, "Failed", db.Error)
		panic(err)
	}
	fmt.Sprintf("%s %s", logEntry, "Success")
}
