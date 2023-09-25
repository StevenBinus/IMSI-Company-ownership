package masteroperationservice

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	"after-sales/api/utils"
	// "after-sales/api/utils"
)

type OperationSectionService interface {
	GetAllOperationSection() ([]masteroperationpayloads.OperationSectionResponse, error)
	GetAllOperationSectionList(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error)
	SaveOperationSection(masteroperationpayloads.OperationSectionRequest) (bool, error)
	GetOperationSectionDescription(string, string) (masteroperationpayloads.OperationSectionDescriptionResponse, error)
	GetOperationSectionById(int) (masteroperationpayloads.OperationSectionResponse, error)
	ChangeStatusOperationSection(int) (bool, error)
}
