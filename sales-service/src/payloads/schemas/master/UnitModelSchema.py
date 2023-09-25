from pydantic import BaseModel
from datetime import datetime

class MtrUnitModelRequest(BaseModel):
    vehicle_brand_id:int
    model_code:str
    model_description:str
    unit_group_id:int
    discontinue_date:datetime
    sales_allow:bool
    indent_indicator:bool
    warranty_expired_year:float
    warranty_expired_mileage:float
    free_service_expired_month:float
    free_service_expired_mileage:float

class MtrUnitModelSchema(MtrUnitModelRequest):
    is_active:bool
    model_id:int