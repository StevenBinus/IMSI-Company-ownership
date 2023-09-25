package masterservice

import (
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"

	"gorm.io/gorm"
)

type BankBranchService interface {
	WithTrx(Trxhandle *gorm.DB) BankBranchService
	GetAllBankBranch(request masterpayloads.GetBankBranchRequests, pages pagination.Pagination) (pagination.Pagination, error)
	GetBankBranchByID(id int) (masterpayloads.SaveBankBranchResponses, error)
	GetBankBranchByBankID(id int) ([]masterpayloads.SaveBankBranchResponses, error)
	Save(masterpayloads.SaveBankBranchRequests) (bool, error)
	ChangeStatus(request masterpayloads.ChangeStatusBankBranchRequests) (bool, error)
}
