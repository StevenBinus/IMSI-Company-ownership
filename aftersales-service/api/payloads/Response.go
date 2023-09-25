package payloads

import "github.com/gin-gonic/gin"

type Response struct {
	Success int         `json:"status_code"`
	Message string      `json:"message"`
	Data    interface{} `json:"data"`
}

func HandleSuccess(c *gin.Context, data interface{}, message string, status int) {
	res := Response{
		Success: 200,
		Message: message,
		Data:    data,
	}

	c.JSON(status, res)
}
