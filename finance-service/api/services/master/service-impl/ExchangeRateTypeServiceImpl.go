package masterserviceimpl

import (
	masterentities "finance/api/entities/master"
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"
	masterrepo "finance/api/repositories/master"
	masterservice "finance/api/services/master"

	"gorm.io/gorm"
)

type ExchangeRateTypeServiceImpl struct {
	structExchangeRateTypeRepo masterrepo.ExchangeRateTypeRepository
}

func OpenExchangeRateTypeService(exchangeratetyperepo masterrepo.ExchangeRateTypeRepository) masterservice.ExchangeRateTypeService {
	return &ExchangeRateTypeServiceImpl{
		structExchangeRateTypeRepo: exchangeratetyperepo,
	}
}

func (s *ExchangeRateTypeServiceImpl) WithTrx(Trxhandle *gorm.DB) masterservice.ExchangeRateTypeService {
	s.structExchangeRateTypeRepo = s.structExchangeRateTypeRepo.WithTrx(Trxhandle)
	return s
}

func (s *ExchangeRateTypeServiceImpl) Save(request masterpayloads.SaveExchangeRateTypeRequest) (bool, error) {
	save, err := s.structExchangeRateTypeRepo.Save(request)

	if err != nil {
		return false, err
	}

	return save, nil
}

func (s *ExchangeRateTypeServiceImpl) ChangeStatus(exchangeRateTypeId int) (bool, error) {
	save, err := s.structExchangeRateTypeRepo.ChangeStatus(exchangeRateTypeId)

	if err != nil {
		return false, err
	}

	return save, nil
}

func (s *ExchangeRateTypeServiceImpl) GetAll(request masterpayloads.GetAllExchangeRateTypeRequest, pages pagination.Pagination) (pagination.Pagination, error) {
	get, err := s.structExchangeRateTypeRepo.GetAll(request, pages)

	if err != nil {
		return pagination.Pagination{}, err
	}

	return get, nil
}

func (s *ExchangeRateTypeServiceImpl) GetById(exchangeRateTypeId int) (masterentities.ExchangeRateType, error) {
	get, err := s.structExchangeRateTypeRepo.GetById(exchangeRateTypeId)

	if err != nil {
		return masterentities.ExchangeRateType{}, err
	}

	return get, nil
}

func (s *ExchangeRateTypeServiceImpl) GetByName(exchangeRateType string) (masterentities.ExchangeRateType, error) {
	get, err := s.structExchangeRateTypeRepo.GetByName(exchangeRateType)

	if err != nil {
		return masterentities.ExchangeRateType{}, err
	}

	return get, nil
}
