package route

import (
	"finance/api/config"
	mastercontrollers "finance/api/controllers/master"
	accountreceivablecontroller "finance/api/controllers/transaction/account-receivable"
	"finance/api/middlewares"
	masterrepoimpl "finance/api/repositories/master/repository-impl"
	accountreceivablerepoimpl "finance/api/repositories/transaction/account-receivable/repository-impl"
	currencycodeserviceimpl "finance/api/services/master/service-impl"
	masterserviceimpl "finance/api/services/master/service-impl"
	accountreceivableserviceimpl "finance/api/services/transaction/account-receivable/services-impl"
	_ "finance/docs"
	"fmt"
	"net"
	"net/http"

	"github.com/gin-gonic/gin"
	log "github.com/sirupsen/logrus"
	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
	"gorm.io/gorm"
)

func CreateHandler(db *gorm.DB, env string) {
	r := gin.New()

	accountReceivableRepo := accountreceivablerepoimpl.OpenAccountReceivableRepository(db)
	currencyCodeRepo := masterrepoimpl.StartCurrencyCodeRepoImpl(db)
	bankRepo := masterrepoimpl.OpenBankRepoImpl(db)
	bankBranchRepo := masterrepoimpl.OpenBankBranchRepoImpl(db)
	bankContactRepo := masterrepoimpl.OpenBankContactRepoImpl(db)
	exchangeRateTypeRepo := masterrepoimpl.OpenExchangeRateTypeImpl(db)

	accountReceivableService := accountreceivableserviceimpl.OpenAccountReceivableUnitService(accountReceivableRepo)
	currencycodeService := currencycodeserviceimpl.StartCurrencyCodeService(currencyCodeRepo)
	bankService := masterserviceimpl.OpenBankService(bankRepo)
	bankBranchService := masterserviceimpl.OpenBankBranchService(bankBranchRepo)
	bankContactService := masterserviceimpl.OpenBankContactService(bankContactRepo)
	exchangeRateTypeService := masterserviceimpl.OpenExchangeRateTypeService(exchangeRateTypeRepo)

	r.Use(middlewares.SetupCorsMiddleware())

	if env != "prod" {
		r.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
	}

	api := r.Group("/api")

	accountreceivablecontroller.OpenAccountReceivableUnitRoutes(db, api.Group("/transaction"), accountReceivableService)
	mastercontrollers.StartCurrencyCodeRoutes(db, api.Group("/master"), currencycodeService)
	mastercontrollers.OpenBankRoutes(db, api.Group("/master"), bankService)
	mastercontrollers.OpenBankBranchRoutes(db, api.Group("/master"), bankBranchService)
	mastercontrollers.OpenBankContactRoutes(db, api.Group("/master"), bankContactService)
	mastercontrollers.OpenExchangeRateTypeRoutes(db, api.Group("/master"), exchangeRateTypeService)

	server := &http.Server{Handler: r}
	l, err := net.Listen("tcp4", fmt.Sprintf(":%v", config.EnvConfigs.Port))
	err = server.Serve(l)
	if err != nil {
		log.Fatal(err)
		return
	}
}
