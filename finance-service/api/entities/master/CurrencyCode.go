package masterentities

const TableNameMaster = "mtr_currency_code"

type MtrCurrency struct {
	IsActive           bool           `gorm:"column:is_active;default:true;not null" json:"is_active"`
	CurrencyID         int            `gorm:"column:currency_id;primaryKey;not null" json:"currency_id"`
	CurrencyCode       string         `gorm:"column:currency_code;index:idx_currency_code,unique;type:char(3);not null" json:"currency_code"`
	CurrencyName       string         `gorm:"column:currency_name;type:varchar(35);not null" json:"currency_name"`
	CompBankFormatType int            `gorm:"column:comp_bank_format_type;not null" json:"comp_bank_format_type"`
	ExchangeRate       []ExchangeRate `gorm:"foreignKey:CurrencyID;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:currency_id" json:"exchange_rate_types"`
}

func (*MtrCurrency) TableName() string {
	return TableNameMaster
}
