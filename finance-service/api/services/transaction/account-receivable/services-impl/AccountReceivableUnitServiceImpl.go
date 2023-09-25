package accountreceivableserviceimpl

import (
	accountreceivableentities "finance/api/entities/transaction/account-receivable"
	"finance/api/payloads/pagination"
	accountreceivablepayloads "finance/api/payloads/transaction/account-receivable"
	accountreceivablerepo "finance/api/repositories/transaction/account-receivable"
	accountreceivableservice "finance/api/services/transaction/account-receivable"

	"gorm.io/gorm"
)

type AccountReceivableUnitServiceImpl struct {
	accountReceivableUnitRepo accountreceivablerepo.AccountReceivableUnitRepository
}

func OpenAccountReceivableUnitService(accountReceivableUnitRepo accountreceivablerepo.AccountReceivableUnitRepository) accountreceivableservice.AccountReceivableUnitService {
	return &AccountReceivableUnitServiceImpl{
		accountReceivableUnitRepo: accountReceivableUnitRepo,
	}
}

func (r *AccountReceivableUnitServiceImpl) WithTrx(trxHandle *gorm.DB) accountreceivableservice.AccountReceivableUnitService {
	r.accountReceivableUnitRepo = r.accountReceivableUnitRepo.WithTrx(trxHandle)
	return r
}

func (r *AccountReceivableUnitServiceImpl) SaveHeader(request accountreceivablepayloads.SaveHeaderRequest, vatRequest accountreceivablepayloads.UpdateVatRequest) (bool, error) {
	create, err := r.accountReceivableUnitRepo.SaveHeader(request, vatRequest)

	if err != nil {
		return false, err
	}

	return create, nil
}

func (r *AccountReceivableUnitServiceImpl) UpdateStatus(invoiceUnitSystemNumber int, request accountreceivablepayloads.UpdateStatusRequest) (bool, error) {
	updates, err := r.accountReceivableUnitRepo.UpdateStatus(invoiceUnitSystemNumber, request)

	if err != nil {
		return false, err
	}

	return updates, nil
}

func (r *AccountReceivableUnitServiceImpl) GetById(invoiceUnitSystemNumber int) (accountreceivableentities.AccountReceivableUnit, error) {
	get, err := r.accountReceivableUnitRepo.GetById(invoiceUnitSystemNumber)

	if err != nil {
		return accountreceivableentities.AccountReceivableUnit{}, err
	}

	return get, nil
}

func (s *AccountReceivableUnitServiceImpl) GetAll(request accountreceivablepayloads.GetAllHeaderRequest, pages pagination.Pagination) (pagination.Pagination, error) {
	get, err := s.accountReceivableUnitRepo.GetAll(request, pages)

	if err != nil {
		return pagination.Pagination{}, err
	}

	return get, nil
}
