from typing import List, Optional
from pydantic import BaseModel

class MtrVillagePost(BaseModel):
    village_code:str
    village_name:str
    village_zip_code:str
    district_id:int
    city_id:int
    province_id:int

    class config:
        orm_mode = True


class MtrVillageGetSchema(BaseModel):
    village_code:Optional[str] = None
    village_name:Optional[str] = None
    
    class Config:
        orm_mode = True