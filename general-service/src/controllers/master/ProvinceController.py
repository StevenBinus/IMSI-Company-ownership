from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.payloads.schemas.master import ProvinceSchema
from src.services.master import ProvinceService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Province"],prefix="/api/general")

@router.get("/provinces", status_code=200)
async def get_provinces(page:int,limit:int,db:Session=Depends(get_db),province_code:str|None=None,province_name:str|None=None,status_active:bool|None=None,country_id:int|None=None,country_code:str|None=None,country_name:str|None=None,sort_by:str|None=None,sort_of:str|None=None):
    get_all_results={"province_code":province_code,"province_name":province_name,"country_id":country_id,"country_code":country_code,"country_name":country_name,"is_active":status_active}
    sort_fields={"sort_by":sort_by,"sort_of":sort_of}

    get_results,pages,err= await ProvinceService.get_provinces_all(db, page,limit,get_all_results,sort_fields)
    if get_results!=[] and err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/province/{province}", status_code=200)
async def get_province(province_id:int, db:Session=Depends(get_db)):
    get_province_by_id,err= await ProvinceService.get_province_cruds(province_id, db)
    if err == None:
        return payload_response(200,"Success",get_province_by_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.post("/province", status_code=201)
async def post_provinces(req:ProvinceSchema.MtrProvincePost, db:Session=Depends(get_db)):
    post_province,err= await ProvinceService.post_province_cruds(req, db)
    if err == None:
        return payload_response(201,"Created",post_province)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/province/{province_id}", status_code=204)
async def delete_province(province_id:int, db:Session=Depends(get_db)):
    del_province,err=await ProvinceService.delete_province(province_id, db)
    if err == None:
        return payload_response(204,"Deleted",del_province)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))

@router.put("/province/{province_id}", status_code=202)
async def put_province(province_id:int,req:ProvinceSchema.MtrProvincePost, db:Session=Depends(get_db)):
    update_province,err= await ProvinceService.put_province(province_id,req, db)
    if err == None:
        return payload_response(202,"Updated",update_province)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
 
@router.patch("/province/{province_id}", status_code=202)
async def patch_province(province_id:int, db:Session=Depends(get_db)):
    updates_province,err= await ProvinceService.patch_province_cruds(province_id, db)
    if err == None:
        return payload_response(202,"Updated",updates_province)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))