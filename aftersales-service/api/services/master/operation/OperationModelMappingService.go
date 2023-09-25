package masteroperationservice

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
)

type OperationModelMappingService interface {
	GetOperationModelMappingById(int32) (masteroperationpayloads.OperationModelMappingResponse, error)
}
