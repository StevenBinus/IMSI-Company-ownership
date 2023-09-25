from typing import List, Optional
from pydantic import BaseModel
from src.payloads import Pagination

class MtrProvinceSchema(BaseModel):
    is_active:Optional[bool]=None
    province_id:Optional[int]=None
    province_code:str
    province_name:str
    country_id:int

    class Config:
        orm_mode = True

class MtrProvincePost(BaseModel):
    province_code:str
    province_name:str
    country_id:int

    class Config:
        orm_mode = True


class MtrProvincePagination(BaseModel):
    status_code:int
    msg_status:str
    data:Pagination.PaginationSchema