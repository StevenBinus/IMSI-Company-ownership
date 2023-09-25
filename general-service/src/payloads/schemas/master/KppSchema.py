from pydantic import BaseModel


class MtrKppPost(BaseModel):
    kpp_code:str
    kpp_name :str
    kpp_phone_no :str
    kpp_address_1:str
    kpp_address_2:str
    kpp_address_3:str
    village_id:int

    class config:
        orm_mode=True

class MtrKppUpdate(BaseModel):
    kpp_name:str
    kpp_phone_no:str
    kpp_address_1:str
    kpp_address_2:str
    kpp_address_3:str
    village_id:int


    class config:
        orm_mode=True


