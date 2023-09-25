from fastapi import APIRouter, HTTPException, status, Query, Request
from src.payloads.schemas.master.VillageSchema import MtrVillageGetSchema,MtrVillagePost
from src.services.master import VillageService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["village"],prefix="/api/general")

@router.get("/villages",status_code=200)
async def get_villages(page:int,limit:int,village_code:str|None=None,village_name:str|None=None,district_name:str|None=None,city_name:str|None=None,province_name:str|None=None,village_zip_code:str|None=None,city_phone_area:str|None=None,status_active:bool|None=None, sort_by:str|None=None,sort_of:str|None=None):
    get_all_params={"village_code":village_code,"village_name":village_name,"district_name":district_name,"city_name":city_name,"province_name":province_name,"village_zip_code":village_zip_code,"city_phone_area":city_phone_area,"is_active":status_active}
    sort_fields={"sort_of":sort_of,"sort_by":sort_by}

    get_results,pages,err=VillageService.get_all_villages(page,limit,get_all_params,sort_fields)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    


@router.get("/village/{village_id}",status_code=200)
async def get_village(village_id:int):
    get_result,err = VillageService.get_village(village_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200, "Success",get_result)

@router.post("/village",status_code=201)
async def post_village(req:MtrVillagePost):
    created_data,err=VillageService.post_village(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
   

@router.delete("/village/{village_id}",status_code=204)
async def delete_village(village_id:int):
    erase_village, err = VillageService.delete_village(village_id)
    if err == None:
        return payload_response(204,"Deleted",erase_village)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/village/{village_id}",status_code=202)
async def update_data(village_id:int, req:MtrVillageGetSchema):
    update_village,err= VillageService.put_village(village_id,req)
    if err == None:
        return payload_response(201,"Updated", update_village)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    

@router.patch("/village/{village_id}",status_code=202)
async def patch_village(village_id:int):
    updated_data, err = VillageService.patch_village(village_id)
    if err == None:
        return payload_response(201,"Updated", updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))