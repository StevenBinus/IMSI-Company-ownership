package masterrepo

import (
	masterentities "finance/api/entities/master"
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"

	"gorm.io/gorm"
)

type BankRepository interface {
	WithTrx(Trxhandle *gorm.DB) BankRepository
	GetAllBank(request masterpayloads.GetBankRequests, pages pagination.Pagination) (pagination.Pagination, error)
	GetBankByID(id int) (masterentities.Bank, error)
	Save(masterpayloads.SaveBankRequests) (bool, error)
	ChangeStatus(request masterpayloads.ChangeStatusBankRequests) (bool, error)
}
