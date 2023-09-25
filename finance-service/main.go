package main

import (
	"finance/api/config"
	"finance/api/route"
	migration "finance/generate/sql"
	"os"
)

// func init() {
// 	config.SetupConfiguration()
// }

// @title Finance API
// @version 1.0

// @securityDefinitions.apikey BearerAuth
// @in Header
// @name Authorization

// @host 10.1.32.26:3010
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
	} else {
		config.InitEnvConfigs(false, env)
		db := config.InitDB()
		route.CreateHandler(db, env)
	}
}
