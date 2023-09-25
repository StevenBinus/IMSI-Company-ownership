package masteroperationrepository

import (
	masteroperationentities "after-sales/api/entities/master/operation"
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	"after-sales/api/utils"

	"gorm.io/gorm"
)

type OperationGroupRepository interface {
	WithTrx(trxHandle *gorm.DB) OperationGroupRepository
	GetAllOperationGroup(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error)
	GetOperationGroupById(int) (masteroperationpayloads.OperationGroupHeader, error)
	SaveOperationGroup(masteroperationpayloads.OperationGroupHeader) (bool, error)
	ChangeStatusOperationGroup(int) (bool, error)
	GetOperationGroupByCode(string) (masteroperationpayloads.OperationGroupHeader, error)
	GetAllOperationGroupIsActive() ([]masteroperationentities.OperationGroup, error)
}
