from typing import List, Optional
from pydantic import BaseModel


class MtrAreaRequest(BaseModel):
    area_code:str
    description:str
    region_id:int
    class Config:
        orm_mode = True

class MtrAreaUpdate(BaseModel):
    region_id:int
    description:str
    class Config:
        orm_mode = True

class MtrAreaSchema(BaseModel):
    is_active:Optional[bool]=None
    area_id:Optional[int]=None

    class Config:
        orm_mode = True
