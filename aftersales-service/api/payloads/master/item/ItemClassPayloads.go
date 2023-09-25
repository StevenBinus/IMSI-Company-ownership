package masteritempayloads

type ItemClassRequest struct {
	ItemClassCode string `json:"item_class_code"`
	ItemGroupID   int    `json:"item_group_id"` //FK with mtr_item_group common-general service
	LineTypeID    int    `json:"line_type_id"`  //FK with mtr_line_type common-general service
}

type ItemClassResponse struct {
	IsActive      bool   `json:"is_active"`
	ID            int32  `json:"id"`
	ItemClassCode string `json:"item_class_code"`
	ItemGroupID   int    `json:"item_group_id"` //FK with mtr_item_group common-general service
	LineTypeID    int    `json:"line_type_id"`  //FK with mtr_line_type common-general service
}
