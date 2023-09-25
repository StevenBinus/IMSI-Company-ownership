package mastertest

import (
	"finance/api/config"
	masterpayloads "finance/api/payloads/master"
	"finance/api/payloads/pagination"
	masterrepoimpl "finance/api/repositories/master/repository-impl"
	masterserviceimpl "finance/api/services/master/service-impl"
	"fmt"
	"testing"
)

func TestSaveExchangeRateType(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	exchangeRateTypeRepo := masterrepoimpl.OpenExchangeRateTypeImpl(db)
	exchangeRateTypeService := masterserviceimpl.OpenExchangeRateTypeService(exchangeRateTypeRepo)

	save, err := exchangeRateTypeService.Save(masterpayloads.SaveExchangeRateTypeRequest{
		IsActive: false,
		ExchangeRateTypeId: 5,
		ExchangeRateType: "kereeenn",
		Description: "wowww kerennn",
	})
	
	if err != nil {
		panic(err)
	}

	fmt.Println(save)
}

func TestChangeExchangeRateTypeStatus(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	exchangeRateTypeRepo := masterrepoimpl.OpenExchangeRateTypeImpl(db)
	exchangeRateTypeService := masterserviceimpl.OpenExchangeRateTypeService(exchangeRateTypeRepo)

	save, err := exchangeRateTypeService.ChangeStatus(1)
	
	if err != nil {
		panic(err)
	}

	fmt.Println(save)
}

func TestGetAll(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	exchangeRateTypeRepo := masterrepoimpl.OpenExchangeRateTypeImpl(db)
	exchangeRateTypeService := masterserviceimpl.OpenExchangeRateTypeService(exchangeRateTypeRepo)

	get, err := exchangeRateTypeService.GetAll(
		masterpayloads.GetAllExchangeRateTypeRequest{
			IsActive: "",
			ExchangeRateType: "test",
			Description: "test",
		},
		pagination.Pagination{
			Limit: 10,
			Page: 1,
		},
	)
	
	if err != nil {
		panic(err)
	}

	fmt.Println(get)
}

func TestGetById(t *testing.T) {
	config.InitEnvConfigs(true, "")
	db := config.InitDB()
	exchangeRateTypeRepo := masterrepoimpl.OpenExchangeRateTypeImpl(db)
	exchangeRateTypeService := masterserviceimpl.OpenExchangeRateTypeService(exchangeRateTypeRepo)

	save, err := exchangeRateTypeService.GetById(1)

	if err != nil {
		panic(err)
	}

	fmt.Println(save)
}