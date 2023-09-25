package exceptions

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func NoContentException(c *gin.Context, message string) {
	if message == "" {
		message = "No Content"
	}
	res := Error{
		Success: false,
		Message: message,
		Data:    nil,
	}

	c.JSON(http.StatusNoContent, res)
}
