package approverentities

const TableNameApproverDetails = "approver_details"

// Approver Detail mapped from table <approver detail>
type ApproverDetails struct {
	IsActive         bool `gorm:"column:is_active;not null" json:"is_active"`
	ApproverDetailId int  `gorm:"size:30;column:approver_detail_id;primaryKey;autoIncrement" json:"approver_detail_id"`
	ApproverId       int  `gorm:"size:30;column:approver_id;index:idx_approver_details,unique" json:"approver_id"`
	UserId           int  `gorm:"size:30;column:user_id;index:idx_approver_details,unique" json:"user_id"`
}

// custom tablename
func (e *ApproverDetails) TableName() string {
	return TableNameApproverDetails
}
