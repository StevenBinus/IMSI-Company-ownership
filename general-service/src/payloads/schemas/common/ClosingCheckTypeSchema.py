from typing import List, Optional
from pydantic import BaseModel

class MtrClosingCheckTypeGetSchema(BaseModel):
    closing_check_type_code:Optional[str] = None
    closing_check_type_description:Optional[str] = None
    
    class Config:
        orm_mode = True