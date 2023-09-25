package exceptions

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func RoleException(c *gin.Context, message string) {
	if message == "" {
		message = "You don't have permission"
	}
	res := Error{
		Success: false,
		Message: message,
		Data:    nil,
	}

	c.JSON(http.StatusForbidden, res)
}
