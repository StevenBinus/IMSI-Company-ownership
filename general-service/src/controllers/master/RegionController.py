from fastapi import APIRouter,HTTPException,status, Request
from src.services.master import RegionService
from src.payloads.schemas.master.RegionSchema import MtrRegionRequest
from src.payloads.responses.PaginationResponse import pagination_response
from src.payloads.responses.GeneralResponse import payload_response
from src.exceptions.RequestException import ResponseException

from src.repositories.master import RegionRepo

router = APIRouter(tags=["Region"],prefix="/api/general")

@router.get("/region",status_code=status.HTTP_200_OK)
async def get_all_data(page:int, 
                       limit:int, 
                       region_code:str|None=None,
                       region_name:str|None=None,
                       is_active:bool|None=None,
                       sort_by:str|None=None,
                       sort_of:str|None=None):
    get_all_params = {
        "region_code":region_code,
        "region_name":region_name,
        "is_active":is_active,
    }
    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }
    
    get_results, pages, err = await RegionRepo.get_all_regions(page,limit,get_all_params,sort_params)
    if get_results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)

        

@router.get("/region/{id}",status_code=status.HTTP_200_OK)
async def get_by_id(id:int):
    get_result, err = RegionService.get_region_by_id(id)
    if get_result == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)
    
@router.get("/region-by-code/{code}",status_code=status.HTTP_200_OK)
async def get_region_on_by_code(code:str):
    result,err = RegionService.get_region_on_by_code(code)
    if result == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",result)

@router.post("/region",status_code=status.HTTP_201_CREATED)
async def create_data(req:MtrRegionRequest,request:Request):
    new_data,err = RegionRepo.post_region(req,request)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(201,"created",new_data)
    
@router.patch("/region/{id}",status_code=202)
async def patch_status_region(id:int,request:Request):
    updated_status, err = RegionService.patch_status_region(id,request)
    if err == None:
        return payload_response(202,"Updated",updated_status)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/region/",status_code=202)
async def update_region(id:int,req_data:MtrRegionRequest,request:Request):
    updated_data, err = RegionService.update_region(id,req_data,request)
    if err == None:
        return payload_response(202,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))