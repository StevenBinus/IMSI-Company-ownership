from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import DistrictService
from src.repositories.master import DistrictRepo
from src.payloads.schemas.master import DistrictSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException


router = APIRouter(tags=["District"],prefix="/api/general")


@router.get("/districts",status_code=200)
async def get_all_districts(page:int,limit:int,
                            is_active:bool|None=None,
                            district_code:str|None=None,
                            district_name:str|None=None,
                            city_code:str|None=None,
                            city_name:str|None=None,
                            province_code:str|None=None,
                            province_name:str|None=None,
                            sort_of:str|None=None,
                            sort_by:str|None=None
                            ):
    get_all_result = {
        "is_active":is_active,
        "district_code":district_code,
        "dictrict_name":district_name,
        "city_code":city_code,
        "city_name":city_name,
        "province_code":province_code,
        "province_name":province_name
    }
    get_sort = {"sort_of":sort_of,"sort_by":sort_by}
    get_result,pages,err=DistrictService.get_all_districts(page,limit,get_all_result,get_sort)
    if err ==None and get_result!=[]:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    
@router.get("/district/{district_id}",status_code=200)
async def get_district_by_id(district_id:int):
    get_result , err=DistrictService.get_district(district_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success", get_result)

@router.post("/district",status_code=202)
async def create_ststus_code(req:DistrictSchema.MtrDistrict):
    created_data,err=DistrictService.post_district(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/district/{district_id}",status_code=202)
async def patch_district(district_id:int):
    patched_data,err =  DistrictService.patch_district(district_id)
    if err == None:
        return payload_response(202,"Updated",patched_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/district/{district_id}",status_code=202)
async def delete_district(district_id):
    delete_data,err=DistrictService.delete_district(district_id)
    if err == None:
        return payload_response(204,"Deleted",delete_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("district/{district_id}",status_code=202)
async def update_district(district_id:int, req:DistrictSchema.MtrDistrictUpdate):
    updated_data,err = DistrictService.put_district(district_id,req)
    if err == None: 
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))