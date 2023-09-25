package masterentities

const TableNameExchangeRateType = "mtr_exchange_rate_type"

type ExchangeRateType struct {
	IsActive           bool           `gorm:"column:is_active;default:true;not null" json:"is_active"`
	ExchangeRateTypeId int            `gorm:"column:exchange_rate_type_id;not null;primaryKey" json:"exchange_rate_type_id"`
	ExchangeRateType   string         `gorm:"column:exchange_rate_type;not null;type:varchar(10);index:idx_exchange_rate_type,unique" json:"exchange_rate_type"`
	Description        string         `gorm:"column:description;not null;type:varchar(35)" json:"description"`
	ExchangeRate       []ExchangeRate `gorm:"foreignKey:ExchangeRateTypeId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:exchange_rate_type_id" json:"exchange_rate_types"`
}

func (*ExchangeRateType) TableName() string {
	return TableNameExchangeRateType
}
