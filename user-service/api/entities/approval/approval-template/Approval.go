package approvalentities

const TableNameApproval = "approval"

// Approval mapped from table <Approval>
type Approval struct {
	IsActive        bool            `gorm:"column:is_active;not null" json:"is_active"`
	ApprovalId      int             `gorm:"size:30;column:approval_id;primaryKey;autoIncrement" json:"approval_id"`
	ApprovalCode    string          `gorm:"size:30;column:approval_code" json:"approval_code"`
	ApprovalName    string          `gorm:"size:100;column:approval_name" json:"approval_name"`
	ModuleId        int             `gorm:"size:30;column:module_id" json:"module_id"`
	DocumentTypeId  int             `gorm:"size:30;column:document_type_id" json:"document_type_id"`
	ApprovalMapping ApprovalMapping `gorm:"foreignKey:ApprovalId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:approval_id"`
	ApprovalAmount  ApprovalAmount  `gorm:"foreignKey:ApprovalId;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:approval_id"`
}

// custom tablename
func (e *Approval) TableName() string {
	return TableNameApproval
}
