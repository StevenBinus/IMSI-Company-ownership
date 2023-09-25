from typing import List, Optional
from pydantic import BaseModel

class MtrTransportGetSchema(BaseModel):
    transport_code:Optional[str] = None
    transport_description:Optional[str] = None
    
    class Config:
        orm_mode = True