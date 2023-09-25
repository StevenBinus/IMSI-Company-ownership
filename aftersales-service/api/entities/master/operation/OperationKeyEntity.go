package masteroperationentities

const TableNameOperationKey = "mtr_operation_key"

type OperationKey struct {
	IsActive                bool             `gorm:"column:is_active;not null;default:true" json:"is_active"`
	OperationKeyId          int32            `gorm:"column:operation_key_id;not null;primaryKey"  json:"operation_key_id"`
	OperationKeyCode        string           `gorm:"column:operation_key_code;not null"  json:"operation_key_code"`
	OperationGroupId        int32            `gorm:"column:operation_group_id;not null"  json:"operation_group_id"` //udah
	OperationGroup          OperationGroup   `gorm:"references:operation_group_id"`
	OperationSectionId      int32            `gorm:"column:operation_section_id;not null"  json:"operation_section_id"` //udah
	OperationSection        OperationSection `gorm:"constraint:OnUpdate:CASCADE,OnDelete:CASCADE;references:operation_section_id"`
	OperationKeyDescription string           `gorm:"column:operation_key_description;not null"  json:"operation_key_description"`
}

func (*OperationKey) TableName() string {
	return TableNameOperationKey
}
