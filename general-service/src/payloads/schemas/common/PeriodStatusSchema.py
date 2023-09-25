from typing import List, Optional
from pydantic import BaseModel

class MtrPeriodStatusGetSchema(BaseModel):
    period_status_code:Optional[str] = None
    period_status_description:Optional[str] = None
    
    class Config:
        orm_mode = True