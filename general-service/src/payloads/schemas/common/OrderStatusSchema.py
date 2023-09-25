from typing import List, Optional
from pydantic import BaseModel

class MtrOrderStatusGetSchema(BaseModel):
    order_status_code:Optional[str] = None
    order_status_description:Optional[str] = None
    
    class Config:
        orm_mode = True