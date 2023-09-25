from typing import Optional

from pydantic import BaseModel

class MtrCostCenterSchema(BaseModel):
    is_active: Optional[bool] = None 
    cost_center_id: int
    cost_center_code: str
    cost_center_name: str

    class Config:
        orm_mode = True

class MtrCostCenterPost(BaseModel):
    cost_center_code:str
    cost_center_name:str

    class Config:
        orm_mode=True

class GetMtrCostCenterSchema(BaseModel):
    detail: str
    data: Optional[MtrCostCenterSchema]


class MtrUpdateCostCenterSchema(BaseModel):
    is_active: Optional[bool] = None 
    cost_center_code: str
    cost_center_name: str

    class Config:
        orm_mode = True
