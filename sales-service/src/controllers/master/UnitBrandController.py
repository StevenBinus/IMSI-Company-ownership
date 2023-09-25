from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.payloads.schemas.master.UnitBrandSchema import UnitBrandRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
import src.services.master.UnitBrandService as UnitBrandService

router = APIRouter(tags=["Master : Unit Brand"],prefix="/api/sales")

@router.get("/unit-brand", status_code=status.HTTP_200_OK)
async def get_unit_brand_all(page:int, limit:int,                   
                             brand_code:str|None=None,
                             brand_name:str|None=None,
                             is_active:bool|None=None,
                             sort_by:str|None=None,
                             sort_of:str|None=None,
                             db:Session=Depends(get_db)):
    
    all_params = {
        "brand_code":brand_code,
        "brand_name":brand_name,
        "is_active":is_active
    }

    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }

    get_results, pages, err = await UnitBrandService.get_unit_brand_all(db,page,limit,all_params,sort_params)
    if get_results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)

@router.get("/unit-brand/drop-down", status_code=status.HTTP_200_OK)
async def get_unit_brand_drop_down(db:Session=Depends(get_db)):
    results, err = await UnitBrandService.get_unit_brand_drop_down(db)
    if results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",results)  
    
@router.get("/unit-brand/{id}", status_code=status.HTTP_200_OK)
async def get_unit_brand_by_id(id:int,db:Session=Depends(get_db)):
    get_result, err = await UnitBrandService.get_unit_brand_by_id(db,id)
    if get_result == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.get("/unit-brand-multi-id/{brand_idstr}")
async def get_unit_brand_multi_id(brand_idstr:str,db:Session=Depends(get_db)):
    results, err = await UnitBrandService.get_unit_brand_multi_id(db,brand_idstr)
    if results == None or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    return payload_response(200,"Success",results)
        
@router.post("/unit-brand",status_code=status.HTTP_201_CREATED)
async def post_unit_brand(req:UnitBrandRequest,db:Session=Depends(get_db)):
    created_data, err = await UnitBrandService.post_unit_brand(db,req)
    if err != None:
       raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(201,"Created",created_data)
    
@router.put("/unit-brand/{id}", status_code=status.HTTP_200_OK)
async def update_unit_brand(id:int, req:UnitBrandRequest, db:Session=Depends(get_db)):
    updated_data,err = await UnitBrandService.update_unit_brand(db,id,req)
    if err != None:
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return payload_response(200,"Updated",updated_data)

@router.patch("/unit-brand",status_code=status.HTTP_200_OK)
async def patch_unit_brand(id:int, db:Session=Depends(get_db)):
    updated_data, err = await UnitBrandService.patch_unit_brand(db,id)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(200,"Updated",updated_data)        