package approvalentities

const TableNameApprovalAmount = "approval_amount"

// ApprovalAmount mapped from table <ApprovalAmount>
type ApprovalAmount struct {
	IsActive         bool    `gorm:"column:is_active;not null" json:"is_active"`
	ApprovalAmountId int     `gorm:"size:30;column:approval_amount_id;primaryKey;autoIncrement" json:"approval_amount_id"`
	ApprovalId       int     `gorm:"size:30;column:approval_id;index:idx_approval_amount;unique" json:"approval_id"`
	MaxAmount        float64 `gorm:"column:max_amount;index:idx_approval_amount;unique" json:"max_amount"`
}

// custom tablename
func (e *ApprovalAmount) TableName() string {
	return TableNameApprovalAmount
}
