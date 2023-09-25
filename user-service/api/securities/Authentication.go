package securities

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
	"user-service/api/payloads"
	"user-service/api/services"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v4"
	"github.com/spf13/viper"
)

func GetAuthentication(c *gin.Context, service services.UserService) error {
	token, err := VerifyToken(c)

	if err != nil {
		return err
	}
	_, ok := token.Claims.(jwt.Claims)

	claims, _ := token.Claims.(jwt.MapClaims)
	userId := fmt.Sprintf("%v", claims["user_id"])
	client := fmt.Sprintf("%v", claims["client"])

	id, _ := strconv.Atoi(userId)
	session, err := service.FindSession(payloads.UserDetail{UserId: int(id)})

	if client != session {
		return errors.New("You are already logged in on a different device")
	}
	if !ok && !token.Valid {
		return err
	}

	return nil
}

func VerifyToken(c *gin.Context) (*jwt.Token, error) {
	tokenString := ExtractToken(c)
	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}

		return []byte(viper.GetString("secret_key")), nil
	})

	if err != nil {
		return nil, err
	}

	return token, nil
}

func ExtractToken(c *gin.Context) string {
	keys := c.Request.URL.Query()
	token := keys.Get("token")

	if token != "" {
		return token
	}

	c.Writer.Header()
	authHeader := c.GetHeader("Authorization")
	bearerToken := strings.Split(authHeader, " ")

	if len(bearerToken) == 2 {
		return bearerToken[1]
	} else {
		return ""
	}
}
