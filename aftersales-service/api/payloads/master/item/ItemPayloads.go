package masteritempayloads

type ItemLookupTestingPurposes struct {
	ItemId int32 `json:"item_id"`
	// itemcode string `json:"item_code"`
	// ItemName     string `json:"item_name"`
	// ItemType     string `json:"item_type"`
	ItemGroupId int `json:"item_group_id"` //fk luar mtr_item_group, item_group_id
	// ItemClass string `json:"item_class_code"` //item_class_id -> ItemClassName
	// SupplierCode string `json:"supplier_code"`   //supplier_id -> supplier_code
	// SupplierName string `json:"supplier_name"`   //supplier_id -> supplier_name
}

type DisplayItemLookupTestingPurposes struct {
	ItemId      int32  `json:"item_id"`
	SectionCode string `json:"operation_section_code"`
}

type ItemResponse struct {
	IsActive                     bool    `json:"is_active"`
	ItemId                       int32   `json:"item_id"`
	ItemCode                     string  `json:"item_code"`
	ItemClassId                  int32   `json:"item_class_id"`
	ItemName                     string  `json:"item_name"`
	ItemGroupId                  int32   `json:"item_group_id"`
	ItemType                     string  `json:"item_type"`
	ItemLevel_1                  string  `json:"item_level_1"`
	ItemLevel_2                  string  `json:"item_level_2"`
	ItemLevel_3                  string  `json:"item_level_3"`
	ItemLevel_4                  string  `json:"item_level_4"`
	SupplierId                   int32   `json:"supplier_id"`
	UnitOfMeasurementTypeId      int32   `json:"unit_of_measurement_type_id"`
	UnitOfMeasurementSelling     string  `json:"unit_of_measurement_selling"`
	UnitOfMeasurementPurchaseId  int32   `json:"unit_of_measurement_purchase_id"`
	UnitOfMeasurementStockId     int32   `json:"unit_of_measurement_stock_id"`
	SalesItem                    string  `json:"sales_item"`
	Lottable                     string  `json:"lottable"`
	Inspection                   string  `json:"inspection"`
	PriceListItem                string  `json:"price_list_item"`
	StockKeeping                 bool    `json:"stock_keeping"`
	DiscountId                   int32   `json:"discount_id"`
	MarkupMasterId               int32   `json:"markup_master_id"`
	DimensionOfLength            float64 `json:"dimension_of_length"`
	DimensionOfWidth             float64 `json:"dimension_of_width"`
	DimensionOfHeight            float64 `json:"dimension_of_height"`
	DimensionUnitOfMeasurementId int32   `json:"dimension_unit_of_measurement_id"`
	Weight                       float64 `json:"weight"`
	UnitOfMeasurementWeight      string  `json:"unit_of_measurement_weight"`
	StorageTypeId                int32   `json:"storage_type_id"`
	Remark                       string  `json:"remark"`
	AtpmWarrantyClaimTypeId      int32   `json:"atpm_warranty_claim_type_id"`
	LastPrice                    float64 `json:"last_price"`
	UseDiscDecentralize          string  `json:"use_disc_decentralize"`
	CommonPricelist              bool    `json:"common_pricelist"`
	IsRemovable                  bool    `json:"is_removable"`
	IsMaterialPlus               bool    `json:"is_material_plus"`
	SpecialMovementId            int32   `json:"special_movement_id"`
	IsItemRegulation             string  `json:"is_item_regulation"`
	IsTechnicalDefect            string  `json:"is_technical_defect"`
	IsMandatory                  bool    `json:"is_mandatory"`
	MinimumOrderQty              float64 `json:"minimum_order_qty"`
	HarmonizedNo                 string  `json:"harmonized_no"`
	AtpmSupplierId               int32   `json:"atpm_supplier_id"`
	AtpmVendorSuppliability      string  `json:"atpm_vendor_suppliability"`
	PmsItem                      string  `json:"pms_item"`
	Regulation                   string  `json:"regulation"`
	AutoPickWms                  string  `json:"auto_pick_wms"`
	GmmCatalogCode               int32   `json:"gmm_catalog_code"`
	PrincipalBrandParentId       int32   `json:"principal_brand_parent_id"`
	ProportionalSupplyWms        string  `json:"proportional_supply_WMS"`
	Remark2                      string  `json:"remark2"`
	Remark3                      string  `json:"remark3"`
	SourceTypeId                 int32   `json:"source_type_id"`
	AtpmSupplierCodeOrderId      int32   `json:"atpm_supplier_code_order_id"`
	PersonInChargeId             int32   `json:"person_in_charge_id"`
}

type ItemRequest struct {
	ItemCode                     string  `json:"item_code"`
	ItemClassId                  int32   `json:"item_class_id"`
	ItemName                     string  `json:"item_name"`
	ItemGroupId                  int32   `json:"item_group_id"`
	ItemType                     string  `json:"item_type"`
	ItemLevel1                   string  `json:"item_level_1"`
	ItemLevel2                   string  `json:"item_level_2"`
	ItemLevel3                   string  `json:"item_level_3"`
	ItemLevel4                   string  `json:"item_level_4"`
	SupplierId                   int32   `json:"supplier_id"`
	UnitOfMeasurementTypeId      int32   `json:"unit_of_measurement_type_id"`
	UnitOfMeasurementSelling     string  `json:"unit_of_measurement_selling"`
	UnitOfMeasurementPurchaseId  int32   `json:"unit_of_measurement_purchase_id"`
	UnitOfMeasurementStockId     int32   `json:"unit_of_measurement_stock_id"`
	SalesItem                    string  `json:"sales_item"`
	Lottable                     string  `json:"lottable"`
	Inspection                   string  `json:"inspection"`
	PriceListItem                string  `json:"price_list_item"`
	StockKeeping                 bool    `json:"stock_keeping"`
	DiscountId                   int32   `json:"discount_id"`
	MarkupMasterId               int32   `json:"markup_master_id"`
	DimensionOfLength            float64 `json:"dimension_of_length"`
	DimensionOfWidth             float64 `json:"dimension_of_width"`
	DimensionOfHeight            float64 `json:"dimension_of_height"`
	DimensionUnitOfMeasurementId int32   `json:"dimension_unit_of_measurement_id"`
	Weight                       float64 `json:"weight"`
	UnitOfMeasurementWeight      string  `json:"unit_of_measurement_weight"`
	StorageTypeId                int32   `json:"storage_type_id"`
	Remark                       string  `json:"remark"`
	AtpmWarrantyClaimTypeId      int32   `json:"atpm_warranty_claim_type_id"`
	LastPrice                    float64 `json:"last_price"`
	UseDiscDecentralize          string  `json:"use_disc_decentralize"`
	CommonPricelist              bool    `json:"common_pricelist"`
	IsRemovable                  bool    `json:"is_removable"`
	IsMaterialPlus               bool    `json:"is_material_plus"`
	SpecialMovementId            int32   `json:"special_movement_id"`
	IsItemRegulation             string  `json:"is_item_regulation"`
	IsTechnicalDefect            string  `json:"is_technical_defect"`
	IsMandatory                  bool    `json:"is_mandatory"`
	MinimumOrderQty              float64 `json:"minimum_order_qty"`
	HarmonizedNo                 string  `json:"harmonized_no"`
	AtpmSupplierId               int32   `json:"atpm_supplier_id"`
	AtpmVendorSuppliability      string  `json:"atpm_vendor_suppliability"`
	PmsItem                      string  `json:"pms_item"`
	Regulation                   string  `json:"regulation"`
	AutoPickWms                  string  `json:"auto_pick_wms"`
	GmmCatalogCode               int32   `json:"gmm_catalog_code"`
	PrincipalBrandParentId       int32   `json:"principal_brand_parent_id"`
	ProportionalSupplyWms        string  `json:"proportional_supply_WMS"`
	Remark2                      string  `json:"remark2"`
	Remark3                      string  `json:"remark3"`
	SourceTypeId                 int32   `json:"source_type_id"`
	AtpmSupplierCodeOrderId      int32   `json:"atpm_supplier_code_order_id"`
	PersonInChargeId             int32   `json:"person_in_charge_id"`
}

type ItemLookup struct {
	IsActive    bool   `json:"is_active" entity:"mtr_item"`
	ItemId      int32  `json:"item_id" entity:"mtr_item"`
	ItemCode    string `json:"item_code" entity:"mtr_item"`
	ItemClassId int32  `json:"item_class_id" entity:"mtr_item_class"`
	ItemName    string `json:"item_name" entity:"mtr_item"`
	ItemGroupId int32  `json:"item_group_id" entity:"mtr_item"`
	ItemType    string `json:"item_type" entity:"mtr_item"`
	SupplierId  int32  `json:"supplier_id" entity:"mtr_item"`
}

type ItemLookupDisplay struct {
	ItemId        int32  `json:"item_id"`
	ItemCode      string `json:"item_code"`
	ItemName      string `json:"item_name"`
	ItemGroupName string `json:"item_group_name"` //fk luar mtr_item_group, item_group_id
	// ItemType      string `json:"item_type"`
	// ItemClass    string `json:"item_class_code"` //fk dalam item_class_id -> ItemClassName
	// SupplierCode string `json:"supplier_code"`   //fk luar mtr_supplier supplier_id -> supplier_code
	// SupplierName string `json:"supplier_name"`   //supplier_id -> supplier_name
}
