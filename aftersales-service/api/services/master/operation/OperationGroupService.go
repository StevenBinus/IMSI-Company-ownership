package masteroperationservice

import (
	masteroperationpayloads "after-sales/api/payloads/master/operation"
	"after-sales/api/utils"

	"gorm.io/gorm"
)

type OperationGroupService interface {
	WithTrx(trxHandle *gorm.DB) OperationGroupService
	GetAllOperationGroup(queryCriteria []utils.QueryCriteria, sortField utils.SortField, pages utils.Pagination) (utils.Pagination, error)
	GetAllOperationGroupIsActive() ([]masteroperationpayloads.OperationGroupHeader, error)
	GetOperationGroupById(int) (masteroperationpayloads.OperationGroupHeader, error)
	GetOperationGroupByCode(string) (masteroperationpayloads.OperationGroupHeader, error)
	ChangeStatusOperationGroup(int) (bool, error)
	SaveOperationGroup(masteroperationpayloads.OperationGroupHeader) (bool, error)
}
