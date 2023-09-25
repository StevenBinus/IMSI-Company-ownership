package masteroperationcontroller

import (
	"after-sales/api/exceptions"
	"after-sales/api/middlewares"
	"after-sales/api/payloads"

	// "after-sales/api/middlewares"

	masteroperationservice "after-sales/api/services/master/operation"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type OperationEntriesController struct {
	operationentriesservice masteroperationservice.OperationEntriesService
}

func StartOperationEntriesRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	operationentriesservice masteroperationservice.OperationEntriesService,
) {
	operationEntriesHandler := OperationEntriesController{operationentriesservice: operationentriesservice}
	r.GET("/operation-entries/:operation_entries_id", middlewares.DBTransactionMiddleware(db), operationEntriesHandler.GetOperationEntriesByID)
}

// @Summary Get Operation Entries By ID
// @Description REST API Operation Entries
// @Accept json
// @Produce json
// @Tags Operation Entries
// @Param operation_entries_id path string true "operation_entries_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-entries/{operation_entries_id} [get]
func (r *OperationEntriesController) GetOperationEntriesByID(c *gin.Context) {
	operationId, _ := strconv.Atoi(c.Param("operation_entries_id"))
	result, err := r.operationentriesservice.GetOperationEntriesById(int32(operationId))
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, result, "Get Data Success", http.StatusOK)
}
