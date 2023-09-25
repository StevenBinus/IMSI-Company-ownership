package masteroperationserviceimpl

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	masteroperationrepository "after-sales/api/repositories/master/operation"
	masteroperationservice "after-sales/api/services/master/operation"
)

type OperationEntriesServiceImpl struct {
	operationEntriesRepo masteroperationrepository.OperationEntriesRepository
}

func StartOperationEntriesService(operationEntriesRepo masteroperationrepository.OperationEntriesRepository) masteroperationservice.OperationEntriesService {
	return &OperationEntriesServiceImpl{
		operationEntriesRepo: operationEntriesRepo,
	}
}

func (s *OperationEntriesServiceImpl) GetOperationEntriesById(id int32) (masteroperationpayloads.OperationEntriesResponse, error) {
	value, err := s.operationEntriesRepo.GetOperationEntriesById(id)
	if err != nil {
		return masteroperationpayloads.OperationEntriesResponse{}, err
	}
	return value, nil
}
