package masterentities

const TableNameBankBranch = "mtr_bank_branch"

type BankBranch struct {
	IsActive       *bool         `gorm:"column:is_active;not null;default:true" json:"is_active"`
	BankBranchId   int           `gorm:"column:bank_branch_id;primaryKey;size:30;not null" json:"bank_branch_id"`
	BankId         int           `gorm:"column:bank_id;index:idx_bank_branch,unique;size:30;not null" json:"bank_id"`
	BankBranchCode string        `gorm:"column:bank_branch_code;index:idx_bank_branch,unique;size:10;not null" json:"bank_branch_code"`
	BankBranchName string        `gorm:"column:bank_branch_name;size:100;null" json:"bank_name"`
	AddressId      int           `gorm:"column:address_id;size:30;not null" json:"address_id"`
	Bank           Bank          `gorm:"references:BankId" json:"mtr_bank"`
	BankContacts   []BankContact `gorm:"foreignKey:BankBranchId;references:bank_branch_id" json:"mtr_bank_contacts"`
}

func (*BankBranch) TableName() string {
	return TableNameBankBranch
}
