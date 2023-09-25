from typing import List, Optional
from pydantic import BaseModel

class MtrApprovalStatusGetSchema(BaseModel):
    approval_status_code:Optional[str] = None
    approval_status_description:Optional[str] = None
    
    class Config:
        orm_mode = True