package masteroperationentities

const TableNameOperationModelMapping = "mtr_operation_model_mapping"

type OperationModelMapping struct {
	IsActive                bool           `gorm:"column:is_active;not null;default:true" json:"is_active"`
	OperationModelMappingId int32          `gorm:"column:operation_model_mapping_id;not null;primaryKey" json:"operation_model_mapping_id"`
	BrandId                 int32          `gorm:"column:brand_id;not null" json:"brand_id"` //fk luar
	ModelId                 int32          `gorm:"column:model_id;not null" json:"model_id"` //fk luar
	OperationGroupId        int32          `gorm:"column:operation_group_id;not null"  json:"operation_group_id"`
	OperationGroup          OperationGroup `gorm:"references:operation_group_id" json:"operation_group"`
	OperationUsingIncentive bool           `gorm:"column:operation_using_incentive;null" json:"operation_using_incentive"`
	OperationUsingActual    bool           `gorm:"column:operation_using_actual;null" json:"operation_using_actual"`
	OperationPdi            bool           `gorm:"column:operation_pdi;null" json:"operation_pdi"`
}

func (*OperationModelMapping) TableName() string {
	return TableNameOperationModelMapping
}
