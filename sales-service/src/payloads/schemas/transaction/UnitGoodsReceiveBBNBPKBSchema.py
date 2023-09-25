from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class TrxUnitGoodsReceiveBBNBPKBRequest(BaseModel):
    company_id: int
    goods_receive_bbn_bpkb_date: datetime
    goods_receive_bbn_stnk_system_number: int
    bpkb_number: str
    bpkb_issue_date: datetime
    bpkb_received_date: datetime
    bpkb_received_by: int
    supplier_reference_number: str
    goods_receive_bbn_bpkb_remark: str

class TrxUnitGoodsReceiveBBNBPKBInputSendRequest(BaseModel):
    bpkb_send_date: datetime
    bpkb_receiver_name: str
    bpkb_receiver_id_number: str

class TrxUnitGoodsReceiveBBNBPKBUpdateRequest(BaseModel):
    goods_receive_bbn_bpkb_date: datetime
    bpkb_number: str
    bpkb_issue_date: datetime
    bpkb_received_date: datetime
    bpkb_received_by: int
    supplier_reference_number: str
    goods_receive_bbn_bpkb_remark: str