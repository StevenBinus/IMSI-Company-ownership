from typing import List, Optional
from pydantic import BaseModel

class MtrBankTypeGetSchema(BaseModel):
    bank_type_code:Optional[str] = None
    bank_type_description:Optional[str] = None
    
    class Config:
        orm_mode = True