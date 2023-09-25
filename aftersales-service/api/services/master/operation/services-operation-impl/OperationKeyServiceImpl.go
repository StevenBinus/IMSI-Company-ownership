package masteroperationserviceimpl

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	masteroperationrepository "after-sales/api/repositories/master/operation"
	masteroperationservice "after-sales/api/services/master/operation"
)

type OperationKeyServiceImpl struct {
	operationKeyRepo masteroperationrepository.OperationKeyRepository
}

func StartOperationKeyService(operationKeyRepo masteroperationrepository.OperationKeyRepository) masteroperationservice.OperationKeyService {
	return &OperationKeyServiceImpl{
		operationKeyRepo: operationKeyRepo,
	}
}

func (s *OperationKeyServiceImpl) GetOperationKeyById(id int32) (masteroperationpayloads.OperationKeyResponse, error) {
	value, err := s.operationKeyRepo.GetOperationKeyById(id)
	if err != nil {
		return masteroperationpayloads.OperationKeyResponse{}, err
	}
	return value, nil
}

func (s *OperationKeyServiceImpl) GetOperationKeyByCode(code string) (masteroperationpayloads.OperationKeyResponse, error) {
	value, err := s.GetOperationKeyByCode(code)
	if err != nil {
		return value, err
	}
	return value, nil
}
