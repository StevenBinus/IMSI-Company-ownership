package mastercontrollers

import (
	"finance/api/exceptions"
	"finance/api/middlewares"
	"finance/api/payloads"
	masterpayloads "finance/api/payloads/master"
	"finance/api/payloads/pagination"
	masterservice "finance/api/services/master"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type BankContactController struct {
	bankContactService masterservice.BankContactService
}

func OpenBankContactRoutes(db *gorm.DB, r *gin.RouterGroup, bankContactService masterservice.BankContactService) {
	bankContactHandler := BankContactController{bankContactService: bankContactService}
	// r.Use(middlewares.SetupAuthenticationMiddleware())
	r.GET("/bank-contact", middlewares.DBTransactionMiddleware(db), bankContactHandler.GetAllBankContact)
	r.GET("/bank-contact/:Id", middlewares.DBTransactionMiddleware(db), bankContactHandler.GetBankContactByID)
	r.POST("/bank-contact", middlewares.DBTransactionMiddleware(db), bankContactHandler.SaveBankContact)
	r.PATCH("/bank-contact-change-status", middlewares.DBTransactionMiddleware(db), bankContactHandler.ChangeStatus)
}

// @Summary Get Bank Contact All Data
// @Description REST API Company
// @Accept json
// @Produce json
// @Tags Master : Bank Contact
// @Success 200 {object} payloads.Response
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param sort_of query string false "Sort Of: {column}"
// @Param sort_by query string false "Sort By: {asc}"
// @Param bank_branch_id query string false "Bank Branch ID"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-contact [get]
func (r *BankContactController) GetAllBankContact(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	limit, _ := strconv.Atoi(c.Query("limit"))
	page, _ := strconv.Atoi(c.Query("page"))
	sortOf := c.Query("sort_of")
	sortBy := c.Query("sort_by")
	bankBranchId, _ := strconv.Atoi(c.Query("bank_branch_id"))

	get, err := r.bankContactService.WithTrx(trxHandle).GetAllBankContact(masterpayloads.GetBankContactRequests{
		BankBranchId: bankBranchId,
	}, pagination.Pagination{
		Limit:  limit,
		Page:   page,
		SortOf: sortOf,
		SortBy: sortBy,
	})

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	payloads.HandleSuccessPagination(c, get, "Get Data Successfully!", 200, get.Limit, get.Page, get.TotalRows, get.TotalPages)
}

// @Summary Get Bank Contact By ID
// @Description REST API Company
// @Accept json
// @Produce json
// @Tags Master : Bank Contact
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-contact/{Id} [get]
func (r *BankContactController) GetBankContactByID(c *gin.Context) {
	CodeId := c.Param("Id")
	Id, err := strconv.Atoi(CodeId)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	result, err := r.bankContactService.GetBankContactByID(Id)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	if result.BankBranchId == 0 {
		exceptions.NotFoundException(c, "Bank Contact Data Not Found!")
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Successfully!", http.StatusOK)
}

// @Summary Save Bank Contact
// @Description REST API Company
// @Accept json
// @Produce json
// @Tags Master : Bank Contact
// @Param reqBody body masterpayloads.SaveBankContactRequests true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-contact/{Id} [post]
func (r *BankContactController) SaveBankContact(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	inp_data := masterpayloads.SaveBankContactRequests{}
	err := c.ShouldBindJSON(&inp_data)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	update, err := r.bankContactService.WithTrx(trxHandle).Save(inp_data)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, update, "Save Bank Contact Successfully!", http.StatusCreated)
}

// @Summary Change Status Bank Contact
// @Description REST API Bank
// @Accept json
// @Produce json
// @Tags Master : Bank Contact
// @Param reqBody body masterpayloads.ChangeStatusBankContactRequests true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-contact-change-status [patch]
func (r *BankContactController) ChangeStatus(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	inpData := masterpayloads.ChangeStatusBankContactRequests{}
	err := c.ShouldBindJSON(&inpData)
	if err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}
	inpData.IsActive = !inpData.IsActive

	save, err := r.bankContactService.WithTrx(trxHandle).ChangeStatus(inpData)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, save, "Change Status Bank Successfully!", http.StatusOK)
}
