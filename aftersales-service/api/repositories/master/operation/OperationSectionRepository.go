package masteroperationrepository

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	"after-sales/api/utils"
	// "after-sales/api/utils"
)

type OperationSectionRepository interface {
	GetAllOperationSection() ([]masteroperationentities.OperationSection, error)
	GetOperationSectionById(int) (masteroperationpayloads.OperationSectionResponse, error)
	GetOperationSectionDescription(string, string) (masteroperationpayloads.OperationSectionDescriptionResponse, error)
	GetAllOperationSectionList(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error)
	SaveOperationSection(masteroperationpayloads.OperationSectionRequest) (bool, error)
	ChangeStatusOperationSection(int) (bool, error)
}
