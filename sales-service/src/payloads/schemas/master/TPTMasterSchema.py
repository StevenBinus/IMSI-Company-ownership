from pydantic import BaseModel

class MtrTPTRequest(BaseModel):
    tpt_type:str
    tpt_quota:int
    tpt_remaining:int
    tpt_used:int
    tpt_status:str
    unit_variant_id:int

class MtrTPTSchema(MtrTPTRequest):
    is_active:bool
    tpt_id:int

class MtrTPTChassisRequest(BaseModel):
    tpt_id:int
    vehicle_id:int
    chassis_no_status:str

class MtrTPTChassisSchema(MtrTPTChassisRequest):
    is_active:bool
    tpt_chassis_id:int

    class Config:
        orm_mode = True