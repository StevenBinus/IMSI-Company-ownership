package route

import (
	"fmt"
	"net"
	"net/http"
	"user-service/api/config"
	"user-service/api/controllers"
	"user-service/api/middlewares"
	"user-service/api/repositories/repoimpl"
	"user-service/api/services/serviceimpl"
	_ "user-service/docs"

	"github.com/gin-gonic/gin"
	log "github.com/sirupsen/logrus"
	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
	"gorm.io/gorm"
)

func CreateHandler(db *gorm.DB, dbRedis *config.Database, env string) {
	r := gin.New()

	userRepo := repoimpl.CreateUserRepository(db, dbRedis)

	userService := serviceimpl.CreateUserService(userRepo)
	authService := serviceimpl.CreateAuthService(userRepo)

	r.Use(middlewares.SetupCorsMiddleware())

	if env != "prod" {
		r.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
	}

	api := r.Group("/api")
	controllers.CreateAuthRoutes(db, api.Group("/auth"), authService, userService)
	controllers.CreateUserRoutes(db, api.Group("/user"), userService)
	controllers.CreateAdminRoutes(db, api.Group("/admin/user"), authService, userService)

	server := &http.Server{Handler: r}
	l, err := net.Listen("tcp4", fmt.Sprintf(":%v", config.EnvConfigs.Port))
	err = server.Serve(l)
	if err != nil {
		log.Fatal(err)
		return
	}
}
