package route

import (
	"after-sales/api/config"
	masteritemcontroller "after-sales/api/controllers/master/item"
	masteroperationcontroller "after-sales/api/controllers/master/operation"
	transactionworkshopcontroller "after-sales/api/controllers/transactions/workshop"

	"after-sales/api/middlewares"
	masteritemrepositoryimpl "after-sales/api/repositories/master/item/repositories-item-impl"
	masteroperationrepositoryimpl "after-sales/api/repositories/master/operation/repositories-operation-impl"
	transactionworkshoprepositoryimpl "after-sales/api/repositories/transaction/workshop/repositories-workshop-impl"
	masteritemserviceimpl "after-sales/api/services/master/item/services-item-impl"
	masteroperationserviceimpl "after-sales/api/services/master/operation/services-operation-impl"
	transactionworkshopserviceimpl "after-sales/api/services/transaction/workshop/services-workshop-impl"
	_ "after-sales/docs"
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
	//mtr_operation_group
	operationGroupRepository := masteroperationrepositoryimpl.StartOperationGroupRepositoryImpl(db)
	operationGroupService := masteroperationserviceimpl.StartOperationGroupService(operationGroupRepository)
	//mtr_operation_section
	operationSectionRepository := masteroperationrepositoryimpl.StartOperationSectionRepositoryImpl(db)
	operationSectionService := masteroperationserviceimpl.StartOperationSectionService(operationSectionRepository)
	//mtr_operation_key
	// operationKeyRepository := operationkeyrepositoryimpl.StartOperationKeyRepositoryImpl(db)
	// operationKeyService := operationkeyserviceimpl.StartOperationMappingService(operationKeyRepository)
	// //mtr_operation_code
	// operationCodeRepository := operationcoderepositoryimpl.StartOperationCodeImpl(db)
	// operationCodeService := operationcodeserviceimpl.StartOperationCodeService(operationCodeRepository)
	// //mtr_operation_entries
	// operationEntriesRepository := operationentriesrepositoryimpl.StartOperationEntriesImpl(db)
	// operationEntriesService := operationentriesserviceimpl.StartOperationEntriesService(operationEntriesRepository)
	// //mtr_operation_model_mapping
	// operationModelMappingRepository := operationmodelmappingrepositoryimpl.StartOperationModelMappingRepositoryImpl(db)
	// operationModelMappingService := operationmodelmappingserviceimpl.StartOperationMappingService(operationModelMappingRepository)
	//mtr_item
	itemRepository := masteritemrepositoryimpl.StartItemRepositoryImpl(db)
	itemService := masteritemserviceimpl.StartItemService(itemRepository)

	bookingEstimationRepository := transactionworkshoprepositoryimpl.OpenBookingEstimationImpl(db)
	bookingEstimationService := transactionworkshopserviceimpl.OpenBookingEstimationServiceImpl(bookingEstimationRepository)

	r.Use(middlewares.SetupCorsMiddleware())

	if env != "prod" {
		r.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
	}

	api := r.Group("/api") //all need work at update boolean
	//master
	masteroperationcontroller.StartOperationGroupRoutes(db, api.Group("/master"), operationGroupService)     //done works
	masteroperationcontroller.StartOperationSectionRoutes(db, api.Group("/master"), operationSectionService) //done works
	// mastercontroller.StartOperationKeyRoutes(db, api.Group("/master"), operationKeyService)                   //done works
	// mastercontroller.StartOperationCodeRoutes(db, api.Group("/master"), operationCodeService)                 //done works
	// mastercontroller.StartOperationEntriesRoutes(db, api.Group("/master"), operationEntriesService)           //done works
	// mastercontroller.StartOperationModelMappingRoutes(db, api.Group("/master"), operationModelMappingService) //done works
	masteritemcontroller.StartItemRoutes(db, api.Group("/master"), itemService) //done works
	// //transaction
	// transactioncontroller.StartSupplySlipRoutes(db, api.Group("/transaction"), supplySlipService) //done works

	transactionworkshopcontroller.OpenBookingEstimationRoutes(db, api.Group("/master"), bookingEstimationService)

	server := &http.Server{Handler: r}
	l, err := net.Listen("tcp4", fmt.Sprintf(":%v", config.EnvConfigs.Port))
	err = server.Serve(l)
	if err != nil {
		log.Fatal(err)
		return
	}
}
