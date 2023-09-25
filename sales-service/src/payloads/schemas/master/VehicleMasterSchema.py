from datetime import datetime
from pydantic import BaseModel

class VehicleMasterRequest(BaseModel):
    vehicle_id:int
    vehicle_chassis_number:str
    vehicle_registration_certificate_tnkb:str
    vehicle_service_booking_number:str
    vehicle_registration_certificate_owner_name:str
    model_variant_colour_description:str
    vehicle_production_year:int
    vehicle_last_service_date:datetime

class VehicleMasterSchema(VehicleMasterRequest):
    is_active:bool
    vehicle_id:int

    class Config:
        orm_mode = True
