package masterservice

import (
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"

	"gorm.io/gorm"
)

type BankService interface {
	WithTrx(Trxhandle *gorm.DB) BankService
	GetAllBank(request masterpayloads.GetBankRequests, pages pagination.Pagination) (pagination.Pagination, error)
	GetBankByID(id int) (masterpayloads.GetBankResponses, error)
	Save(masterpayloads.SaveBankRequests) (bool, error)
	ChangeStatus(request masterpayloads.ChangeStatusBankRequests) (bool, error)
}
