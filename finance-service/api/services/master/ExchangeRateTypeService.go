package masterservice

import (
	masterentities "finance/api/entities/master"
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"

	"gorm.io/gorm"
)

type ExchangeRateTypeService interface {
	WithTrx(Trxhandle *gorm.DB) ExchangeRateTypeService
	Save(masterpayloads.SaveExchangeRateTypeRequest) (bool, error)
	GetAll(request masterpayloads.GetAllExchangeRateTypeRequest, pages pagination.Pagination) (pagination.Pagination, error)
	GetById(int) (masterentities.ExchangeRateType, error)
	GetByName(string) (masterentities.ExchangeRateType, error)
	ChangeStatus(int) (bool, error)
}
