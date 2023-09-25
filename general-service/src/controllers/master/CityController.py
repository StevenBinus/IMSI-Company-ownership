from fastapi import APIRouter, HTTPException, status, Query, Request, Depends
from src.payloads.schemas.master.CitySchema import MtrCitySchemaByList,MtrCityUpdate
from src.repositories.master import CityRepo
from src.services.master import CityService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from src.configs.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["City"],prefix="/api/general")

@router.get("/cities",status_code=200)
async def get_cities(page:int,limit:int,is_active:bool|None=None,city_code:str|None=None,city_name:str|None=None,province_code:int|None=None,province_name:str|None=None,sort_by:str|None=None,sort_of:str|None=None, db:Session=Depends(get_db)):
    get_all_params={"city_code":city_code,"city_name":city_name,"province_code":province_code,"province_name":province_name,"is_active":is_active}
    sort_fields={"sort_by":sort_by,"sort_of":sort_of}

    get_result, pages, err= await CityRepo.get_all_cities(db, page,limit,get_all_params,sort_fields)

    if get_result!=[] or err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/city/{city_id}",status_code=200)
async def get_city(city_id:int, db:Session=Depends(get_db)):
    get_result,err = await CityService.get_city(db, city_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200, "Success",get_result)

@router.post("/city",status_code=201)
async def post_city(req:MtrCitySchemaByList, db:Session=Depends(get_db)):
    created_data,err= await CityService.post_city(db, req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
   

@router.delete("/city/{city_id}",status_code=204)
async def delete_city(city_id:int, db:Session=Depends(get_db)):
    erase_city, err = await CityService.delete_city(db, city_id)
    if err == None:
        return payload_response(204,"Deleted",erase_city)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/city/{city_id}",status_code=202)
async def update_data(city_id:int, req:MtrCityUpdate, db:Session=Depends(get_db)):
    update_city,err= await CityService.put_city(db, city_id,req)
    if err == None:
        return payload_response(201,"Updated", update_city)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    

@router.patch("/city/{city_id}",status_code=202)
async def patch_city(city_id:int, db:Session=Depends(get_db)):
    updated_data, err = await CityService.patch_City(db, city_id)
    if err == None:
        return payload_response(201,"Updated", updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))