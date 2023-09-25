package masterentities

const TableNameBank = "mtr_bank"

type Bank struct {
	IsActive     *bool        `gorm:"column:is_active;default:true;not null" json:"is_active"`
	BankId       int          `gorm:"column:bank_id;primaryKey;size:30;not null" json:"bank_id"`
	BankCode     string       `gorm:"column:bank_code;unique;size:5;not null" json:"bank_code"`
	BankName     string       `gorm:"column:bank_name;size:100;null" json:"bank_name"`
	BankAbbr     string       `gorm:"column:bank_abbr;size:100;null" json:"bank_abbr"`
	BankBranches []BankBranch `gorm:"foreignKey:BankId;references:bank_id" json:"mtr_bank_branches"`
}

func (*Bank) TableName() string {
	return TableNameBank
}
