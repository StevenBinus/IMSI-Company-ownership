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

type OperationCodeController struct {
	operationcodeservice masteroperationservice.OperationCodeService
}

func StartOperationCodeRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	operationcodeservice masteroperationservice.OperationCodeService,
) {
	operationCodeHandler := OperationCodeController{operationcodeservice: operationcodeservice}
	r.GET("/operation-code/:operation_id", middlewares.DBTransactionMiddleware(db), operationCodeHandler.GetOperationCodeByID)
}

// @Summary Get Operation Code By ID
// @Description REST API Operation Code
// @Accept json
// @Produce json
// @Tags Operation Code
// @Param operation_id path string true "operation_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-code/{operation_id} [get]
func (r *OperationCodeController) GetOperationCodeByID(c *gin.Context) {
	operationId, _ := strconv.Atoi(c.Param("operation_id"))
	result, err := r.operationcodeservice.GetOperationCodeById(int32(operationId))
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Success", http.StatusOK)
}
