from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class TrxPDIRequestAllSchema(BaseModel):
    brand_id: int
    pdi_request_date: datetime
    company_id: int
    issued_by_id: int
    service_dealer_id: int
    service_by_id: int
    total_frt: int
    pdi_request_remark: str


    class Config:
        orm_mode = True

class TrxPDIRequestDetailSchema(BaseModel):
    pdi_request_system_number: int
    vehicle_id : int
    operation_number_id: int
    estimated_delivery: datetime
    frt: int
    service_date: datetime
    service_time: int
    pdi_status_id: int
    pdi_request_detail_line_status_id: int
    pdi_request_detail_line_remark: str


    class Config:
        orm_mode = True

class TrxPDIRequestPostSchema(BaseModel):
    brand_id: int
    pdi_request_date: datetime
    service_dealer_id: int
    pdi_request_remark: str

    class Config:
        orm_mode = True

class TrxPDIRequestResponseHeaderDetail(BaseModel):
    brand_id :int
    pdi_request_document_number:str
    pdi_request_date:datetime
    company_id: int
    issued_by_id: int
    service_dealer_id:int
    service_by_id: int
    total_frt:int
    pdi_request_remark: str
    pdirequestlist:list