package main

import (
	"after-sales/api/config"
	"after-sales/api/route"
	migration "after-sales/generate/sql"
	"os"
)

// func init() {
// 	config.SetupConfiguration()
// }

// @title After Sales API
// @version 1.0

// @host localhost:3020
// @BasePath /api
func main() {
	args := os.Args
	env := ""
	if len(args) > 1 {
		env = args[1]
	}

	if env == "migrate" {
		migration.Migrate()
	} else if env == "generate" {
		migration.Generate()
	} else if env == "migg" {
		migration.MigrateGG()
	} else {
		config.InitEnvConfigs(false, env)
		db := config.InitDB()
		route.CreateHandler(db, env)
	}
}
