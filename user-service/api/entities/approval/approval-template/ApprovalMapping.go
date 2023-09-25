package approvalentities

const TableNameApprovalMapping = "approval_mapping"

// ApprovalMapping mapped from table <approval>
type ApprovalMapping struct {
	IsActive          bool `gorm:"column:is_active;not null" json:"is_active"`
	ApprovalMappingId int  `gorm:"size:30;column:approval_mapping_id;primaryKey;autoIncrement" json:"approval_mapping_id"`
	CompanyId         int  `gorm:"size:30;column:company_id;index:idx_approval_mapping,unique;not null" json:"company_id"`
	ApprovalId        int  `gorm:"size:30;column:approval_id;index:idx_approval_mapping,unique" json:"approval_id"`
	TransactionId     int  `gorm:"size:30;column:transaction_id;index:idx_approval_mapping,unique" json:"transaction_id"`
	BrandId           int  `gorm:"size:30;column:brand_id;index:idx_approval_mapping,unique" json:"brand_id"`
	ProfitCenterId    int  `gorm:"size:30;column:profit_center_id;index:idx_approval_mapping,unique" json:"profit_center_id"`
	CostCenterId      int  `gorm:"size:30;column:cost_center_id;index:idx_approval_mapping,unique" json:"cost_center_id"`
}

// custom tablename
func (e *ApprovalMapping) TableName() string {
	return TableNameApprovalMapping
}
