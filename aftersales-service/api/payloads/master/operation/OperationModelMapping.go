package masteroperationpayloads

type OperationModelMappingResponse struct {
	IsActive                bool  `json:"is_active"`
	OperationModelMappingId int32 `json:"operation_model_mapping_id"`
	BrandId                 int32 `json:"brand_id"`
	ModelId                 int32 `json:"model_id"`
	OperationGroupId        int32 `json:"operation_group_id"`
	OperationUsingIncentive bool  `json:"operation_using_incentive"`
	OperationUsingActual    bool  `json:"operation_using_actual"`
	OperationPdi            bool  `json:"operation_pdi"`
}

type OperationModelMappingRequest struct {
	BrandId                 int32 `json:"brand_id"`
	ModelId                 int32 `json:"model_id"`
	OperationGroupId        int32 `json:"operation_group_id"`
	OperationUsingIncentive bool  `json:"operation_using_incentive"`
	OperationUsingActual    bool  `json:"operation_using_actual"`
	OperationPdi            bool  `json:"operation_pdi"`
}
