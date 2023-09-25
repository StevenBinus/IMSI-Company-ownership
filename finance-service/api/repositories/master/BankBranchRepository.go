package masterrepo

import (
	masterentities "finance/api/entities/master"
	masterpayloads "finance/api/payloads/master"
	"finance/api/payloads/pagination"

	"gorm.io/gorm"
)

type BankBranchRepository interface {
	WithTrx(Trxhandle *gorm.DB) BankBranchRepository
	GetAllBankBranch(request masterpayloads.GetBankBranchRequests, pages pagination.Pagination) (pagination.Pagination, error)
	GetBankBranchByID(id int) (masterentities.BankBranch, error)
	GetBankBranchByBankID(id int) ([]masterentities.BankBranch, error)
	Save(masterpayloads.SaveBankBranchRequests) (bool, error)
	ChangeStatus(request masterpayloads.ChangeStatusBankBranchRequests) (bool, error)
}
