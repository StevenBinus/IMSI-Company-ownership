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

type BankBranchController struct {
	bankBranchService masterservice.BankBranchService
}

func OpenBankBranchRoutes(db *gorm.DB, r *gin.RouterGroup, bankBranchService masterservice.BankBranchService) {
	bankBranchHandler := BankBranchController{bankBranchService: bankBranchService}
	// r.Use(middlewares.SetupAuthenticationMiddleware())
	r.GET("/bank-branch", middlewares.DBTransactionMiddleware(db), bankBranchHandler.GetAllBankBranch)
	r.GET("/bank-branch/:Id", middlewares.DBTransactionMiddleware(db), bankBranchHandler.GetBankBranchByID)
	r.POST("/bank-branch", middlewares.DBTransactionMiddleware(db), bankBranchHandler.SaveBankBranch)
	r.PATCH("/bank-branch-change-status", middlewares.DBTransactionMiddleware(db), bankBranchHandler.ChangeStatus)
}

// @Summary Get Bank Branch All Data
// @Description REST API Company
// @Accept json
// @Produce json
// @Tags Master : Bank Branch
// @Success 200 {object} payloads.ResponsePagination
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param sort_of query string false "Sort Of: {column}"
// @Param sort_by query string false "Sort By: {asc}"
// @Param bank_id query string false "Bank ID"
// @Param bank_code query string false "Bank Code"
// @Param bank_branch_code query string false "Bank Branch Code"
// @Param bank_branch_name query string false "Bank Branch Name"
// @Param is_active query string false "Is Active"
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-branch [get]
func (r *BankBranchController) GetAllBankBranch(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	limit, _ := strconv.Atoi(c.Query("limit"))
	page, _ := strconv.Atoi(c.Query("page"))
	sortOf := c.Query("sort_of")
	sortBy := c.Query("sort_by")
	bankId, _ := strconv.Atoi(c.Query("bank_id"))
	bankCode := c.Query("bank_code")
	bankBranchCode := c.Query("bank_branch_code")
	bankBranchName := c.Query("bank_branch_name")
	isActive, _ := strconv.ParseBool(c.Query("is_active"))

	get, err := r.bankBranchService.WithTrx(trxHandle).GetAllBankBranch(masterpayloads.GetBankBranchRequests{
		BankId:         bankId,
		BankCode:       bankCode,
		BankBranchCode: bankBranchCode,
		BankBranchName: bankBranchName,
		IsActive:       utils.BoolPtr(isActive),
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

	payloads.HandleSuccessPagination(c, get.Rows, "Get Data Successfully!", 200, get.Limit, get.Page, get.TotalRows, get.TotalPages)
}

// @Summary Get Bank Branch By ID
// @Description REST API Company
// @Accept json
// @Produce json
// @Tags Master : Bank Branch
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-branch/{Id} [get]
func (r *BankBranchController) GetBankBranchByID(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	CodeId := c.Param("Id")
	Id, err := strconv.Atoi(CodeId)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	result, err := r.bankBranchService.WithTrx(trxHandle).GetBankBranchByID(Id)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	if result.BankBranchId == 0 {
		exceptions.NotFoundException(c, "Bank Branch Data Not Found!")
		return
	}
	payloads.HandleSuccess(c, result, "Get Data Successfully!", http.StatusOK)
}

// @Summary Save Bank Branch
// @Description REST API Company
// @Accept json
// @Produce json
// @Tags Master : Bank Branch
// @Param reqBody body masterpayloads.SaveBankBranchRequests true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-branch/{Id} [post]
func (r *BankBranchController) SaveBankBranch(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	inp_data := masterpayloads.SaveBankBranchRequests{}
	err := c.ShouldBindJSON(&inp_data)
	if err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}
	update, err := r.bankBranchService.WithTrx(trxHandle).Save(inp_data)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}
	payloads.HandleSuccess(c, update, "Save Bank Branch Successfully!", http.StatusCreated)
}

// @Summary Change Status Bank Branch
// @Description REST API Bank
// @Accept json
// @Produce json
// @Tags Master : Bank Branch
// @Param reqBody body masterpayloads.ChangeStatusBankBranchRequests true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/bank-branch-change-status [patch]
func (r *BankBranchController) ChangeStatus(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	inpData := masterpayloads.ChangeStatusBankBranchRequests{}
	err := c.ShouldBindJSON(&inpData)
	if err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}
	inpData.IsActive = !inpData.IsActive

	save, err := r.bankBranchService.WithTrx(trxHandle).ChangeStatus(inpData)
	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, save, "Change Status Bank Successfully!", http.StatusCreated)
}
