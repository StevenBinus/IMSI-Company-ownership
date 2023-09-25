from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import VehicleMasterService
from src.payloads.schemas.master.VehicleMasterSchema import VehicleMasterRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

from datetime import datetime

router = APIRouter(tags=["Master : Vehicle Master"],prefix="/api/sales")

@router.get("/vehicle-master", status_code=status.HTTP_200_OK)
async def get_all(page:int,limit:int,
                  vehicle_chassis_number:str|None=None,
                  vehicle_registration_certificate_tnkb:str|None=None,
                  vehicle_service_booking_number:str|None=None,
                  vehicle_registration_certificate_owner_name:str|None=None,
                  model_variant_colour_description:str|None=None,
                  vehicle_production_year:int|None=None,
                  vehicle_last_service_date:datetime|None=None,
                  vehicle_last_km:str|None=None
                  
                  ):

    get_all_params = {
        "vehicle_chassis_number": vehicle_chassis_number,
        "vehicle_registration_certificate_tnkb": vehicle_registration_certificate_tnkb,
        "vehicle_service_booking_number": vehicle_service_booking_number,
        "vehicle_registration_certificate_owner_name": vehicle_registration_certificate_owner_name,
        "model_variant_colour_description":model_variant_colour_description,
        "vehicle_production_year":vehicle_production_year,
        "vehicle_last_service_date":vehicle_last_service_date,
        "vehicle_last_km":vehicle_last_km
    }

    get_results, pages, err = VehicleMasterService.get_vehicle_master_search(page,limit,get_all_params)
    if err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    
    else:
        return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
  
  
@router.get("/vehicle-master/{id}", status_code=status.HTTP_200_OK)
async def get_tpt_master_by_id(id:int):
    result, err = VehicleMasterService.get_vehicle_master_by_id(id)
    # if not get_result and err == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    # return payload_response(200,"success",get_result)
    if result == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))    
    return payload_response(200,"Success",result)
    
