package securities

import (
	"finance/api/config"
	"fmt"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v4"
	"github.com/spf13/viper"
)

func GetAuthentication(c *gin.Context) error {
	token, err := VerifyToken(c)

	if err != nil {
		return err
	}

	if _, ok := token.Claims.(jwt.Claims); !ok && !token.Valid {
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

		return []byte(viper.GetString(config.EnvConfigs.JWTKey)), nil
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
