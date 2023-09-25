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

type BankContactImpl struct {
	DB *gorm.DB
}

func OpenBankContactRepoImpl(db *gorm.DB) *BankContactImpl {
	return &BankContactImpl{DB: db}
}

func (r *BankContactImpl) WithTrx(Trxhandle *gorm.DB) masterrepo.BankContactRepository {
	if Trxhandle == nil {
		log.Println("Transaction Database Not Found")
		return r
	}
	r.DB = Trxhandle
	return r
}

func (r *BankContactImpl) Save(request masterpayloads.SaveBankContactRequests) (bool, error) {
	var entities masterentities.BankContact
	entities.IsActive = utils.BoolPtr(request.IsActive)
	entities.BankContactId = request.BankContactId
	entities.BankBranchId = request.BankBranchId
	entities.ContactName = request.ContactName
	entities.ContactPhone = request.ContactPhone
	entities.ContactPosition = request.ContactPosition
	err := r.DB.Save(&entities)

	if err != nil {
		return false, err.Error
	}

	return true, nil
}

func (r *BankContactImpl) GetAllBankContact(request masterpayloads.GetBankContactRequests, pages pagination.Pagination) (pagination.Pagination, error) {
	var bankContactEnities []masterentities.BankContact
	var bankContactResponses []masterpayloads.GetBankContactResponses

	tempRows := r.DB.
		Model(&masterentities.BankContact{}).
		Select(
			"is_active",
			"bank_contact_id",
			"bank_branch_id",
			"contact_name",
			"contact_position",
			"contact_phone",
		).
		Where("bank_branch_id = ?", request.BankBranchId)

	rows, err := tempRows.
		Scopes(pagination.Paginate(bankContactEnities, &pages, tempRows)).
		Scan(&bankContactResponses).
		Rows()

	if err != nil {
		return pages, err
	}

	defer rows.Close()

	pages.Rows = bankContactResponses
	return pages, nil
}

func (r *BankContactImpl) GetBankContactByID(id int) (masterentities.BankContact, error) {
	var result masterentities.BankContact

	err := r.DB.Find(&result, id)
	if err != nil {
		return result, err.Error
	}

	return result, nil
}

func (r *BankContactImpl) GetBankContactByBankBranchID(id int) ([]masterentities.BankContact, error) {
	var BankContact []masterentities.BankContact

	rows, err := r.DB.Model(&BankContact).Scan(&BankContact).Where("bank_branch_id = ?", id).Rows()
	if err != nil {
		return BankContact, err
	}
	defer rows.Close()
	return BankContact, nil
}

func (r *BankContactImpl) ChangeStatus(request masterpayloads.ChangeStatusBankContactRequests) (bool, error) {
	var bankContact masterentities.BankContact

	if err := r.DB.Model(&bankContact).
		Where(masterentities.BankContact{
			BankContactId: request.BankContactId,
		}).
		Update("is_active", request.IsActive).Error; err != nil {
		return false, err
	}

	return true, nil
}
