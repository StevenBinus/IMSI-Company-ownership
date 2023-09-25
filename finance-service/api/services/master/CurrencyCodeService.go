package masterservice

import (
	masterentities "finance/api/entities/master"
	currencycodepayloads "finance/api/payloads/master"

	"gorm.io/gorm"
)

type CurrencyCodeService interface {
	WithTrx(Trxhandle *gorm.DB) CurrencyCodeService
	GetAllCurrencyCodes() ([]currencycodepayloads.CurrencyCodeResponses, error)
	GetCurrencyCodeByID(id int) (currencycodepayloads.CurrencyCodeResponses, error)
	CreateCurrencyCode(currencycodepayloads.CurrencyCodeRequest) (bool, error)
	UpdateCurrencyCode(masterentities.MtrCurrency) (bool, error)
}
