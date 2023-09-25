package payloads

import "github.com/gin-gonic/gin"

type ResponseAuth struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Token   string `json:"token"`
	UserId  int    `json:"user_id"`
}

func ResponseToken(c *gin.Context, message string, token string, userId int, status int) {
	res := ResponseAuth{
		Status:  status,
		Message: message,
		Token:   token,
		UserId:  userId,
	}

	c.JSON(status, res)
}
