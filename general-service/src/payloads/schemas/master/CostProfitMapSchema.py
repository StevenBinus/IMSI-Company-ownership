from pydantic import BaseModel
from typing import Optional

class MtrCostProfitMapSchema(BaseModel):
    company_id:int
    profit_center_id:int
    cost_center_id:int
    mapping_description:str

class mtrCostProfitMapUpdateSchema(BaseModel):
    mapping_description:str

