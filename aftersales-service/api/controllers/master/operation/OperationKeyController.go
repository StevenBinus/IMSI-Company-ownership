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

type OperationKeyController struct {
	operationkeyservice masteroperationservice.OperationKeyService
}

func StartOperationKeyRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	operationkeyservice masteroperationservice.OperationKeyService,
) {
	operationKeyHandler := OperationKeyController{operationkeyservice: operationkeyservice}
	r.GET("/operation-key/:operation_key_id", middlewares.DBTransactionMiddleware(db), operationKeyHandler.GetOperationKeyByID)
}

// @Summary Get Operation Key By ID
// @Description REST API Operation Key
// @Accept json
// @Produce json
// @Tags Operation Key
// @Param operation_key_id path string true "operation_key_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-key/{operation_key_id} [get]
func (r *OperationKeyController) GetOperationKeyByID(c *gin.Context) {
	operationKeyId, _ := strconv.Atoi(c.Param("operation_key_id"))
	result, err := r.operationkeyservice.GetOperationKeyById(int32(operationKeyId))
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Success", http.StatusOK)
}
