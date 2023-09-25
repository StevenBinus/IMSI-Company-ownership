package main

import (
	"os"
	"user-service/api/config"
	migration "user-service/api/generate"
	"user-service/api/route"
)

// func init() {
// 	config.SetupConfiguration()
// }

// @title DMS User Service
// @version 1.0
// @description DMS User Service Architecture
// @termsOfService http://swagger.io/terms/

// @contact.name Indomobil
// @contact.url https://github.com/Indomobil-Sukses-Internasional-Tbk
// @contact.email indomobil01@gmail.com

// @license.name MIT
// @license.url https://github.com/Indomobil-Sukses-Internasional-Tbk/-/blob/main/LICENSE

// @securityDefinitions.apikey BearerAuth
// @in Header
// @name Authorization

// @host 10.1.32.26:3000
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
		db, dbRedis := config.InitDB()
		route.CreateHandler(db, dbRedis, env)
	}
}
