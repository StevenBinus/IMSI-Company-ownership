from pydantic import BaseModel

class UnitGroupRequest(BaseModel):
    unit_group_code:str
    unit_group_name:str

class UnitGroupSchema(UnitGroupRequest):
    is_active:bool
    unit_group_id:int

    class Config:
        orm_mode = True