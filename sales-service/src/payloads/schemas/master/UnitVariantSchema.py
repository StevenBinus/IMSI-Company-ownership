from pydantic import BaseModel
from datetime import datetime

class UnitVariantRequest(BaseModel):
    variant_code:str
    model_id:int
    variant_description:str
    release_date:datetime
    discontinue_date:datetime
    chassis_prefix:str
    engine_prefix:str
    prod_year:str
    sales_allow:bool
    indent_indicator:bool
    dp_amount:float
    cylinder_id:int
    fuel_id:int
    unit_type:int
    transmission:int
    wheel_drive:int
    vehicle_type_police_invoice:str
    vehicle_kind_police_invoice:str
    SUT:str
    price:float