package masterserviceimpl

import (
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"
	masterrepo "finance/api/repositories/master"
	masterservice "finance/api/services/master"

	"gorm.io/gorm"
)

type BankServiceImpl struct {
	structBankRepo masterrepo.BankRepository
	// structBankBranchRepo masterrepo.BankBranchRepository
}

func OpenBankService(bankRepo masterrepo.BankRepository) masterservice.BankService {
	return &BankServiceImpl{
		structBankRepo: bankRepo,
		// structBankBranchRepo: bankBranchRepo,
	}
}

func (s *BankServiceImpl) WithTrx(Trxhandle *gorm.DB) masterservice.BankService {
	s.structBankRepo = s.structBankRepo.WithTrx(Trxhandle)
	// s.structBankBranchRepo = s.structBankBranchRepo.WithTrx(Trxhandle)
	return s
}

func (s *BankServiceImpl) Save(request masterpayloads.SaveBankRequests) (bool, error) {
	save, err := s.structBankRepo.Save(request)

	if err != nil {
		return false, err
	}

	return save, nil
}

func (s *BankServiceImpl) GetAllBank(request masterpayloads.GetBankRequests, pages pagination.Pagination) (pagination.Pagination, error) {
	get, err := s.structBankRepo.GetAllBank(request, pages)

	if err != nil {
		return pagination.Pagination{}, err
	}

	return get, nil
}

func (s *BankServiceImpl) GetBankByID(id int) (masterpayloads.GetBankResponses, error) {
	value, err := s.structBankRepo.GetBankByID(id)

	if err != nil {
		return masterpayloads.GetBankResponses{}, err
	}

	response := masterpayloads.GetBankResponses{
		IsActive: value.IsActive,
		BankId:   value.BankId,
		BankCode: value.BankCode,
		BankName: value.BankName,
		BankAbbr: value.BankAbbr,
	}

	return response, nil
}

func (s *BankServiceImpl) ChangeStatus(request masterpayloads.ChangeStatusBankRequests) (bool, error) {
	_, err := s.structBankRepo.ChangeStatus(request)

	if err != nil {
		return false, err
	}
	// _, err = s.structBankBranchRepo.ChangeStatusByBank(id, isActive)

	// if err != nil {
	// 	return false, err
	// }

	return true, nil
}
