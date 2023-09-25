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

type OperationModelMappingController struct {
	operationmodelmappingservice masteroperationservice.OperationModelMappingService
}

func StartOperationModelMappingRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	operationmodelmappingservice masteroperationservice.OperationModelMappingService,
) {
	operationModelMappingHandler := OperationModelMappingController{operationmodelmappingservice: operationmodelmappingservice}
	r.GET("/operation-model-mapping/:operation_model_mapping_id", middlewares.DBTransactionMiddleware(db), operationModelMappingHandler.GetOperationModelMappingByID)
}

// @Summary Get Operation Model Mapping By ID
// @Description REST API Operation Model Mapping
// @Accept json
// @Produce json
// @Tags Operation Model Mapping
// @Param operation_model_mapping_id path string true "operation_model_mapping_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-model-mapping/{operation_model_mapping_id} [get]
func (r *OperationModelMappingController) GetOperationModelMappingByID(c *gin.Context) {
	operationModelMappingId, _ := strconv.Atoi(c.Param("operation_model_mapping_id"))
	result, err := r.operationmodelmappingservice.GetOperationModelMappingById(int32(operationModelMappingId))
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Success", http.StatusOK)
}
