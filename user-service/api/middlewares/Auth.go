package middlewares

import (
	"user-service/api/exceptions"
	"user-service/api/securities"
	"user-service/api/services"

	"github.com/gin-gonic/gin"
)

func SetupAuthenticationMiddleware(services services.UserService) gin.HandlerFunc {
	return func(c *gin.Context) {
		err := securities.GetAuthentication(c, services)
		if err != nil {
			exceptions.AuthorizeException(c, "")
			c.Abort()
			return
		}

		c.Next()
	}
}
