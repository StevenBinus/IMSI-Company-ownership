package middlewares

import (
	"finance/api/exceptions"
	"finance/api/securities"
	"github.com/gin-gonic/gin"
)

func SetupAuthenticationMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		err := securities.GetAuthentication(c)

		if err != nil {
			exceptions.AuthorizeException(c, err.Error())
			c.Abort()
			return
		}

		c.Next()
	}
}
