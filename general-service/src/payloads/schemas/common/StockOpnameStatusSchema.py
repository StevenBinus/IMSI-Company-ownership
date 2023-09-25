from typing import List, Optional
from pydantic import BaseModel

class MtrStockOpnameStatusGetSchema(BaseModel):
    stock_opname_status_code:Optional[str] = None
    stock_opname_status_name:Optional[str] = None
    
    class Config:
        orm_mode = True

