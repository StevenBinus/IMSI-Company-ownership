package masteroperationserviceimpl

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	masteroperationrepository "after-sales/api/repositories/master/operation"
	masteroperationservice "after-sales/api/services/master/operation"
)

type OperationModelMappingServiceImpl struct {
	operationModelMappingRepo masteroperationrepository.OperationModelMappingRepository
}

func StartOperationMappingService(operationModelMappingRepo masteroperationrepository.OperationModelMappingRepository) masteroperationservice.OperationModelMappingService {
	return &OperationModelMappingServiceImpl{
		operationModelMappingRepo: operationModelMappingRepo,
	}
}

func (s *OperationModelMappingServiceImpl) GetOperationModelMappingById(id int32) (masteroperationpayloads.OperationModelMappingResponse, error) {
	value, err := s.operationModelMappingRepo.GetOperationModelMappingById(id)
	if err != nil {
		return masteroperationpayloads.OperationModelMappingResponse{}, err
	}
	return value, nil
}
