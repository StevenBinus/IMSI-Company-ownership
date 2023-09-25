from typing import List, Optional
from pydantic import BaseModel

class MtrTransferTypeGetSchema(BaseModel):
    transfer_type_code:Optional[str] = None
    transfer_type_description:Optional[str] = None
    
    class Config:
        orm_mode = True