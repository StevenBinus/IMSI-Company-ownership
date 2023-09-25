package masterserviceimpl

import (
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"
	masterrepo "finance/api/repositories/master"
	masterservice "finance/api/services/master"

	"gorm.io/gorm"
)

type BankContactServiceImpl struct {
	structBankContactRepo masterrepo.BankContactRepository
}

func OpenBankContactService(BankContactrepo masterrepo.BankContactRepository) masterservice.BankContactService {
	return &BankContactServiceImpl{
		structBankContactRepo: BankContactrepo,
	}
}

func (s *BankContactServiceImpl) WithTrx(Trxhandle *gorm.DB) masterservice.BankContactService {
	s.structBankContactRepo = s.structBankContactRepo.WithTrx(Trxhandle)
	return s
}

func (s *BankContactServiceImpl) Save(request masterpayloads.SaveBankContactRequests) (bool, error) {
	save, err := s.structBankContactRepo.Save(request)

	if err != nil {
		return false, err
	}

	return save, nil
}

func (s *BankContactServiceImpl) GetAllBankContact(request masterpayloads.GetBankContactRequests, pages pagination.Pagination) (pagination.Pagination, error) {
	get, err := s.structBankContactRepo.GetAllBankContact(request, pages)

	if err != nil {
		return pagination.Pagination{}, err
	}

	return get, nil
}

func (s *BankContactServiceImpl) GetBankContactByID(id int) (masterpayloads.SaveBankContactResponses, error) {
	value, err := s.structBankContactRepo.GetBankContactByID(id)

	if err != nil {
		return masterpayloads.SaveBankContactResponses{}, err
	}

	response := masterpayloads.SaveBankContactResponses{
		IsActive:        *value.IsActive,
		BankContactId:   value.BankContactId,
		BankBranchId:    value.BankBranchId,
		ContactName:     value.ContactName,
		ContactPhone:    value.ContactPhone,
		ContactPosition: value.ContactPosition,
	}

	return response, nil
}

func (s *BankContactServiceImpl) GetBankContactByBankBranchID(id int) ([]masterpayloads.SaveBankContactResponses, error) {
	rows, err := s.structBankContactRepo.GetBankContactByBankBranchID(id)
	var responses []masterpayloads.SaveBankContactResponses

	if err != nil {
		return []masterpayloads.SaveBankContactResponses{}, err
	}

	for _, value := range rows {
		response := masterpayloads.SaveBankContactResponses{
			IsActive:        *value.IsActive,
			BankContactId:   value.BankContactId,
			BankBranchId:    value.BankBranchId,
			ContactName:     value.ContactName,
			ContactPhone:    value.ContactPhone,
			ContactPosition: value.ContactPosition,
		}
		responses = append(responses, response)
	}
	return responses, nil
}

func (s *BankContactServiceImpl) ChangeStatus(request masterpayloads.ChangeStatusBankContactRequests) (bool, error) {
	save, err := s.structBankContactRepo.ChangeStatus(request)

	if err != nil {
		return false, err
	}

	return save, nil
}
