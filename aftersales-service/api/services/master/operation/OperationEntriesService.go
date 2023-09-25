package masteroperationservice

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
)

type OperationEntriesService interface {
	GetOperationEntriesById(int32) (masteroperationpayloads.OperationEntriesResponse, error)
}
