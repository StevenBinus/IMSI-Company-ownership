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

type OperationSectionController struct {
	operationsectionservice masteroperationservice.OperationSectionService
}

func StartOperationSectionRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	operationsectionservice masteroperationservice.OperationSectionService,
) {
	operationSectionHandler := OperationSectionController{operationsectionservice: operationsectionservice}
	r.GET("/operation-section/", middlewares.DBTransactionMiddleware(db), operationSectionHandler.GetAllOperationSectionList)
	r.GET("/operation-section/:operation_section_id", middlewares.DBTransactionMiddleware(db), operationSectionHandler.GetOperationSectionByID)
	r.GET("/operation-section/section-description", middlewares.DBTransactionMiddleware(db), operationSectionHandler.GetOperationSectionDescription)
	r.PUT("/operation-section/", middlewares.DBTransactionMiddleware(db), operationSectionHandler.SaveOperationSection)
	r.PATCH("/operation-section/:operation_section_id", middlewares.DBTransactionMiddleware(db), operationSectionHandler.ChangeStatusOperationSection)
}

// @Summary Get All Operation Section
// @Description REST API Operation Section
// @Accept json
// @Produce json
// @Tags Operation Section
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param operation_section_code query string false "operation_section_code"
// @Param operation_section_description query string false "operation_section_description"
// @Param operation_group_code query string false "operation_group_code"
// @Param operation_group_description query string false "operation_group_description"
// @Param is_active query string false "is_active" Enums(true, false)
// @Param sort_of query string false "sort_of"
// @Param sort_by query string false "sort_by"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-section [get]
func (r *OperationSectionController) GetAllOperationSectionList(c *gin.Context) {
	queryParams := map[string]string{
		"operation_group_code":          c.Query("operation_group_code"),
		"operation_group_description":   c.Query("operation_group_description"),
		"operation_section_code":        c.Query("operation_section_code"),
		"operation_section_description": c.Query("operation_section_description"),
		"is_active":                     c.Query("is_active"),
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

	result, err := r.operationsectionservice.GetAllOperationSectionList(criteria, sortField, pagination)
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, result, "success", http.StatusOK)
}

// @Summary Get Operation Section By ID
// @Description REST API Operation Section
// @Accept json
// @Produce json
// @Tags Operation Section
// @Param operation_section_id path string true "operation_section_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-section/{operation_section_id} [get]
func (r *OperationSectionController) GetOperationSectionByID(c *gin.Context) {
	operationSectionId, _ := strconv.Atoi(c.Param("operation_section_id"))
	result, err := r.operationsectionservice.GetOperationSectionById(int(operationSectionId))
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Success Kesini", http.StatusOK)
}

// @Summary Get Operation Section Name
// @Description REST API Operation Section
// @Accept json
// @Produce json
// @Tags Operation Section
// @Param operation_section_code query string true "operation_section_code"
// @Param operation_group_code query string true "operation_group_code"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-section/section-description [get]
func (r *OperationSectionController) GetOperationSectionDescription(c *gin.Context) {
	operationSectionCode := c.Query("operation_section_code")
	operationGroupCode := c.Query("operation_group_code")
	result, err := r.operationsectionservice.GetOperationSectionDescription(operationSectionCode, operationGroupCode)
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Success", http.StatusOK)
}

// @Summary Save Operation Section
// @Description REST API Operation Section
// @Accept json
// @Produce json
// @Tags Operation Section
// @param reqBody body masterpayloads.OperationSectionRequest true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-section/ [put]
func (r *OperationSectionController) SaveOperationSection(c *gin.Context) {
	var request masteroperationpayloads.OperationSectionRequest
	var message = ""
	if err := c.ShouldBindJSON(&request); err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}

	create, err := r.operationsectionservice.SaveOperationSection(request)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if request.OperationSectionId == 0 {
		message = "Create Data Success"
	} else {
		message = "Update Data Success"
	}

	payloads.HandleSuccess(c, create, message, http.StatusOK)
}

// @Summary Change Status Operation Section
// @Description REST API Operation Section
// @Accept json
// @Produce json
// @Tags Operation Section
// @param operation_section_id path string true "operation_section_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/master/operation-section/{operation_section_id} [patch]
func (r *OperationSectionController) ChangeStatusOperationSection(c *gin.Context) {
	operationSectionId, err := strconv.Atoi(c.Param("operation_section_id"))
	if err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}
	//id check
	result, err := r.operationsectionservice.GetOperationSectionById(int(operationSectionId))
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if result.OperationGroupId == 0 {
		exceptions.NotFoundException(c, err.Error())
		return
	}

	response, err := r.operationsectionservice.ChangeStatusOperationSection(int(operationSectionId))
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, response, "Change Status Successfully!", http.StatusOK)
}
