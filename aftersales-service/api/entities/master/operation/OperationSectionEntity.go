package masteroperationentities

const TableNameOperationSection = "mtr_operation_section"

type OperationSection struct {
	IsActive                    bool           `gorm:"column:is_active;not null;default:true" json:"is_active"`
	OperationSectionId          int            `gorm:"column:operation_section_id;not null;primaryKey" json:"operation_section_id"`
	OperationSectionCode        string         `gorm:"column:operation_section_code;not null;size:3" json:"operation_section_code"`
	OperationGroupId            int            `gorm:"column:operation_group_id;not null;" json:"operation_group_id"`
	OperationGroup              OperationGroup `gorm:"references:operation_group_id" json:"operation_group"`
	OperationSectionDescription string         `gorm:"column:operation_section_description;not null;size:50" json:"operation_section_description"`
}

func (*OperationSection) TableName() string {
	return TableNameOperationSection
}
