from fastapi import APIRouter,Depends,HTTPException,status,Query
from src.payloads.responses.GeneralResponse import payload_response
from src.exceptions.RequestException import ResponseException 
from sqlalchemy.orm import Session
from src.configs.database import get_db
from sqlalchemy.exc import IntegrityError
from src.repositories.master import CountryRepo
from src.services.master import CountryService
from src.payloads.schemas.master import CountrySchema
from src.payloads.responses.PaginationResponse import pagination_response

router = APIRouter(tags=["Country"],prefix="/api/general")

@router.get("/countries",status_code=200)
async def get_all_countries(page:int,limit:int,
                            is_active:bool|None=None,
                            country_id:int|None=None,
                            country_code:str|None=None,
                            country_name:str|None=None,
                            country_language:str|None=None,
                            country_phone:str|None=None,
                            currency_id:int|None=None,
                            sort_by:str|None=None,
                            sort_of:str|None=None):
    get_all_params={
        "is_active":is_active,
        "country_id":country_id,
        "country_code":country_code,
        "country_name":country_name,
        "country_language":country_language,
        "Country_phone":country_phone,
        "currency_id":currency_id
    }
    sort_params={
        "sort_by":sort_by,
        "sort_of":sort_of
    }

    get_result,pages,err=CountryService.get_countries_cruds(page,limit,get_all_params,sort_params)
    if err ==None and get_all_countries!=[]:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    
@router.get("/country/{id}",status_code=200)
async def get_country(id:int):
    country, err = CountryService.get_country_cruds(id)
    if not country and err !=None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    else:
        return payload_response(200,"success",country)
    
@router.post("/country", status_code=201)
async def post_country(req:CountrySchema.MtrCountryRequest):
    created_data,err=CountryService.post_country_cruds(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))

@router.delete("/country/{country_id}", status_code=204)
async def delete_country(country_id:int):
    erase_country, err = CountryService.delete_country(country_id)
    if err == None:
        return payload_response(204,"Success", erase_country)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/country/{country_id}", status_code=202)
async def put_country(country_id:int,req:CountrySchema.MtrCountryRequest):
    update_data_new,err  = CountryService.put_country(country_id,req)
    if err == None:
        return payload_response(ResponseException(202), "Success",update_data_new)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))

@router.patch("/country/{country_id}", status_code=202)
async def patch_country(country_id:int):
    active_country, err  = CountryService.patch_country_cruds(country_id)
    if err == None:
        return payload_response(202,"Success",active_country)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    