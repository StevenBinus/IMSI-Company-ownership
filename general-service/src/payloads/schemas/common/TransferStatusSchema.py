from typing import List, Optional
from pydantic import BaseModel

class MtrTransferStatusGetSchema(BaseModel):
    transfer_status_code:Optional[str] = None
    transfer_status_description:Optional[str] = None
    
    class Config:
        orm_mode = True