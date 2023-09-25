package masterserviceimpl

import (
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"
	masterrepo "finance/api/repositories/master"
	masterservice "finance/api/services/master"

	"gorm.io/gorm"
)

type BankBranchServiceImpl struct {
	structBankBranchRepo masterrepo.BankBranchRepository
}

func OpenBankBranchService(bankBranchrepo masterrepo.BankBranchRepository) masterservice.BankBranchService {
	return &BankBranchServiceImpl{
		structBankBranchRepo: bankBranchrepo,
	}
}

func (s *BankBranchServiceImpl) WithTrx(Trxhandle *gorm.DB) masterservice.BankBranchService {
	s.structBankBranchRepo = s.structBankBranchRepo.WithTrx(Trxhandle)
	return s
}

func (s *BankBranchServiceImpl) Save(request masterpayloads.SaveBankBranchRequests) (bool, error) {
	save, err := s.structBankBranchRepo.Save(request)

	if err != nil {
		return false, err
	}

	return save, nil
}

func (s *BankBranchServiceImpl) GetAllBankBranch(request masterpayloads.GetBankBranchRequests, pages pagination.Pagination) (pagination.Pagination, error) {
	get, err := s.structBankBranchRepo.GetAllBankBranch(request, pages)

	if err != nil {
		return pagination.Pagination{}, err
	}

	return get, nil
}

func (s *BankBranchServiceImpl) GetBankBranchByID(id int) (masterpayloads.SaveBankBranchResponses, error) {
	value, err := s.structBankBranchRepo.GetBankBranchByID(id)

	if err != nil {
		return masterpayloads.SaveBankBranchResponses{}, err
	}

	response := masterpayloads.SaveBankBranchResponses{
		IsActive:       *value.IsActive,
		BankBranchId:   value.BankBranchId,
		BankId:         value.BankId,
		BankBranchCode: value.BankBranchCode,
		BankBranchName: value.BankBranchName,
		AddressId:      value.AddressId,
	}

	return response, nil
}

func (s *BankBranchServiceImpl) GetBankBranchByBankID(id int) ([]masterpayloads.SaveBankBranchResponses, error) {
	rows, err := s.structBankBranchRepo.GetBankBranchByBankID(id)
	var responses []masterpayloads.SaveBankBranchResponses

	if err != nil {
		return []masterpayloads.SaveBankBranchResponses{}, err
	}

	for _, value := range rows {
		response := masterpayloads.SaveBankBranchResponses{
			IsActive:       *value.IsActive,
			BankBranchId:   value.BankBranchId,
			BankId:         value.BankId,
			BankBranchCode: value.BankBranchCode,
			BankBranchName: value.BankBranchName,
			AddressId:      value.AddressId,
		}
		responses = append(responses, response)
	}
	return responses, nil
}

func (s *BankBranchServiceImpl) ChangeStatus(request masterpayloads.ChangeStatusBankBranchRequests) (bool, error) {
	save, err := s.structBankBranchRepo.ChangeStatus(request)

	if err != nil {
		return false, err
	}

	return save, nil
}
