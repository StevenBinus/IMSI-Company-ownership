from typing import List, Optional
from pydantic import BaseModel

class MtrClosingModuleGrouplistGetSchema(BaseModel):
    closing_module_grouplist_code:Optional[str] = None
    closing_module_grouplist_description:Optional[str] = None
    
    class Config:
        orm_mode = True