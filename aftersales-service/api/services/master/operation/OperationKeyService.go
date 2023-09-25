package masteroperationservice

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
)

type OperationKeyService interface {
	GetOperationKeyById(int32) (masteroperationpayloads.OperationKeyResponse, error)
}
