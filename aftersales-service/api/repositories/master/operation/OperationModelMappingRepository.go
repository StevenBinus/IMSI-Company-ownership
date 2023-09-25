package masteroperationrepository

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
)

type OperationModelMappingRepository interface {
	GetOperationModelMappingById(int32) (masteroperationpayloads.OperationModelMappingResponse, error)
}
