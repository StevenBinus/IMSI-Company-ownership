from pydantic import BaseModel

class MtrAddressRequest(BaseModel):
    address_latitude:float
    address_longitude:float
    address_street_1:str
    address_street_2:str
    address_street_3:str
    address_type:str
    village_id:int

    class Config:
        orm_mode = True


class MtrAddressUpdate(BaseModel):
    address_latitude:float
    address_longitude:float
    address_street_1:str
    address_street_2:str
    address_street_3:str
    address_type:str

    class Config:
        orm_mode = True