package approverentities

const TableNameApprover = "approver"

// Approver mapped from table <approver>
type Approver struct {
	IsActive     bool            `gorm:"column:is_active;not null" json:"is_active"`
	CompanyId    int             `gorm:"column:company_id;not null" json:"company_id"`
	ApproverId   int             `gorm:"size:30;column:approver_id;primaryKey;autoIncrement" json:"approver_id"`
	ApproverCode string          `gorm:"size:30;column:approver_code" json:"approver_code"`
	Approver     ApproverDetails `gorm:"foreignKey:ApproverId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:approver_id"`
}

// custom tablename
func (e *Approver) TableName() string {
	return TableNameApprover
}
