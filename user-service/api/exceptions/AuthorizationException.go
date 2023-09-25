package exceptions

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func AuthorizeException(c *gin.Context, message string) {
	if message == "" {
		message = "Not Authorized"
	}
	res := Error{
		Success: false,
		Message: message,
		Data:    nil,
	}

	c.JSON(http.StatusUnauthorized, res)
}
