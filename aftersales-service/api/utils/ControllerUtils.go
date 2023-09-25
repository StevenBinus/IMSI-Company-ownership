package utils

import (
	"strconv"

	"github.com/gin-gonic/gin"
)

// BuildQueryCriteria insert queryOf and queryBy into QueryCriteria struct of slices then return it
func BuildQueryCriteria(queryParams map[string]string) []QueryCriteria {
	var criteria []QueryCriteria
	for key, value := range queryParams {
		if value != "" {
			criteria = append(criteria, QueryCriteria{
				QueryOf: value,
				QueryBy: key,
			})
		}
	}
	return criteria
}

// GetQueryInt take QueryParam to return int
func GetQueryInt(c *gin.Context, param string) int {
	value, _ := strconv.Atoi(c.Query(param))
	return value
}
