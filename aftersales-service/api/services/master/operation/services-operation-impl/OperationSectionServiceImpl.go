package masteroperationserviceimpl

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	masteroperationrepository "after-sales/api/repositories/master/operation"
	masteroperationservice "after-sales/api/services/master/operation"
	"after-sales/api/utils"

	// "after-sales/api/utils"
	"log"

	"gorm.io/gorm"
)

type OperationSectionServiceImpl struct {
	operationSectionRepo masteroperationrepository.OperationSectionRepository
}

func StartOperationSectionService(operationSectionRepo masteroperationrepository.OperationSectionRepository) masteroperationservice.OperationSectionService {
	return &OperationSectionServiceImpl{
		operationSectionRepo: operationSectionRepo,
	}
}

func (s *OperationSectionServiceImpl) GetAllOperationSectionList(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error) {
	results, err := s.operationSectionRepo.GetAllOperationSectionList(queryCriteria, sortField, pages)

	if err != nil {
		return pages, err
	}

	return results, nil
}

func (s *OperationSectionServiceImpl) GetOperationSectionDescription(groupCode string, sectionCode string) (masteroperationpayloads.OperationSectionDescriptionResponse, error) {
	payloads, err := s.operationSectionRepo.GetOperationSectionDescription(groupCode, sectionCode)

	if err != nil {
		return masteroperationpayloads.OperationSectionDescriptionResponse{}, err
	}

	return payloads, nil
}

func (s *OperationSectionServiceImpl) SaveOperationSection(req masteroperationpayloads.OperationSectionRequest) (bool, error) {

	save, err := s.operationSectionRepo.SaveOperationSection(req)
	if err != nil {
		return false, err
	}
	return save, nil
}

func (s *OperationSectionServiceImpl) GetOperationSectionById(id int) (masteroperationpayloads.OperationSectionResponse, error) {
	value, err := s.operationSectionRepo.GetOperationSectionById(id)

	if err != nil {
		return masteroperationpayloads.OperationSectionResponse{}, err
	}
	return value, nil
}

// func (s *OperationSectionServiceImpl) GetAllOperationSectionList(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) ([]masterpayloads.OperationSectionListResponse, error) {
// 	results, err := s.operationSectionRepo.GetAllOperationSectionList(queryCriteria ,  sortField , pages )
// 	var responses []masterpayloads.OperationSectionListResponse

// 	if err!= nil {
// 		return responses, err
// 	}

// 	for _,value := range results{
// 		response := masterpayloads.OperationSectionListResponse{
// 			IsActive: value.IsActive,
// 			OperationSectionId: value.OperationSectionId,
// 			OperationSectionCode: value.OperationSectionCode,
// 			OperationSectionDescription: value.OperationSectionDescription,
// 			OperationGroupId: value.OperationGroupId,
// 			OperationGroupCode: value.OperationGroupCode,
// 			OperationGroupDescription: value.OperationGroupDescription,
// 		}
// 		responses = append(responses,response)
// 	}
// 	return responses,nil
// }

func (s *OperationSectionServiceImpl) GetAllOperationSection() ([]masteroperationpayloads.OperationSectionResponse, error) {
	results, err := s.operationSectionRepo.GetAllOperationSection()
	var responses []masteroperationpayloads.OperationSectionResponse

	if err != nil {
		log.Fatal(err)
	}

	if len(results) == 0 {
		return responses, gorm.ErrRecordNotFound
	}

	for _, value := range results {
		response := masteroperationpayloads.OperationSectionResponse{
			IsActive:                    value.IsActive,
			OperationSectionId:          value.OperationSectionId,
			OperationSectionCode:        value.OperationSectionCode,
			OperationGroupId:            value.OperationGroupId,
			OperationSectionDescription: value.OperationSectionDescription,
		}
		responses = append(responses, response)
	}
	return responses, nil
}

func (r *OperationSectionServiceImpl) ChangeStatusOperationSection(Id int) (bool, error) {
	updates, err := r.operationSectionRepo.ChangeStatusOperationSection(Id)
	if err != nil {
		return false, err
	}
	return updates, nil
}
