package exceptions

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Error struct {
	Success bool        `json:"Success"`
	Message string      `json:"Message"`
	Data    interface{} `json:"Data"`
}

func AppException(c *gin.Context, message string) {
	if message == "" {
		message = "Internal Server Error"
	}
	res := Error{
		Success: false,
		Message: message,
		Data:    nil,
	}

	c.JSON(http.StatusInternalServerError, res)
}
