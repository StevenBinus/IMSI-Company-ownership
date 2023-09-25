package masteroperationservice

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
)

type OperationCodeService interface {
	GetOperationCodeById(int32) (masteroperationpayloads.OperationCodeResponse, error)
}
