package masterrepo

import (
	masterentities "finance/api/entities/master"
	masterpayloads "finance/api/payloads/master"
	"finance/api/payloads/pagination"

	"gorm.io/gorm"
)

type BankContactRepository interface {
	WithTrx(Trxhandle *gorm.DB) BankContactRepository
	GetAllBankContact(request masterpayloads.GetBankContactRequests, pages pagination.Pagination) (pagination.Pagination, error)
	GetBankContactByID(id int) (masterentities.BankContact, error)
	GetBankContactByBankBranchID(id int) ([]masterentities.BankContact, error)
	Save(masterpayloads.SaveBankContactRequests) (bool, error)
	ChangeStatus(request masterpayloads.ChangeStatusBankContactRequests) (bool, error)
}
