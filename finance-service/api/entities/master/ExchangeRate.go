package masterentities

import "time"

const TableNameExchangeRate = "mtr_exchange_rate"

type ExchangeRate struct {
	IsActive             bool      `gorm:"column:is_active;default:true;not null" json:"is_active"`
	ExchangeRateId       int       `gorm:"column:exchange_rate_id;not null;primaryKey" json:"exchange_rate_id"`
	ExchangeRateTypeId   int       `gorm:"column:exchange_rate_type_id;not null" json:"exchange_rate_type_id"`
	CurrencyID           int       `gorm:"column:currency_id;not null" json:"currency_id"`
	EffectiveDate        time.Time `gorm:"column:effective_date;not null" json:"effective_date"`
	CurrencyExchangeRate float64   `gorm:"column:currency_exchange_rate;not null" json:"currency_exchange_rate"`
}

func (*ExchangeRate) TableName() string {
	return TableNameExchangeRate
}