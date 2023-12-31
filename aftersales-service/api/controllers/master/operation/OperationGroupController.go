package masteroperationcontroller

import (
	"after-sales/api/exceptions"
	"after-sales/api/middlewares"
	"after-sales/api/payloads"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	masteroperationservice "after-sales/api/services/master/operation"
	"after-sales/api/utils"

	// "after-sales/api/middlewares"

	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type OperationGroupController struct {
	operationgroupservice masteroperationservice.OperationGroupService
}

func StartOperationGroupRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	operationgroupservice masteroperationservice.OperationGroupService,
) {
	operationGroupHandler := OperationGroupController{operationgroupservice: operationgroupservice}
	r.GET("/operation-group/", middlewares.DBTransactionMiddleware(db), operationGroupHandler.GetAllOperationGroup)
	r.GET("/operation-group/:operation_group_code", middlewares.DBTransactionMiddleware(db), operationGroupHandler.GetOperationGroupByCode)
	r.GET("/operation-group/drop-down", middlewares.DBTransactionMiddleware(db), operationGroupHandler.GetAllOperationGroupIsActive)
	r.POST("/operation-group/", middlewares.DBTransactionMiddleware(db), operationGroupHandler.SaveOperationGroup)
	r.PATCH("/operation-group/:operation_group_id", middlewares.DBTransactionMiddleware(db), operationGroupHandler.ChangeStatusOperationGroup)
}

// @Summary Get All Operation Group
// @Description REST API Operation Group
// @Accept json
// @Produce json
// @Tags Operation Group
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param operation_group_code query string false "operation_group_code"
// @Param operation_group_description query string false "operation_group_description"
// @Param is_active query string false "is_active" Enums(true, false)
// @Param sort_of query string false "sort_of"
// @Param sort_by query string false "sort_by"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-group [get]
func (r *OperationGroupController) GetAllOperationGroup(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	queryParams := map[string]string{
		"operation_group_code":        c.Query("operation_group_code"),
		"operation_group_description": c.Query("operation_group_description"),
		"is_active":                   c.Query("is_active"),
	}

	sortField := utils.SortField{
		SortOf: c.Query("sort_of"),
		SortBy: c.Query("sort_by"),
	}

	pagination := utils.Pagination{
		Limit: utils.GetQueryInt(c, "limit"),
		Page:  utils.GetQueryInt(c, "page"),
	}

	criteria := utils.BuildQueryCriteria(queryParams)

	result, err := r.operationgroupservice.WithTrx(trxHandle).GetAllOperationGroup(criteria, sortField, pagination)
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, result, "success", http.StatusOK)
}

// @Summary Get All Operation Group Is Active
// @Description REST API Operation Group
// @Accept json
// @Produce json
// @Tags Operation Group
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-group/drop-down [get]
func (r *OperationGroupController) GetAllOperationGroupIsActive(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	result, err := r.operationgroupservice.WithTrx(trxHandle).GetAllOperationGroupIsActive()
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, result, http.StatusText(200), http.StatusOK)
}

// @Summary Get Operation Group By Code
// @Description REST API Operation Group
// @Accept json
// @Produce json
// @Tags Operation Group
// @Param operation_group_id path string true "operation_group_code"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-group/{operation_group_code} [get]
func (r *OperationGroupController) GetOperationGroupByCode(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	operationGroupCode := c.Param("operation_group_code")
	result, err := r.operationgroupservice.WithTrx(trxHandle).GetOperationGroupByCode(operationGroupCode)
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, result, "success", http.StatusOK)
}

// @Summary Save Operation Group
// @Description REST API Operation Group
// @Accept json
// @Produce json
// @Tags Operation Group
// @param reqBody body masterpayloads.OperationGroupHeader true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-group/ [post]
func (r *OperationGroupController) SaveOperationGroup(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	var request masteroperationpayloads.OperationGroupHeader
	var message = ""

	if err := c.ShouldBindJSON(&request); err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}

	if int(request.OperationGroupId) != 0 {
		result, err := r.operationgroupservice.WithTrx(trxHandle).GetOperationGroupById(int(request.OperationGroupId))

		if err != nil {
			exceptions.AppException(c, err.Error())
			return
		}

		if result.OperationGroupId == 0 {
			exceptions.NotFoundException(c, err.Error())
			return
		}
	}

	create, err := r.operationgroupservice.WithTrx(trxHandle).SaveOperationGroup(request)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if request.OperationGroupId == 0 {
		message = "created"
	} else {
		message = "updated"
	}

	payloads.HandleSuccess(c, create, message, http.StatusOK)
}

// @Summary Change Status Operation Group
// @Description REST API Operation Group
// @Accept json
// @Produce json
// @Tags Operation Group
// @param operation_group_id path string true "operation_group_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-group/{operation_group_id} [patch]
func (r *OperationGroupController) ChangeStatusOperationGroup(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	operationGroupId, err := strconv.Atoi(c.Param("operation_group_id"))
	if err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}
	//id check
	result, err := r.operationgroupservice.WithTrx(trxHandle).GetOperationGroupById(int(operationGroupId))
	if err != nil || result.OperationGroupId == 0 {
		exceptions.NotFoundException(c, err.Error())
		return
	}

	response, err := r.operationgroupservice.WithTrx(trxHandle).ChangeStatusOperationGroup(int(operationGroupId))
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, response, "updated", http.StatusOK)
}
