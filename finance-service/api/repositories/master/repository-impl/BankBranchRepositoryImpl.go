package masterrepoimpl

import (
	masterentities "finance/api/entities/master"
	masterpayloads "finance/api/payloads/master"
	"finance/api/payloads/pagination"
	masterrepo "finance/api/repositories/master"
	"finance/api/utils"
	"log"

	"gorm.io/gorm"
)

type BankBranchImpl struct {
	DB *gorm.DB
}

func OpenBankBranchRepoImpl(db *gorm.DB) *BankBranchImpl {
	return &BankBranchImpl{DB: db}
}

func (r *BankBranchImpl) WithTrx(Trxhandle *gorm.DB) masterrepo.BankBranchRepository {
	if Trxhandle == nil {
		log.Println("Transaction Database Not Found")
		return r
	}
	r.DB = Trxhandle
	return r
}

func (r *BankBranchImpl) Save(request masterpayloads.SaveBankBranchRequests) (bool, error) {
	var entities masterentities.BankBranch
	entities.IsActive = utils.BoolPtr(request.IsActive)
	entities.BankBranchId = request.BankBranchId
	entities.BankId = request.BankId
	entities.BankBranchCode = request.BankBranchCode
	entities.BankBranchName = request.BankBranchName
	err := r.DB.Save(&entities)

	if err != nil {
		return false, err.Error
	}

	return true, nil
}

func (r *BankBranchImpl) GetAllBankBranch(request masterpayloads.GetBankBranchRequests, pages pagination.Pagination) (pagination.Pagination, error) {

	var bankBranchEnities []masterentities.BankBranch
	var bankBranchResponses []masterpayloads.GetBankBranchResponses

	tempRows := r.DB.
		Model(&masterentities.BankBranch{}).
		Select(
			"mtr_bank_branch.is_active",
			"mtr_bank_branch.bank_id",
			"mtr_bank_branch.bank_branch_id",
			"Bank.bank_code",
			"mtr_bank_branch.bank_branch_code",
			"mtr_bank_branch.bank_branch_name",
			"mtr_bank_branch.address_id",
		).InnerJoins("Bank").
		Where("Bank.bank_code like ?", "%"+request.BankCode+"%").
		Where("mtr_bank_branch.bank_branch_code like ?", "%"+request.BankBranchCode+"%").
		Where("mtr_bank_branch.bank_branch_name like ?", "%"+request.BankBranchName+"%")

	if request.IsActive != nil {
		tempRows = tempRows.Where("mtr_bank_branch.is_active = ?", request.IsActive)
	}
	if request.BankId != 0 {
		tempRows = tempRows.Where("mtr_bank_branch.bank_id = ?", request.BankId)
	}

	rows, err := tempRows.
		Scopes(pagination.Paginate(bankBranchEnities, &pages, tempRows)).
		Scan(&bankBranchResponses).
		Rows()

	if err != nil {
		return pages, err
	}

	defer rows.Close()

	pages.Rows = bankBranchResponses
	return pages, nil
}

func (r *BankBranchImpl) GetBankBranchByID(id int) (masterentities.BankBranch, error) {
	var result masterentities.BankBranch

	err := r.DB.Find(&result, id)
	if err != nil {
		return result, err.Error
	}

	return result, nil
}

func (r *BankBranchImpl) GetBankBranchByBankID(id int) ([]masterentities.BankBranch, error) {
	var BankBranch []masterentities.BankBranch

	rows, err := r.DB.Model(&BankBranch).Scan(&BankBranch).Where("bank_id = ?", id).Rows()
	if err != nil {
		return BankBranch, err
	}
	defer rows.Close()
	return BankBranch, nil
}

func (r *BankBranchImpl) ChangeStatus(request masterpayloads.ChangeStatusBankBranchRequests) (bool, error) {
	var bankBranch masterentities.BankBranch

	isActive := request.IsActive
	// Retrieve the bank you want to update
	r.DB.Preload("BankContacts").First(&bankBranch, request.BankBranchId)
	// Update the is_active value for the bank and its branches and contacts
	if bankBranch.BankBranchId != 0 {
		bankBranch.IsActive = &isActive
		for i := 0; i < len(bankBranch.BankContacts); i++ {
			bankBranch.BankContacts[i].IsActive = &isActive
		}
		if err := r.DB.Session(&gorm.Session{FullSaveAssociations: true}).Updates(&bankBranch).Error; err != nil {
			return false, err
		}
	}
	return true, nil
}
