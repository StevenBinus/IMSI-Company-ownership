from typing import List, Optional
from pydantic import BaseModel

class MtrRFPPaidInGetSchema(BaseModel):
    rfp_paid_in_code:Optional[str] = None
    rfp_paid_in_description:Optional[str] = None
    
    class Config:
        orm_mode = True