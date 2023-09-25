package masteroperationserviceimpl

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	masteroperationrepository "after-sales/api/repositories/master/operation"
	masteroperationservice "after-sales/api/services/master/operation"
)

type OperationCodeServiceImpl struct {
	operationCodeRepo masteroperationrepository.OperationCodeRepository
}

func StartOperationCodeService(operationCodeRepo masteroperationrepository.OperationCodeRepository) masteroperationservice.OperationCodeService {
	return &OperationCodeServiceImpl{
		operationCodeRepo: operationCodeRepo,
	}
}

func (s *OperationCodeServiceImpl) GetOperationCodeById(id int32) (masteroperationpayloads.OperationCodeResponse, error) {
	value, err := s.operationCodeRepo.GetOperationCodeById(id)
	if err != nil {
		return masteroperationpayloads.OperationCodeResponse{}, err
	}

	return value, nil
}
