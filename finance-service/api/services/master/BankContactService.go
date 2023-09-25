package masterservice

import (
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"

	"gorm.io/gorm"
)

type BankContactService interface {
	WithTrx(Trxhandle *gorm.DB) BankContactService
	GetAllBankContact(request masterpayloads.GetBankContactRequests, pages pagination.Pagination) (pagination.Pagination, error)
	GetBankContactByID(id int) (masterpayloads.SaveBankContactResponses, error)
	GetBankContactByBankBranchID(id int) ([]masterpayloads.SaveBankContactResponses, error)
	Save(masterpayloads.SaveBankContactRequests) (bool, error)
	ChangeStatus(request masterpayloads.ChangeStatusBankContactRequests) (bool, error)
}
