package entities

import (
	"time"
)

const TableNameUserDetail = "user_details"

// UserDetail mapped from table <user_details>
type UserDetail struct {
	IsActive        bool      `gorm:"column:is_active;not null" json:"is_active"`
	UserId          int       `gorm:"size:30;column:user_id;not null;unique" json:"user_id"`
	UserName        string    `gorm:"column:user_name;size:100;not null" json:"user_name"`
	UserNickname    string    `gorm:"column:user_nickname;size:10;default:NULL" json:"user_nickname"`
	CompanyID       int       `gorm:"size:30;column:company_id;not null" json:"company_id"`
	JobTitleID      uint16    `gorm:"column:job_title_id;not null" json:"job_title_id"`
	JobPositionID   uint16    `gorm:"column:job_position_id;not null" json:"job_position_id"`
	SkillLevelID    uint16    `gorm:"column:skill_level_id" json:"skill_level_id"`
	FactorX         uint8     `gorm:"column:factor_x;default:0" json:"factor_x"`
	DivisionID      uint16    `gorm:"column:division_id;not null" json:"division_id"`
	CostCenterID    uint16    `gorm:"column:cost_center_id;not null" json:"cost_center_id"`
	ProfitCenterID  uint16    `gorm:"column:profit_center_id;not null" json:"profit_center_id"`
	OfficePhoneNo   string    `gorm:"column:office_phone_no;size:13;default:NULL" json:"office_phone_no"`
	AddressID       int       `gorm:"size:30;column:address_id;not null" json:"address_id"`
	HomePhoneNo     string    `gorm:"column:home_phone_no;size:13;default:NULL" json:"home_phone_no"`
	MobilePhone     string    `gorm:"column:mobile_phone;size:13;default:NULL" json:"mobile_phone"`
	EmailAddress    string    `gorm:"column:email_address;size:100;not null" json:"email_address"`
	StartDate       time.Time `gorm:"column:start_date;default:NULL" json:"start_date"`
	TerminationDate time.Time `gorm:"column:termination_date;default:NULL" json:"termination_date"`
	Gender          string    `gorm:"column:gender;size:10;not null" json:"gender"`
	DateOfBirth     time.Time `gorm:"column:date_of_birth;not null" json:"date_of_birth"`
	CityOfBirth     int       `gorm:"size:30;column:city_of_birth;not null" json:"city_of_birth"`
	MaritalStatus   string    `gorm:"column:marital_status;size:30;not null" json:"marital_status"`
	NoOfChildren    uint8     `gorm:"column:no_of_children" json:"no_of_children"`
	IDType          string    `gorm:"column:id_type;size:30;default:NULL" json:"id_type"`
	IDNo            string    `gorm:"column:id_no;size:30;default:NULL" json:"id_no"`
	Citizenship     string    `gorm:"column:citizenship;size:30;default:NULL" json:"citizenship"`
	LastEducation   string    `gorm:"column:last_education;size:10;default:NULL" json:"last_education"`
	LastEmployment  string    `gorm:"column:last_employment;size:100;default:NULL" json:"last_employment"`
	BankID          int       `gorm:"size:30;column:bank_id;not null" json:"bank_id"`
	BankAccountId   int       `gorm:"size:30;column:bank_account_id;default:NULL" json:"bank_account_id"`
	CurrencyID      uint16    `gorm:"column:currency_id;not null" json:"currency_id"`
}

// TableName UserDetail's table name
func (*UserDetail) TableName() string {
	return TableNameUserDetail
}
