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

type BankImpl struct {
	DB *gorm.DB
}

func OpenBankRepoImpl(db *gorm.DB) *BankImpl {
	return &BankImpl{DB: db}
}

func (r *BankImpl) WithTrx(Trxhandle *gorm.DB) masterrepo.BankRepository {
	if Trxhandle == nil {
		log.Println("Transaction Database Not Found")
		return r
	}

	r.DB = Trxhandle
	return r
}

func (r *BankImpl) Save(request masterpayloads.SaveBankRequests) (bool, error) {
	var entities masterentities.Bank
	entities.IsActive = utils.BoolPtr(request.IsActive)
	entities.BankId = request.BankId
	entities.BankCode = request.BankCode
	entities.BankName = request.BankName
	entities.BankAbbr = request.BankAbbr
	err := r.DB.Save(&entities)

	if err.Error != nil {
		return false, err.Error
	}

	return true, nil
}

func (r *BankImpl) GetAllBank(request masterpayloads.GetBankRequests, pages pagination.Pagination) (pagination.Pagination, error) {
	var bankEnities []masterentities.Bank
	var bankResponses []masterpayloads.GetBankResponses

	tempRows := r.DB.
		Model(&masterentities.Bank{}).
		Select(
			"is_active",
			"bank_id",
			"bank_code",
			"bank_name",
			"bank_abbr",
		).
		Where("bank_code like ?", "%"+request.BankCode+"%").
		Where("bank_name like ?", "%"+request.BankName+"%").
		Where("bank_abbr like ?", "%"+request.BankName+"%")

	if request.IsActive != nil {
		tempRows = tempRows.Where("is_active = ?", request.IsActive)
	}

	rows, err := tempRows.
		Scopes(pagination.Paginate(bankEnities, &pages, tempRows)).
		Scan(&bankResponses).
		Rows()

	if err != nil {
		return pages, err
	}

	defer rows.Close()

	pages.Rows = bankResponses
	return pages, nil
}

func (r *BankImpl) GetBankByID(id int) (masterentities.Bank, error) {
	var result masterentities.Bank

	err := r.DB.Find(&result, id)
	if err.Error != nil {
		return result, err.Error
	}

	return result, nil
}

func (r *BankImpl) ChangeStatus(request masterpayloads.ChangeStatusBankRequests) (bool, error) {
	var bank masterentities.Bank

	isActive := request.IsActive
	// Retrieve the bank you want to update
	r.DB.Preload("BankBranches.BankContacts").First(&bank, request.BankId)
	// Update the is_active value for the bank and its branches and contacts
	if bank.BankId != 0 {
		bank.IsActive = &isActive
		for i := 0; i < len(bank.BankBranches); i++ {
			bank.BankBranches[i].IsActive = &isActive
			for j := 0; j < len(bank.BankBranches[i].BankContacts); j++ {
				bank.BankBranches[i].BankContacts[j].IsActive = &isActive
			}
		}
		if err := r.DB.Session(&gorm.Session{FullSaveAssociations: true}).Updates(&bank).Error; err != nil {
			return false, err
		}
	}

	return true, nil
}
