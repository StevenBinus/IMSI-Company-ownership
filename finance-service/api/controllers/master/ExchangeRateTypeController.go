package mastercontrollers

import (
	"finance/api/exceptions"
	"finance/api/middlewares"
	"finance/api/payloads"
	masterpayloads "finance/api/payloads/master"
	"finance/api/payloads/pagination"
	masterservice "finance/api/services/master"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type ExchangeRateTypeController struct {
	exchangeRateTypeService masterservice.ExchangeRateTypeService
}

func OpenExchangeRateTypeRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	exchangeRateTypeService masterservice.ExchangeRateTypeService,
) {
	handler := ExchangeRateTypeController{
		exchangeRateTypeService: exchangeRateTypeService,
	}

	// r.Use(middlewares.SetupAuthenticationMiddleware())
	r.POST("/save-exchange-rate-type", middlewares.DBTransactionMiddleware(db), handler.Save)
	r.GET("/exchange-rate-type", middlewares.DBTransactionMiddleware(db), handler.GetAll)
	r.GET("/exchange-rate-type-by-id/:exchange_rate_type_id", middlewares.DBTransactionMiddleware(db), handler.GetById)
	r.GET("/exchange-rate-type-by-name/:exchange_rate_type", middlewares.DBTransactionMiddleware(db), handler.GetByName)
	r.PUT("/change-exchange-rate-type-status/:exchange_rate_type_id", middlewares.DBTransactionMiddleware(db), handler.ChangeStatus)
}

// @Summary Save Exchange Rate Type
// @Description Save Exchange Rate Type
// @Accept json
// @Produce json
// @Tags Master : Exchange Rate Type
// @Security BearerAuth
// @param reqBody body masterpayloads.SaveExchangeRateTypeRequest true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/save-exchange-rate-type [post]
func (r *ExchangeRateTypeController) Save(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	requestBody := masterpayloads.SaveExchangeRateTypeRequest{}

	if err := c.ShouldBindJSON(&requestBody); err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}

	checkName, err := r.exchangeRateTypeService.WithTrx(trxHandle).GetByName(requestBody.ExchangeRateType)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if checkName.ExchangeRateType != "" {
		exceptions.ConflictException(c, fmt.Sprintf("Data %s already exist!", checkName.ExchangeRateType))
		return
	}

	save, err := r.exchangeRateTypeService.WithTrx(trxHandle).Save(requestBody)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, save, "Insert successfully", http.StatusOK)

}

// @Summary Change Exchange Rate Status By Id
// @Description Change Exchange Rate Status By Id
// @Accept json
// @Produce json
// @Tags Master : Exchange Rate Type
// @Security BearerAuth
// @Param exchange_rate_type_id path string true "exchange_rate_type_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/change-exchange-rate-type-status/{exchange_rate_type_id} [patch]
func (r *ExchangeRateTypeController) ChangeStatus(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	exchangeRateTypeId, _ := strconv.Atoi(c.Param("exchange_rate_type_id"))

	save, err := r.exchangeRateTypeService.WithTrx(trxHandle).ChangeStatus(exchangeRateTypeId)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, save, "Updated successfully", http.StatusOK)

}

// @Summary Get All Exchange Rate Type
// @Description Get All Exchange Rate Type
// @Accept json
// @Produce json
// @Tags Master : Exchange Rate Type
// @Security BearerAuth
// @Success 200 {object} payloads.Response
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param sort_of query string false "Sort Of: {column}"
// @Param sort_by query string false "Sort By: {asc}"
// @Param exchange_rate_type query string false "Exchange Rate Type"
// @Param description query string false "Description"
// @Param is_active query string false "Is Active"
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/exchange-rate-type [get]
func (r *ExchangeRateTypeController) GetAll(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	limit, _ := strconv.Atoi(c.Query("limit"))
	page, _ := strconv.Atoi(c.Query("page"))
	sortOf := c.Query("sort_of")
	sortBy := c.Query("sort_by")
	// exchangeRateTypeId, _ := strconv.Atoi(c.Query("exchange_rate_type_id"))
	exchangeRateType := c.Query("exchange_rate_type")
	description := c.Query("description")
	isActive := c.Query("is_active")
	get, err := r.exchangeRateTypeService.WithTrx(trxHandle).GetAll(masterpayloads.GetAllExchangeRateTypeRequest{
		ExchangeRateType: exchangeRateType,
		Description:      description,
		IsActive:         isActive,
	}, pagination.Pagination{
		Limit:  limit,
		SortOf: sortOf,
		SortBy: sortBy,
		Page:   page,
	})

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccessPagination(c, get, "Get Data Successfully!", 200, get.Limit, get.Page, get.TotalRows, get.TotalPages)
}

// @Summary Get Exchange Rate Type By Id
// @Description Get Exchange Rate Type By Id
// @Accept json
// @Produce json
// @Tags Master : Exchange Rate Type
// @Security BearerAuth
// @Param exchange_rate_type_id path string true "exchange_rate_type_id"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/exchange-rate-type-by-id/{exchange_rate_type_id} [get]
func (r *ExchangeRateTypeController) GetById(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	exchangeRateTypeId, _ := strconv.Atoi(c.Param("exchange_rate_type_id"))

	get, err := r.exchangeRateTypeService.WithTrx(trxHandle).GetById(exchangeRateTypeId)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if get.ExchangeRateTypeId == 0 {
		exceptions.NotFoundException(c, "Exchange Rate Type Data Not Found!")
		return
	}

	payloads.HandleSuccess(c, get, "Get Data Successfully!", http.StatusOK)
}

// @Summary Get Exchange Rate Type By Name
// @Description Get Exchange Rate Type By Name
// @Accept json
// @Produce json
// @Tags Master : Exchange Rate Type
// @Security BearerAuth
// @Param exchange_rate_type query string true "Exchange Rate Type"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/exchange-rate-type-by-name/{exchange_rate_type} [get]
func (r *ExchangeRateTypeController) GetByName(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	exchangeRateType := c.Query("exchange_rate_type")

	get, err := r.exchangeRateTypeService.WithTrx(trxHandle).GetByName(exchangeRateType)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if get.ExchangeRateTypeId == 0 {
		exceptions.NotFoundException(c, "Exchange Rate Type Data Not Found!")
		return
	}

	payloads.HandleSuccess(c, get, "Get Data Successfully!", http.StatusOK)
}
