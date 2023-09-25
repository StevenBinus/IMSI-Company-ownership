package masterrepo

import (
	masterentities "finance/api/entities/master"
	currencycodepayloads "finance/api/payloads/master"

	"gorm.io/gorm"
)

type CurrencyCodeRepository interface {
	WithTrx(Trxhandle *gorm.DB) CurrencyCodeRepository
	GetAllCurrencyCodes() ([]masterentities.MtrCurrency, error)
	GetCurrencyCodeByID(id int) (masterentities.MtrCurrency, error)
	CreateCurrencyCode(currencycodepayloads.CurrencyCodeRequest) (bool, error)
	UpdateCurrencyCode(masterentities.MtrCurrency) (bool, error)
	PatchStatusCurrencyCode(id int) bool
}
