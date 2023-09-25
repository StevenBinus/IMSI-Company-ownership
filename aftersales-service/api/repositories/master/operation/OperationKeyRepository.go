package masteroperationrepository

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
)

type OperationKeyRepository interface {
	GetOperationKeyById(int32) (masteroperationpayloads.OperationKeyResponse, error)
	GetOperationKeyByCode(string) (masteroperationpayloads.OperationKeyResponse, error)
}
