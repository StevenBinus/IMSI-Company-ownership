package exceptions

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func CreatedException(c *gin.Context, message string) {
	if message == "" {
		message = "Data Created"
	}
	res := Error{
		Success: false,
		Message: message,
		Data:    nil,
	}

	c.JSON(http.StatusCreated, res)
}
