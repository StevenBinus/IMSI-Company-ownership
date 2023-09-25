package masteroperationpayloads

type OperationSectionResponse struct {
	IsActive                    bool   `json:"is_active"`
	OperationSectionId          int    `json:"operation_section_id"`
	OperationSectionCode        string `json:"operation_section_code"`
	OperationGroupId            int    `json:"operation_group_id"`
	OperationSectionDescription string `json:"operation_section_description"`
}

type OperationSectionListResponse struct {
	IsActive                    bool   `json:"is_active" entity:"mtr_operation_section"`
	OperationSectionId          int    `json:"operation_section_id" entity:"mtr_operation_section"`
	OperationSectionCode        string `json:"operation_section_code" entity:"mtr_operation_section"`
	OperationSectionDescription string `json:"operation_section_description" entity:"mtr_operation_section"`
	OperationGroupId            int    `json:"operation_group_id" entity:"mtr_operation_section"`
	OperationGroupCode          string `json:"operation_group_code" entity:"mtr_operation_group"`
	OperationGroupDescription   string `json:"operation_group_description" entity:"mtr_operation_group"`
}

type OperationSectionRequest struct {
	IsActive                    bool   `json:"is_active"`
	OperationSectionId          int    `json:"operation_section_id"`
	OperationSectionCode        string `json:"operation_section_code"`
	OperationGroupId            int    `json:"operation_group_id"`
	OperationSectionDescription string `json:"operation_section_description"`
}

type OperationSectionDescriptionResponse struct {
	OperationSectionDescription string `json:"operation_section_description"`
}
