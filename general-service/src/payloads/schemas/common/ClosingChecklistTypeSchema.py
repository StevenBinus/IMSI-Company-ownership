from typing import List, Optional
from pydantic import BaseModel

class MtrClosingChecklistTypeGetSchema(BaseModel):
    closing_checklist_type_code:Optional[str] = None
    closing_checklist_type_description:Optional[str] = None
    
    class Config:
        orm_mode = True