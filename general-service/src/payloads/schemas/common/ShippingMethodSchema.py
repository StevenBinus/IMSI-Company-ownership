from typing import List, Optional
from pydantic import BaseModel

class MtrShippingMethodGetSchema(BaseModel):
    shipping_method_code :Optional[str] = None
    shipping_method_description :Optional[str] = None
    
    class Config:
        orm_mode = True