from pydantic import BaseModel
from datetime import datetime


class TrxSpmFormTakeRequest(BaseModel):
    taken_document_number:str
    spm_issue_date:datetime
    spm_issued_by:int
    spm_issued_to:int

class TrxSpmFormTakeSchema(TrxSpmFormTakeRequest):
    taken_system_number:int
    taken_system_number_old:int

    company_id:int
    brand_id:int
    total_spm_taken:int
    print_counter:int
    class Config:
        orm_mode = True

class TrxSpmFormTakeAssigned(BaseModel):
    vehicle_sales_order_system_number:int
    vehicle_sales_order_document_number:str

class TrxSpmFormTakeRequestDetail(BaseModel):
    spm_issued_to:int
    spm_list:list[TrxSpmFormTakeAssigned]

class TrxSpmFormTakeDeleteRequest(BaseModel):
    taken_detail_system_number:list[int]

class TrxSpmformTakeDetailRequest(BaseModel):
    taken_system_number:int
    vehicle_sales_order_document_number:str
    vehicle_sales_order_system_number:int
class TrxSpmformTakeDetailSchema(TrxSpmformTakeDetailRequest):
    taken_detail_system_number:int
    taken_detail_system_number_old:int
    class Config:
        orm_mode = True


class TakeResponseHeaderDetail(BaseModel):
    taken_system_number:int
    taken_document_number:str
    spm_issue_date:datetime
    spm_issued_by:int
    spm_issued_to:int
    spmtakelist:list