package mastercontrollers

import (
	"finance/api/exceptions"
	"finance/api/middlewares"
	"finance/api/payloads"
	masterpayloads "finance/api/payloads/master"
	"finance/api/payloads/pagination"
	masterservice "finance/api/services/master"
	"finance/api/utils"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type BankController struct {
	bankService masterservice.BankService
}

func OpenBankRoutes(db *gorm.DB, r *gin.RouterGroup, bankService masterservice.BankService) {
	bankHandler := BankController{bankService: bankService}
	// r.Use(middlewares.SetupAuthenticationMiddleware())
	r.GET("/bank", middlewares.DBTransactionMiddleware(db), bankHandler.GetAllBank)
	r.GET("/bank/:Id", middlewares.DBTransactionMiddleware(db), bankHandler.GetBankByID)
	r.POST("/bank", middlewares.DBTransactionMiddleware(db), bankHandler.SaveBank)
	r.PATCH("/bank-change-status", middlewares.DBTransactionMiddleware(db), bankHandler.ChangeStatus)
}

// @Summary Get Bank All Data
// @Description REST API Bank
// @Accept json
// @Produce json
// @Tags Master : Bank
// @Success 200 {object} payloads.ResponsePagination
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param sort_of query string false "Sort Of: {column}"
// @Param sort_by query string false "Sort By: {asc}"
// @Param bank_code query string false "Bank Code"
// @Param bank_name query string false "Bank Name"
// @Param bank_abbr query string false "Bank Abbreviation"
// @Param is_active query string false "Is Active"
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank [get]
func (r *BankController) GetAllBank(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	limit, _ := strconv.Atoi(c.Query("limit"))
	page, _ := strconv.Atoi(c.Query("page"))
	bankCode := c.Query("bank_code")
	bankName := c.Query("bank_name")
	bankAbbr := c.Query("bank_abbr")
	isActive, _ := strconv.ParseBool(c.Query("is_active"))
	sortOf := c.Query("sort_of")
	sortBy := c.Query("sort_by")

	get, err := r.bankService.WithTrx(trxHandle).GetAllBank(masterpayloads.GetBankRequests{
		BankCode: bankCode,
		BankName: bankName,
		BankAbbr: bankAbbr,
		IsActive: utils.BoolPtr(isActive),
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

	payloads.HandleSuccessPagination(c, get.Rows, "Get Data Successfully!", 200, get.Limit, get.Page, get.TotalRows, get.TotalPages)
}

// @Summary Get Bank By ID
// @Description REST API Bank
// @Accept json
// @Produce json
// @Tags Master : Bank
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank/{Id} [get]
func (r *BankController) GetBankByID(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	CodeId := c.Param("Id")
	Id, err := strconv.Atoi(CodeId)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	result, err := r.bankService.WithTrx(trxHandle).GetBankByID(Id)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	if result.BankId == 0 {
		exceptions.NotFoundException(c, "Bank Data Not Found!")
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Successfully!", http.StatusOK)
}

// @Summary Save Bank
// @Description REST API Bank
// @Accept json
// @Produce json
// @Tags Master : Bank
// @Param reqBody body masterpayloads.SaveBankRequests true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank/{Id} [post]
func (r *BankController) SaveBank(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	inpData := masterpayloads.SaveBankRequests{}
	err := c.ShouldBindJSON(&inpData)
	if err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}
	update, err := r.bankService.WithTrx(trxHandle).Save(inpData)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, update, "Save Bank Successfully!", http.StatusCreated)
}

// @Summary Change Status Bank
// @Description REST API Bank
// @Accept json
// @Produce json
// @Tags Master : Bank
// @Param reqBody body masterpayloads.ChangeStatusBankRequests true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-change-status [patch]
func (r *BankController) ChangeStatus(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	inpData := masterpayloads.ChangeStatusBankRequests{}
	err := c.ShouldBindJSON(&inpData)
	if err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}
	inpData.IsActive = !inpData.IsActive

	save, err := r.bankService.WithTrx(trxHandle).ChangeStatus(inpData)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, save, "Change Status Bank Successfully!", http.StatusCreated)
}
