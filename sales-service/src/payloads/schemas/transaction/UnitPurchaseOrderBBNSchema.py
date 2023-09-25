from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class TrxUnitPurchaseOrderBBNCostDetailRequest(BaseModel):
    purchase_order_bbn_detail_system_number: int
    cost_type_id: int
    cost_amount: float
    vat_charged: bool

class TrxUnitPurchaseOrderBBNDetailRequest(BaseModel):
    purchase_order_bbn_system_number: int
    vehicle_id: int

class TrxUnitPurchaseOrderBBNRequest(BaseModel):
    company_id: int
    dealer_representative_id: int
    cost_center_id: int
    purchase_order_date: datetime
    purchase_order_remark: str
    brand_id: int
    supplier_id: int
    term_of_payment_id: int
    bill_code_id: int
    down_payment_request: float

    class Config:
        orm_mode = True

class TrxUnitPurchaseOrderBBNRequestUpdate(BaseModel):
    purchase_order_date: datetime
    purchase_order_remark: str
    down_payment_request: float

class TrxUnitPurchaseOrderBBNCostDetailRequestUpdate(BaseModel):
    cost_type_id: int
    cost_amount: float
    vat_charged: bool

class TrxUnitPurchaseOrderBBNResponse(BaseModel):
    purchase_order_bbn_document_number: str
    purchase_order_date: datetime
    brand_id: int
    supplier_id: int
    term_of_payment_id: int
    bill_code_id: int
    cost_center_id: int
    currency_id: int
    purchase_order_remark: str
    down_payment_request: float
    total_after_vat: Optional[float]
    purchase_order_bbn_detail: list

class TrxUnitPurchaseOrderBBNDetailResponse(BaseModel):
    vehicle_chassis_number: str
    vehicle_engine_number: str
    supplier_name: str
    purchase_price: float
    purchase_order_bbn_cost_detail: list