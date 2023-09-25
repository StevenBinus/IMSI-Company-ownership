package masteroperationrepository

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"

	"gorm.io/gorm"
)

type OperationEntriesRepository interface {
	WithTrx(trxHandle *gorm.DB) OperationEntriesRepository
	GetOperationEntriesById(int32) (masteroperationpayloads.OperationEntriesResponse, error)
}
