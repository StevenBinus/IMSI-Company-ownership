package accountreceivablerepo

import (
	accountreceivableentities "finance/api/entities/transaction/account-receivable"
	"finance/api/payloads/pagination"
	accountreceivablepayloads "finance/api/payloads/transaction/account-receivable"

	"gorm.io/gorm"
)

type AccountReceivableUnitRepository interface {
	WithTrx(trxHandle *gorm.DB) AccountReceivableUnitRepository
	SaveHeader(accountreceivablepayloads.SaveHeaderRequest, accountreceivablepayloads.UpdateVatRequest) (bool, error)
	UpdateStatus(int, accountreceivablepayloads.UpdateStatusRequest) (bool, error)
	GetById(int) (accountreceivableentities.AccountReceivableUnit, error)
	GetAll(request accountreceivablepayloads.GetAllHeaderRequest, pages pagination.Pagination) (pagination.Pagination, error)
}
