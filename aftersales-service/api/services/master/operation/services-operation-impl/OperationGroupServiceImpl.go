package masteroperationserviceimpl

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	masteroperationrepository "after-sales/api/repositories/master/operation"
	masteroperationservice "after-sales/api/services/master/operation"
	"after-sales/api/utils"

	"gorm.io/gorm"
)

type OperationGroupServiceImpl struct {
	operationGroupRepo masteroperationrepository.OperationGroupRepository
}

func StartOperationGroupService(operationGroupRepo masteroperationrepository.OperationGroupRepository) masteroperationservice.OperationGroupService {
	return &OperationGroupServiceImpl{
		operationGroupRepo: operationGroupRepo,
	}
}
func (r *OperationGroupServiceImpl) WithTrx(trxHandle *gorm.DB) masteroperationservice.OperationGroupService {
	r.operationGroupRepo = r.operationGroupRepo.WithTrx(trxHandle)
	return r
}

func (s *OperationGroupServiceImpl) GetAllOperationGroupIsActive() ([]masteroperationpayloads.OperationGroupHeader, error) {
	var responses []masteroperationpayloads.OperationGroupHeader
	results, err := s.operationGroupRepo.GetAllOperationGroupIsActive()
	if err != nil {
		return responses, err
	}
	for _, value := range results {
		response := masteroperationpayloads.OperationGroupHeader{
			IsActive:                  value.IsActive,
			OperationGroupId:          value.OperationGroupId,
			OperationGroupCode:        value.OperationGroupCode,
			OperationGroupDescription: value.OperationGroupDescription,
		}
		responses = append(responses, response)
	}
	return responses, nil
}

func (s *OperationGroupServiceImpl) GetOperationGroupById(id int) (masteroperationpayloads.OperationGroupHeader, error) {
	value, err := s.operationGroupRepo.GetOperationGroupById(id)

	if err != nil {
		return masteroperationpayloads.OperationGroupHeader{}, err
	}
	return value, nil
}

func (s *OperationGroupServiceImpl) GetOperationGroupByCode(Code string) (masteroperationpayloads.OperationGroupHeader, error) {
	value, err := s.operationGroupRepo.GetOperationGroupByCode(Code)
	if err != nil {
		return masteroperationpayloads.OperationGroupHeader{}, err
	}
	return value, nil
}

func (s *OperationGroupServiceImpl) GetAllOperationGroup(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error) {
	results, err := s.operationGroupRepo.GetAllOperationGroup(queryCriteria, sortField, pages)
	if err != nil {
		return pages, err
	}
	return results, nil
}

func (r *OperationGroupServiceImpl) ChangeStatusOperationGroup(oprId int) (bool, error) {
	updates, err := r.operationGroupRepo.ChangeStatusOperationGroup(oprId)
	if err != nil {
		return false, err
	}
	return updates, nil
}

func (r *OperationGroupServiceImpl) SaveOperationGroup(req masteroperationpayloads.OperationGroupHeader) (bool, error) {
	save, err := r.operationGroupRepo.SaveOperationGroup(req)
	if err != nil {
		return false, err
	}
	return save, nil
}
