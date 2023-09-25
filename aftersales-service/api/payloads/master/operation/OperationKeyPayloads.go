package masteroperationpayloads

type OperationKeyResponse struct {
	IsActive                bool   `json:"is_active"`
	OperationKeyId          int32  `json:"operation_key_id"`
	OperationKeyCode        string `json:"operation_key_code"`
	OperationGroupId        int32  `json:"operation_group_id"`
	OperationSectionId      int32  `json:"operation_section_id"`
	OperationKeyDescription string `json:"operation_key_description"`
}

type OperationKeyRequest struct {
	OperationKeyCode        string `json:"operation_key_code"`
	OperationGroupId        int32  `json:"operation_group_id"`
	OperationSectionId      int32  `json:"operation_section_id"`
	OperationKeyDescription string `json:"operation_key_description"`
}
