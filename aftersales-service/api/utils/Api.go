package utils

import (
	"after-sales/api/exceptions"
	"bytes"
	"encoding/json"
	"net/http"

	"github.com/gin-gonic/gin"
)

type APIResponse struct {
	Data interface{} `json:"data"`
}

func GetJSON(url string, target interface{}) error {
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	return json.NewDecoder(resp.Body).Decode(target)
}

func GetAPIResponse(url string, target interface{}) (APIResponse, error) {
	var apiResponse APIResponse
	err := GetJSON(url, &apiResponse)
	if err != nil {
		return apiResponse, err
	}

	dataMap, ok := apiResponse.Data.(map[string]interface{})
	if ok {
		dataBytes, err := json.Marshal(dataMap)
		if err != nil {
			return apiResponse, err
		}
		err = json.Unmarshal(dataBytes, &target)
		if err != nil {
			return apiResponse, err
		}
	}
	return apiResponse, nil
}

// soon ganti ke function ini
func Get(c *gin.Context, url string, data interface{}, body interface{}) error {
	client := &http.Client{}
	var buf bytes.Buffer

	// Jika ada parameter Body
	err := json.NewEncoder(&buf).Encode(body)
	if err != nil {
		exceptions.EntityException(c, "Error Entity Body!")
		return err
	}

	var responseBody APIResponse

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

	responseBody = APIResponse{
		Data: data,
	}

	err = json.NewDecoder(newResponse.Body).Decode(&responseBody)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return err
	}

	return nil
}
