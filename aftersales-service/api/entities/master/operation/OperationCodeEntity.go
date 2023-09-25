package masteroperationentities

const TableNameOperationCode = "mtr_operation_code"

type OperationCode struct {
	IsActive                bool             `gorm:"column:is_active;not null;default:true" json:"is_active"`
	OperationId             int32            `gorm:"column:operation_id;not null;primaryKey"  json:"operation_id"`
	OperationCode           string           `gorm:"column:operation_code;not null"  json:"operation_code"`
	OperationName           string           `gorm:"column:operation_name;null"  json:"operation_name"`
	OperationGroupId        int32            `gorm:"column:operation_group_id;not null"  json:"operation_group_id"`
	OperationGroup          OperationGroup   `gorm:"references:operation_group_id" json:"operation_group"`
	OperationSectionId      int32            `gorm:"column:operation_section_id;not null"  json:"operation_section_id"`
	OperationSection        OperationSection `gorm:"references:operation_section_id" json:"operation_section"`
	OperationKeyId          int32            `gorm:"column:operation_key_id;not null"  json:"operation_key_id"`
	OperationKey            OperationKey     `gorm:"references:operation_key_id" json:"operation_key"`
	OperationEntriesId      int32            `gorm:"column:operation_entries_id;not null"  json:"operation_entries_id"`
	OperationEntries        OperationEntries `gorm:"references:operation_entries_id" json:"operation_entries"`
	OperationUsingIncentive bool             `gorm:"column:operation_using_incentive;null"  json:"operation_using_incentive"`
	OperationUsingActual    bool             `gorm:"column:operation_using_actual;null"  json:"operation_using_actual"`
}

func (*OperationCode) TableName() string {
	return TableNameOperationCode
}
