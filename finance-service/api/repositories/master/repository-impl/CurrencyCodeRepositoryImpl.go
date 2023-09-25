package masterrepoimpl

import (
	masterentities "finance/api/entities/master"
	currencycodepayloads "finance/api/payloads/master"
	currencycoderepo "finance/api/repositories/master"

	"log"

	"gorm.io/gorm"
)

type CurrencyCodeImpl struct {
	myDB *gorm.DB
}

func (r *CurrencyCodeImpl) WithTrx(Trxhandle *gorm.DB) currencycoderepo.CurrencyCodeRepository {
	if Trxhandle != nil {
		log.Println("Transaction Database Not Found")
		return r
	}
	r.myDB = Trxhandle
	return r
}

func StartCurrencyCodeRepoImpl(db *gorm.DB) *CurrencyCodeImpl {
	return &CurrencyCodeImpl{myDB: db}
}

func (r *CurrencyCodeImpl) GetAllCurrencyCodes() ([]masterentities.MtrCurrency, error) {
	var CurrencyCodes []masterentities.MtrCurrency

	err := r.myDB.Find(&CurrencyCodes)
	if err != nil {
		log.Fatal(err)
	}

	return CurrencyCodes, nil
}

func (r *CurrencyCodeImpl) GetCurrencyCodeByID(id int) (masterentities.MtrCurrency, error) {
	var result masterentities.MtrCurrency

	err := r.myDB.Find(&result, id)
	if err != nil {
		log.Fatal(err)
	}

	return result, nil
}

func (r *CurrencyCodeImpl) CreateCurrencyCode(req currencycodepayloads.CurrencyCodeRequest) (bool, error) {
	var data_inp masterentities.MtrCurrency
	data_inp.CurrencyCode = req.CurrencyCode
	data_inp.CurrencyName = req.Description
	data_inp.CompBankFormatType = req.CompanyBankFormatType

	err := r.myDB.Create(&data_inp)
	if err != nil {
		log.Fatal((err))
	}

	return true, nil
}

func (r *CurrencyCodeImpl) UpdateCurrencyCode(inp_data masterentities.MtrCurrency) (bool, error) {
	check, _ := r.GetCurrencyCodeByID(inp_data.CurrencyID)

	check.CurrencyCode = inp_data.CurrencyCode
	check.CurrencyName = inp_data.CurrencyName
	check.CompBankFormatType = inp_data.CompBankFormatType

	err := r.myDB.Save(&check)
	if err != nil {
		log.Fatal(err)
	}

	return true, nil
}

func (r *CurrencyCodeImpl) PatchStatusCurrencyCode(id int) bool {
	var check_status masterentities.MtrCurrency
	current_status := check_status.IsActive
	new_status := !current_status
	return new_status

}
