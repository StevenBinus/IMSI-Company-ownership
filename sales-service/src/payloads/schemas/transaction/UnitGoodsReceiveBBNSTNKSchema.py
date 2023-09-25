from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class TrxUnitGoodsReceiveBBNSTNKRequest(BaseModel):
    company_id: int
    goods_receive_bbn_stnk_date: datetime
    purchase_order_bbn_detail_system_number: int
    police_invoice_number: str
    stnk_number: str
    stnk_expired_date: datetime
    stnk_received_date: datetime
    stnk_received_by: int
    supplier_reference_number: str
    goods_receive_bbn_stnk_remark: str

class TrxUnitGoodsReceiveBBNSTNKInputSendRequest(BaseModel):
    stnk_send_date: datetime
    stnk_receiver_name: str
    stnk_receiver_id_number: str

class TrxUnitGoodsReceiveBBNSTNKUpdateRequest(BaseModel):
    goods_receive_bbn_stnk_date: datetime
    police_invoice_number: str
    stnk_expired_date: datetime
    stnk_received_date: datetime
    stnk_received_by: int
    supplier_reference_number: str
    goods_receive_bbn_stnk_remark: str