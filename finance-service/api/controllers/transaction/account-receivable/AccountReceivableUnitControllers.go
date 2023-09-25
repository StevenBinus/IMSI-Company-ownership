package accountreceivablecontroller

import (
	"finance/api/exceptions"
	"finance/api/middlewares"
	"finance/api/payloads"
	"finance/api/payloads/pagination"
	accountreceivablepayloads "finance/api/payloads/transaction/account-receivable"
	accountreceivableservice "finance/api/services/transaction/account-receivable"
	"finance/api/utils"
	"fmt"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type AccountReceivableUnitController struct {
	accountReceivableService accountreceivableservice.AccountReceivableUnitService
}

func OpenAccountReceivableUnitRoutes(
	db *gorm.DB,
	r *gin.RouterGroup,
	accountReceivableService accountreceivableservice.AccountReceivableUnitService,
) {
	accountReceivableUnitHandler := AccountReceivableUnitController{
		accountReceivableService: accountReceivableService,
	}

	// r.Use(middlewares.SetupAuthenticationMiddleware())
	r.POST("/save-account-receivable-unit", middlewares.DBTransactionMiddleware(db), accountReceivableUnitHandler.Save)
	r.PATCH("/account-receivable-unit/:invoice_unit_system_number", middlewares.DBTransactionMiddleware(db), accountReceivableUnitHandler.UpdateStatus)
	r.GET("/account-receivable-unit/:invoice_unit_system_number", middlewares.DBTransactionMiddleware(db), accountReceivableUnitHandler.GetById)
	r.GET("/account-receivable-unit", middlewares.DBTransactionMiddleware(db), accountReceivableUnitHandler.GetAll)
	// r.POST("/add-line-account-receivable-unit", middlewares.DBTransactionMiddleware(db), accountReceivableUnitHandler.AddLine)
}

// @Summary Save Account Receivable Unit
// @Description Save Account Receivable Unit
// @Accept json
// @Produce json
// @Tags Transaction : Account Receivable Unit
// @Security BearerAuth
// @param reqBody body accountreceivablepayloads.SaveHeaderRequest true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /transaction/save-account-receivable-unit [post]
func (r *AccountReceivableUnitController) Save(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	var requestBody accountreceivablepayloads.SaveHeaderRequest
	var vatRequest accountreceivablepayloads.UpdateVatRequest

	if err := c.ShouldBindJSON(&requestBody); err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}

	requestBody.InvoiceStatusId = 1

	if requestBody.InvoiceUnitSystemNumber == 0 {
		insert, err := r.accountReceivableService.WithTrx(trxHandle).SaveHeader(requestBody, vatRequest)

		if err != nil {
			exceptions.AppException(c, err.Error())
			return
		}

		payloads.HandleSuccess(c, insert, "Unit Invoice Insert Successfully!", http.StatusCreated)
	} else {
		check, err := r.accountReceivableService.WithTrx(trxHandle).GetById(requestBody.InvoiceUnitSystemNumber)

		if err != nil {
			exceptions.AppException(c, err.Error())
			return
		}

		if check.InvoiceStatusId != 1 {
			exceptions.BadRequestException(c, "Approval is not draft")
			return
		}

		if !check.IsActive {
			exceptions.BadRequestException(c, "Change your active status to Active before Updating data!")
			return
		}

		// Transaction Type == SU05 - Internal
		if requestBody.TransactionTypeAccountReceviableUnitId == 1 {
			fmt.Println("Logic for VAT_PERCENT, TOTAL_VAT, TOTAL_VAT_BASE_AMOUNT, TOTAL_AFTER_VAT, TOTAL_AFTER_BASE_VAT_AMOUNT")
			// Option = 7
			// SET @Vat_Percent = dbo.getTaxPercent(dbo.getVariableValue('TAX_TYPE_PPN'), dbo.getVariableValue('TAX_SERV_CODE_PPN'), ISNULL(@Inv_Date,GETDATE()))

			// 	UPDATE rtInvoice0
			// 	SET VAT_PERCENT = @Vat_Percent
			// 		, TOTAL_VAT = ROUND(TOTAL_AFTER_DISC * @Vat_Percent / 100,0,-1)
			// 		, TOTAL_VAT_BASE_AMOUNT = ROUND(TOTAL_AFTER_DISC_BASE_AMOUNT * @Vat_Percent / 100,0,-1)
			// 		, TOTAL_AFTER_VAT =TOTAL_AFTER_DISC +  ROUND((TOTAL_AFTER_DISC * @Vat_Percent / 100),0,-1)
			// 		, TOTAL_AFTER_VAT_BASE_AMOUNT = TOTAL_AFTER_DISC_BASE_AMOUNT + ROUND((TOTAL_AFTER_DISC_BASE_AMOUNT * @Vat_Percent / 100),0,-1)
			// 	WHERE INV_SYS_NO = @Inv_Sys_No
		} else {
			vatRequest = accountreceivablepayloads.UpdateVatRequest{
				VatPercent:              0,
				TotalVat:                0,
				TotalVatBaseAmount:      0,
				TotalAfterVat:           check.TotalAfterVat,
				TotalAfterVatBaseAmount: check.TotalAfterVatBaseAmount,
				IsUpdate:                true,
			}
		}

		// get is_use_tax_industry
		isUseTaxIndustry := 0

		// must check from mtr_ref with IS_USE_TAX_INDUSTRY column ( call API )
		if isUseTaxIndustry == 1 {
			totalVatSummary := check.TotalAfterDiscount + vatRequest.TotalVat + check.TaxIndustryAmount

			vatRequest = accountreceivablepayloads.UpdateVatRequest{
				TotalAfterVat:           totalVatSummary,
				TotalAfterVatBaseAmount: totalVatSummary,
				IsUpdate:                true,
			}
		}

		update, err := r.accountReceivableService.WithTrx(trxHandle).SaveHeader(requestBody, vatRequest)

		if err != nil {
			exceptions.AppException(c, err.Error())
			return
		}

		payloads.HandleSuccess(c, update, "Unit Invoice Update Successfully!", http.StatusCreated)
	}
}

// @Summary Change Status Account Receivable Unit
// @Description Change Status Account Receivable Unit
// @Accept json
// @Produce json
// @Tags Transaction : Account Receivable Unit
// @Security BearerAuth
// @Param invoice_unit_system_number path string true "invoice_unit_system_number"
// @param reqBody body accountreceivablepayloads.UpdateStatusRequest true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /transaction/account-receivable-unit/{invoice_unit_system_number} [patch]
func (r *AccountReceivableUnitController) UpdateStatus(c *gin.Context) {
	invoiceUnitSystemNumber, _ := strconv.Atoi(c.Param("invoice_unit_system_number"))
	var request accountreceivablepayloads.UpdateStatusRequest

	if err := c.ShouldBindJSON(&request); err != nil {
		exceptions.EntityException(c, err.Error())
		return
	}

	get, err := r.accountReceivableService.GetById(invoiceUnitSystemNumber)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if get.InvoiceUnitSystemNumber == 0 {
		exceptions.NotFoundException(c, "Account Receivable Unit Invoice Not Found")
		return
	}

	updates, err := r.accountReceivableService.UpdateStatus(invoiceUnitSystemNumber, request)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	payloads.HandleSuccess(c, updates, "Change Status Successfully!", http.StatusOK)
}

// @Summary Get All Account Receivable Unit
// @Description Get All Account Receivable Unit
// @Accept json
// @Produce json
// @Tags Transaction : Account Receivable Unit
// @Security BearerAuth
// @Param limit query string true "Limit"
// @Param page query string true "Page"
// @Param sort_of query string false "Sort Of: {column}"
// @Param sort_by query string false "Sort By: {asc}"
// @Param company_id query string true "Company Id"
// @Param brand_id query string false "Brand Id"
// @Param invoice_unit_document_number query string false "Invoice Unit Document Number"
// @Param invoice_date_from query string false "Invoice Date From"
// @Param invoice_date_to query string false "Invoice Date To"
// @Param invoice_due_date_from query string false "Invoice Due Date From"
// @Param invoice_due_date_to query string false "Invoice Due Date To"
// @Param customer_id query string false "Customer Id"
// @Param bill_to_customer_id query string false "Bill To Customer Id"
// @Param transaction_type_account_receviable_unit_id query string false "Transaction Type Unit Id"
// @Param invoice_status_id query string false "Invoice Status Id"
// @Param vehicle_chassis_no query string false "Vehicle Chassis No"
// @Success 200 {object} payloads.ResponsePagination
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /transaction/account-receivable-unit [get]
func (r *AccountReceivableUnitController) GetAll(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	limit, _ := strconv.Atoi(c.Query("limit"))
	page, _ := strconv.Atoi(c.Query("page"))
	sortOf := c.Query("sort_of")
	sortBy := c.Query("sort_by")
	companyId, _ := strconv.Atoi(c.Query("company_id"))
	brandId, _ := strconv.Atoi(c.Query("brand_id"))
	invoiceUnitDocNo := c.Query("invoice_unit_document_number")
	invoiceDateFrom, _ := time.Parse("2006-01-02T15:04:05Z", c.Query("invoice_date_from"))
	invoiceDateTo, _ := time.Parse("2006-01-02T15:04:05Z", c.Query("invoice_date_to"))
	invoiceDueDateFrom, _ := time.Parse("2006-01-02T15:04:05Z", c.Query("invoice_due_date_from"))
	invoiceDueDateTo, _ := time.Parse("2006-01-02T15:04:05Z", c.Query("invoice_due_date_to"))
	customerId, _ := strconv.Atoi(c.Query("customer_id"))
	billToCustomerId, _ := strconv.Atoi(c.Query("bill_to_customer_id"))
	transactionTypeUnitId, _ := strconv.Atoi(c.Query("transaction_type_account_receviable_unit_id"))
	vehicleChassisNo := c.Query("vehicle_chassis_no")
	var tempBrandId []int

	get, err := r.accountReceivableService.WithTrx(trxHandle).GetAll(accountreceivablepayloads.GetAllHeaderRequest{
		CompanyId:                              companyId,
		BrandId:                                brandId,
		InvoiceUnitDocumentNumber:              invoiceUnitDocNo,
		InvoiceDateFrom:                        invoiceDateFrom,
		InvoiceDateTo:                          invoiceDateTo,
		InvoiceDueDateFrom:                     invoiceDueDateFrom,
		InvoiceDueDateTo:                       invoiceDueDateTo,
		CustomerId:                             customerId,
		BillToCustomerId:                       billToCustomerId,
		TransactionTypeAccountReceviableUnitId: transactionTypeUnitId,
		VehicleChassisNo:                       vehicleChassisNo,
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
	if len(get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)) != 0 {
		for i := range get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse) {
			tempBrandId = append(tempBrandId, get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)[i].BrandId)
		}
		var getBrand accountreceivablepayloads.GetBrandResponse

		urlBrand := utils.URL + "/sales-service/api/sales/unit-brand/" + fmt.Sprint(tempBrandId[0])

		errUrlBrand := utils.Get(c, urlBrand, &getBrand, nil)

		if errUrlBrand != nil {
			exceptions.BadRequestException(c, "Error Consume External API!")
			return
		}

		for i := range get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse) {
			if get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)[i].BrandId == getBrand.BrandId {
				get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)[i].BrandName = getBrand.BrandName
			}
		}
		for i := range get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse) {
			if get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)[i].BrandId == getBrand.BrandId {
				get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)[i].CustomerName = getBrand.BrandName
			}
		}
		for i := range get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse) {
			if get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)[i].BrandId == getBrand.BrandId {
				get.Rows.([]accountreceivablepayloads.GetAllHeaderResponse)[i].BillToCustomerName = getBrand.BrandName
			}
		}
	}
	payloads.HandleSuccessPagination(c, get.Rows, "Get Data Successfully!", 200, get.Limit, get.Page, get.TotalRows, get.TotalPages)
}

// @Summary Get Account Receivable Unit By Id
// @Description Get Account Receivable Unit By Id
// @Accept json
// @Produce json
// @Tags Transaction : Account Receivable Unit
// @Security BearerAuth
// @Param invoice_unit_system_number path string true "invoice_unit_system_number"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/transaction/account-receivable-unit/{invoice_unit_system_number} [get]
func (r *AccountReceivableUnitController) GetById(c *gin.Context) {
	trxHandle := c.MustGet("db_trx").(*gorm.DB)
	invoiceUnitSystemNumber, _ := strconv.Atoi(c.Param("invoice_unit_system_number"))

	get, err := r.accountReceivableService.WithTrx(trxHandle).GetById(invoiceUnitSystemNumber)

	if err != nil {
		exceptions.AppException(c, err.Error())
		return
	}

	if get.InvoiceUnitSystemNumber == 0 {
		exceptions.NotFoundException(c, "Account Receivable Data Not Found!")
		return
	}

	payloads.HandleSuccess(c, get, "Get Data Successfully!", http.StatusOK)
}

// @Summary Save Account Receivable Unit
// @Description Save Account Receivable Unit
// @Accept json
// @Produce json
// @Tags Transaction : Account Receivable Unit
// @Security BearerAuth
// @param reqBody body accountreceivablepayloads.AddLineHeaderRequest true "Form Request"
// @Success 200 {object} payloads.Response
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /api/transaction/add-line-account-receivable-unit [post]
// func (r *AccountReceivableUnitController) AddLine(c *gin.Context) {
// 	trxHandle := c.MustGet("db_trx").(*gorm.DB)
// 	var requestBody accountreceivablepayloads.AddLineHeaderRequest
// 	// suppTypeDealer := "Supplier Type Dealer" // SUPPTYPE_DEALER
// 	// custTypeDealer := "Dealer" // CUST_TYPE_DEALER
// 	// custTypeAtpm := "Related Parties – IMSI" // CUST_TYPE_ATPM
// 	// suppTypeAtpm := "Related Parties – IMSI" // SUPPTYPE_ATPM
// 	// approvalApproved := "Approved" // APPROVAL_APPROVED
// 	// approvalConfirmed := "Confirmed" // APPROVAL_CONFIRMED
// 	// approvalDraft := "Draft" // APPROVAL_DRAFT
// 	// approvalWaitApproved := "Wait Approve" // APPROVAL_WAITAPPROVED
// 	// taxInvoiceTypeStd := "Faktur Pajak Standar" // TAXINVTYPE_STD
// 	// accountReceivableInvoiceTypeUnit := "AI01" // AR_INV_TYPE_UNIT
// 	var isDistributor bool
// 	var withVat bool

// 	if err := c.ShouldBindJSON(&requestBody); err != nil {
// 		exceptions.EntityException(c, err.Error())
// 		return
// 	}

// 	// select @isDistributor = isnull(IS_DISTRIBUTOR,'0') from gmComp0 where COMPANY_CODE = @Company_Code

// 	if requestBody.TransactionTypeAccountReceviableUnitId == 6 && requestBody.TransactionTypeAccountReceviableUnitId != 5 ||
// 		requestBody.TransactionTypeAccountReceviableUnitId != 5 && withVat {

// 	}
// }
