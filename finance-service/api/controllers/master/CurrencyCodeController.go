package mastercontrollers

import (
	"finance/api/exceptions"
	"finance/api/middlewares"
	currencycodepayloads "finance/api/payloads/master"
	currencycodeservice "finance/api/services/master"
	"log"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type CurrencyCodeController struct {
	currencycodeservice currencycodeservice.CurrencyCodeService
}

func StartCurrencyCodeRoutes(db *gorm.DB, r *gin.RouterGroup, currencyCodeService currencycodeservice.CurrencyCodeService) {
	currencyCodeHandler := CurrencyCodeController{currencycodeservice: currencyCodeService}
	// r.Use(middlewares.SetupAuthenticationMiddleware())
	r.GET("/currency-code", currencyCodeHandler.GetAllCurrencyCodes)
	r.GET("/currency-code/:Id", currencyCodeHandler.GetCurrencyCodeByID)
	r.POST("/currency-code", middlewares.DBTransactionMiddleware(db), currencyCodeHandler.CreateCurrencyCode)
}

// @Summary Get All Currency Code Data
// @Description REST API Company
// @Accept json
// @Produce json
// @Tags Master : Currency Code
// @Success 200 {object} []currencycodepayloads.CurrencyCodeResponses
// @Failure 500,400,401,404,403,422 {object} exceptions.Error
// @Router /master/currency-code [get]
func (r *CurrencyCodeController) GetAllCurrencyCodes(c *gin.Context) {
	results, err := r.currencycodeservice.GetAllCurrencyCodes()
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
	}
	c.JSON(http.StatusOK, gin.H{"data": results})
}

func (r *CurrencyCodeController) GetCurrencyCodeByID(c *gin.Context) {
	CodeId := c.Param("Id")
	Id, err := strconv.Atoi(CodeId)
	if err != nil {
		log.Panic(err)
	}
	result, err := r.currencycodeservice.GetCurrencyCodeByID(Id)
	if err != nil {
		exceptions.NotFoundException(c, err.Error())
	}
	c.JSON(http.StatusOK, gin.H{"data": result})
}

func (r *CurrencyCodeController) CreateCurrencyCode(c *gin.Context) {
	inp_data := currencycodepayloads.CurrencyCodeRequest{}
	err := c.ShouldBindJSON(&inp_data)
	if err != nil {
		log.Panic((err))
	}
	r.currencycodeservice.CreateCurrencyCode(inp_data)
	c.JSON(http.StatusCreated, gin.H{"data": "created"})
}
