from typing import List, Optional
from pydantic import BaseModel

class MtrLandedCostTypeGetSchema(BaseModel):
    landed_cost_type_code:Optional[str] = None
    landed_cost_type_desc:Optional[str] = None
    
    class Config:
        orm_mode = True