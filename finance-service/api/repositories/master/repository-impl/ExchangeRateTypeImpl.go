package masterrepoimpl

import (
	masterentities "finance/api/entities/master"
	masterpayloads "finance/api/payloads/master"
	pagination "finance/api/payloads/pagination"
	masterrepo "finance/api/repositories/master"

	"log"

	"gorm.io/gorm"
)

type ExchangeRateTypeImpl struct {
	DB *gorm.DB
}

func OpenExchangeRateTypeImpl(db *gorm.DB) masterrepo.ExchangeRateTypeRepository {
	return &ExchangeRateTypeImpl{DB: db}
}

func (r *ExchangeRateTypeImpl) WithTrx(Trxhandle *gorm.DB) masterrepo.ExchangeRateTypeRepository {
	if Trxhandle != nil {
		log.Println("Transaction Database Not Found")
		return r
	}
	r.DB = Trxhandle
	return r
}

func (r *ExchangeRateTypeImpl) Save(request masterpayloads.SaveExchangeRateTypeRequest) (bool, error) {

	var exchangeRateTypeEntities = masterentities.ExchangeRateType{
		IsActive:           request.IsActive,
		ExchangeRateTypeId: request.ExchangeRateTypeId,
		ExchangeRateType:   request.ExchangeRateType,
		Description:        request.Description,
	}

	rows, err := r.DB.Model(&exchangeRateTypeEntities).
		Save(&exchangeRateTypeEntities).
		Rows()

	if err != nil {
		return false, err
	}

	defer rows.Close()

	return true, nil
}

func (r *ExchangeRateTypeImpl) ChangeStatus(exchangeRateTypeId int) (bool, error) {
	var entities masterentities.ExchangeRateType

	rows, err := r.DB.Model(&entities).
		Where(masterentities.ExchangeRateType{
			ExchangeRateTypeId: exchangeRateTypeId,
		}).
		Update("is_active", gorm.Expr("1 ^ is_active")).
		Rows()

	if err != nil {
		return false, err
	}

	defer rows.Close()

	return true, nil
}

func (r *ExchangeRateTypeImpl) GetAll(request masterpayloads.GetAllExchangeRateTypeRequest, pages pagination.Pagination) (pagination.Pagination, error) {
	var entities []masterentities.ExchangeRateType
	var exchangeRateTypeHeaderResponse []masterpayloads.GetAllExchangeRateTypeHeaderResponse

	tempRows := r.DB.
		Model(&masterentities.ExchangeRateType{}).
		Select(
			"is_active",
			"exchange_rate_type_id",
			"exchange_rate_type",
			"description",
		).
		Where("exchange_rate_type like ?", "%"+request.ExchangeRateType+"%").
		Where("description like ?", "%"+request.Description+"%")

	if request.IsActive != "" {
		tempRows = tempRows.Where("is_active = ?", request.IsActive)
	}

	rows, err := tempRows.
		Scopes(pagination.Paginate(entities, &pages, tempRows)).
		Scan(&exchangeRateTypeHeaderResponse).
		Rows()

	if err != nil {
		return pages, err
	}

	defer rows.Close()

	pages.Rows = exchangeRateTypeHeaderResponse
	return pages, nil
}

func (r *ExchangeRateTypeImpl) GetById(exchangeRateTypeId int) (masterentities.ExchangeRateType, error) {
	var entities masterentities.ExchangeRateType

	rows, err := r.DB.Model(&entities).
		Where(masterentities.ExchangeRateType{
			ExchangeRateTypeId: exchangeRateTypeId,
		}).
		Find(&entities).
		Scan(&entities).
		Rows()

	if err != nil {
		return entities, err
	}

	defer rows.Close()

	return entities, nil
}

func (r *ExchangeRateTypeImpl) GetByName(exchangeRateType string) (masterentities.ExchangeRateType, error) {
	var entities masterentities.ExchangeRateType

	rows, err := r.DB.Model(&entities).
		Where(masterentities.ExchangeRateType{
			ExchangeRateType: exchangeRateType,
		}).
		Find(&entities).
		Scan(&entities).
		Rows()

	if err != nil {
		return entities, err
	}

	defer rows.Close()

	return entities, nil
}
