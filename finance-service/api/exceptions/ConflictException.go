package exceptions

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func ConflictException(c *gin.Context, message string) {
	if message == "" {
		message = "Data Already Exists"
	}
	res := Error{
		Success: false,
		Message: message,
		Data:    nil,
	}

	c.JSON(http.StatusConflict, res)
}