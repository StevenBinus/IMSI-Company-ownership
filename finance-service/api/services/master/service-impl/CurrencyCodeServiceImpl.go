package masterserviceimpl

import (
	masterentities "finance/api/entities/master"
	currencycodepayloads "finance/api/payloads/master"
	currencycoderepo "finance/api/repositories/master"
	currencycodeservice "finance/api/services/master"
	"log"

	"gorm.io/gorm"
)

type CurrencyCodeServiceImpl struct {
	currencycodemasterrepo currencycoderepo.CurrencyCodeRepository
}

func StartCurrencyCodeService(currencycoderepo currencycoderepo.CurrencyCodeRepository) currencycodeservice.CurrencyCodeService {
	return &CurrencyCodeServiceImpl{
		currencycodemasterrepo: currencycoderepo,
	}
}

func (s *CurrencyCodeServiceImpl) WithTrx(Trxhandle *gorm.DB) currencycodeservice.CurrencyCodeService {
	s.currencycodemasterrepo = s.currencycodemasterrepo.WithTrx(Trxhandle)
	return s
}

func (s *CurrencyCodeServiceImpl) GetAllCurrencyCodes() ([]currencycodepayloads.CurrencyCodeResponses, error) {
	results, err := s.currencycodemasterrepo.GetAllCurrencyCodes()
	var responses []currencycodepayloads.CurrencyCodeResponses

	if err != nil {
		log.Fatal(err)
	}

	for _, value := range results {
		response := currencycodepayloads.CurrencyCodeResponses{
			IsActive:           value.IsActive,
			CurrencyID:         value.CurrencyID,
			CurrencyCode:       value.CurrencyCode,
			CurrencyName:       value.CurrencyName,
			CompBankFormatType: value.CompBankFormatType,
		}
		responses = append(responses, response)
	}
	return responses, nil
}

func (s *CurrencyCodeServiceImpl) GetCurrencyCodeByID(id int) (currencycodepayloads.CurrencyCodeResponses, error) {
	value, err := s.currencycodemasterrepo.GetCurrencyCodeByID(id)

	if err != nil {
		log.Fatal(err)
	}

	response := currencycodepayloads.CurrencyCodeResponses{
		IsActive:           value.IsActive,
		CurrencyID:         value.CurrencyID,
		CurrencyCode:       value.CurrencyCode,
		CurrencyName:       value.CurrencyName,
		CompBankFormatType: value.CompBankFormatType,
	}

	return response, nil
}

func (s *CurrencyCodeServiceImpl) CreateCurrencyCode(req currencycodepayloads.CurrencyCodeRequest) (bool, error) {
	add_data := req
	created_status, err := s.currencycodemasterrepo.CreateCurrencyCode(add_data)
	if err != nil {
		return false, err
	}
	return created_status, nil
}

func (s *CurrencyCodeServiceImpl) UpdateCurrencyCode(upd masterentities.MtrCurrency) (bool, error) {
	updated_status, err := s.currencycodemasterrepo.UpdateCurrencyCode(upd)
	if err != nil {
		return false, err
	}
	return updated_status, nil
}
