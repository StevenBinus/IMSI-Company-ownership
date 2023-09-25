package masterentities

const TableNameBankContact = "mtr_bank_contact"

type BankContact struct {
	IsActive        *bool  `gorm:"column:is_active;not null;default:true" json:"is_active"`
	BankContactId   int    `gorm:"column:bank_contact_id;size:30;primaryKey;not null" json:"bank_contact_id"`
	BankBranchId    int    `gorm:"column:bank_branch_id;size:30;not null" json:"bank_branch_id"`
	ContactName     string `gorm:"column:contact_name;size:100;not null" json:"contact_name"`
	ContactPosition string `gorm:"column:contact_position;size:100;null" json:"contact_posiion"`
	ContactPhone    string `gorm:"column:contact_phone;size:100;null" json:"contact_phone"`
}

func (*BankContact) TableName() string {
	return TableNameBankContact
}
