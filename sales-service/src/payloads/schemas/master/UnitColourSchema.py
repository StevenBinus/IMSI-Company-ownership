from pydantic import BaseModel

class UnitColourRequest(BaseModel):
    vehicle_brand:int
    colour_code:str
    description_commercial:str
    description_police:str