package masteroperationrepository

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"

	"gorm.io/gorm"
)

type OperationCodeRepository interface {
	WithTrx(trxHandle *gorm.DB) OperationCodeRepository
	GetOperationCodeById(int32) (masteroperationpayloads.OperationCodeResponse, error)
}
