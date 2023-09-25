package utils

import (
	"bytes"
	"encoding/json"
	"finance/api/exceptions"
	"net/http"

	"github.com/gin-gonic/gin"
)

const URL = "http://10.1.32.26:8000"

type ResponseBody struct {
	StatusCode int         `json:"status_code"`
	Message    string      `json:"message"`
	Data       interface{} `json:"data"`
}

func Get(c *gin.Context, url string, data interface{}, body interface{}) error {
	client := &http.Client{}
	var buf bytes.Buffer

	// Jika ada parameter Body
	err := json.NewEncoder(&buf).Encode(body)
	if err != nil {
		exceptions.EntityException(c, "Error Entity Body!")
		return err
	}

	var responseBody ResponseBody

	newRequest, err := http.NewRequest("GET", url, &buf)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return err
	}

	newResponse, err := client.Do(newRequest)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return err
	}

	defer newResponse.Body.Close()
	defer client.CloseIdleConnections()

	if newResponse.StatusCode != http.StatusOK {
		c.JSON(newResponse.StatusCode, gin.H{"error": "Failed to fetch data from the external API"})
		return err
	}

	responseBody = ResponseBody{
		Data: data,
	}

	err = json.NewDecoder(newResponse.Body).Decode(&responseBody)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return err
	}

	return nil
}
