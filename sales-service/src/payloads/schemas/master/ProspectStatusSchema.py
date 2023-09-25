from pydantic import BaseModel

class ProspectStatusRequest(BaseModel):
    prospect_status_code:str
    prospect_status_description:str

class ProspectStatusSchema(ProspectStatusRequest):  
    is_active:bool
    prospect_status_id:int
    class Config:
        orm_mode = True
