from pydantic import BaseModel
from datetime import datetime

class SpmFormRegisterRequest(BaseModel):
    company_id:int
    spm_received_by:str
    spm_received_date:datetime
    spm_number_format:str
    spm_number_from:int
    total_spm:int
    reference_document_number:str

class SpmFormRegisterSchema(SpmFormRegisterRequest):
    register_system_number:int
    register_system_number_old:int
    class Config:
        orm_mode = True

class SpmDetail(BaseModel):
    spm_doc:str

class HeaderDetail(SpmFormRegisterSchema):
    spm_list:list[SpmDetail]
    class Config:
        orm_mode = True

class SpmFormRegisterHeaderDetailResponse(BaseModel):
    company_id:int
    register_document_number:str
    spm_received_date:datetime
    spm_received_by:str
    spm_number_format:str
    spm_number_from:int
    total_spm:int
    list_spm:list

class SPMFormRegisterDetailRequest(BaseModel):
    register_system_number_id:int
    register_document_number:int
    spm_document_number:str
    last_taken_system_number:int
    last_return_system_number:int
    last_spm_status:str

class SPMFormRegisterDetailSchema(SPMFormRegisterDetailRequest):
    spm_form_registration_detail_id:int
    class Config:
        orm_mode = True

class customResponse(BaseModel):
    spm_number_format:str
    spm_number_from:int
    total_spm:int
    class Config:
        orm_mode = True