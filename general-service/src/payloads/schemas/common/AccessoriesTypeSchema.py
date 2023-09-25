from typing import List, Optional
from pydantic import BaseModel

class MtrAccessoriesTypeGetSchema(BaseModel):
    accessories_type_code:Optional[str] = None
    accessories_type_description:Optional[str] = None
    
    class Config:
        orm_mode = True
