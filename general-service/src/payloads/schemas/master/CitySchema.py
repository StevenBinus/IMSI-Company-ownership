from pydantic import BaseModel


class MtrCitySchemaByList(BaseModel):
    city_code:str
    city_name :str
    city_phone_area :str
    province_id :int

    class config:
        orm_mode=True

class MtrCityUpdate(BaseModel):
    city_name:str
    city_phone_area:str

    class config:
        orm_mode=True


