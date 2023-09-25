from pydantic import BaseModel

class PriceCodeRequest(BaseModel):
    brand_id:int
    price_code:str
    price_code_name:str
    price_code_customized:bool
    price_code_modifiabled:bool
    price_code_otr_modifiabled:bool
    price_code_dp_modifiabled:bool

class PriceCodeSchema(PriceCodeRequest):
    is_active:bool
    price_code_id:int

    class Config:
        orm_mode = True
