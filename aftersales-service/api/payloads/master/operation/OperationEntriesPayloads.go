package masteroperationpayloads

type OperationEntriesResponse struct {
	IsActive             bool   `json:"is_active"`
	OperationEntriesId   int32  `json:"operation_entries_id"`
	OperationEntriesCode string `json:"operation_entries_code"`
	OperationGroupId     int32  `json:"operation_group_id"`
	OperationSectionId   int32  `json:"operation_section_id"`
	OperationKeyId       int32  `json:"operation_key_id"`
	OperationEntriesDesc string `json:"operation_entries_desc"`
}

type OperationEntriesRequest struct {
	OperationEntriesCode string `json:"operation_entries_code"`
	OperationGroupId     int32  `json:"operation_group_id"`
	OperationSectionId   int32  `json:"operation_section_id"`
	OperationKeyId       int32  `json:"operation_key_id"`
	OperationEntriesDesc string `json:"operation_entries_desc"`
}
