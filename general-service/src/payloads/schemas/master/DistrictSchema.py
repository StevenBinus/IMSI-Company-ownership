
from pydantic import BaseModel

class MtrDistrict(BaseModel):
    district_code: str
    district_name: str
    city_id : int
    province_id:int

class MtrDistrictUpdate(BaseModel):
    district_name: str