from fastapi import Request
from sqlalchemy import select
from sqlalchemy.orm import load_only
from src.entities.master.VehicleEntity import MtrVehicle
from src.entities.master.VehicleEntity import MtrVehicle as vehicle
from src.entities.master.VehicleRegistrationCertificateEntity import MtrVehicleRegistrationCertificate as regist_certif

from src.entities.master.ModelVariantColourEntity import MtrModelVariantColour as model_variant_colour

from src.payloads.schemas.master.VehicleMasterSchema import VehicleMasterRequest
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search

def get_vehicle_master_search(page:int,limit:int,all_params:dict()):
    db = get_db()
    try:
        query_set = select(
                        vehicle.vehicle_chassis_number,
                        regist_certif.vehicle_registration_certificate_tnkb,
                        vehicle.vehicle_service_booking_number,
                        regist_certif.vehicle_registration_certificate_owner_name,
                         "", #model_variant_colour.model_variant_colour_description,
                        vehicle.vehicle_production_year ,
                        vehicle.vehicle_last_service_date,
                        vehicle.vehicle_last_km
                        # ).join(brand, pricecode.brand_id == brand.brand_id )      
                        ).join(regist_certif, vehicle.vehicle_id == regist_certif.vehicle_id
                        ).join(model_variant_colour, vehicle.vehicle_variant_id == model_variant_colour.variant_id)
     

        query_check,counter = get_the_pagination_search(db,query_set,all_params)
        query_check =  query_check.order_by(vehicle.vehicle_id).offset(page*limit).limit(limit)
        results = db.execute(query_check).all()

        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }

        # finalresults = [
        #             {
        #                 "vehicle_chassis_number": "vehicle_chassis_number",
        #                 "registration_certificate_tnkb": "registration_certificate_tnkb",
        #                 "service_booking_number": "service_booking_number",
        #                 "variant_colour_description": "variant_colour_description",
        #                 "production_year":"production_year",
        #                 "last_service_date":"last_service_date",
        #                 "last_km":"last_km"
        #             },
        #             {
        #                 "vehicle_chassis_number": "vehicle_chassis_number",
        #                 "registration_certificate_tnkb": "registration_certificate_tnkb",
        #                 "service_booking_number": "service_booking_number",
        #                 "variant_colour_description": "variant_colour_description",
        #                 "production_year":"production_year",
        #                 "last_service_date":"last_service_date",
        #                 "last_km":"last_km"
        #             }
        #                 ]

        finalresults = []
        for vehicle_chassis_number,registration_certificate_tnkb,service_booking_number,variant_colour_description,production_year, last_service_date,last_km in results:
            data = {
                "vehicle_chassis_number": vehicle_chassis_number,
                "registration_certificate_tnkb": registration_certificate_tnkb,
                "service_booking_number": service_booking_number,
                "variant_colour_description": variant_colour_description,
                "production_year":production_year,
                "last_service_date":last_service_date,
                "last_km":last_km
            }
        
            finalresults.append(data)

        return finalresults, page_results, None
    except Exception as err:
        return None, None, err     
        
    
def get_vehicle_master_by_id(id: int):
    db = get_db()
    try:
        check_query = select(MtrVehicle).where(MtrVehicle.vehicle_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
# async def get_vehicle_master_by_id(id:int):
#     db = get_db()
#     try:
#         query_set = select(MtrVehicle).where(MtrVehicle.vehicle_id==id).options(load_only(
#             MtrVehicle.vehicle_chassis_number,
#             MtrVehicle.vehicle_engine_number
#         ))
#         results = db.scalars(query_set).first()
#         return results,None
#     except Exception as err:
#         return None,err