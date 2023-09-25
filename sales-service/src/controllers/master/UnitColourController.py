from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.master import UnitColourService
from src.payloads.schemas.master.UnitColourSchema import UnitColourRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Master : Unit Colour"],prefix="/api/sales")

@router.get("/unit-colour")
async def get_unit_colour_list_all(page:int,
                         limit:int,
                         brand_id:int|None=None,
                         colour_code:str|None=None,
                         colour_commercial_name:str|None=None,
                         colour_police_name:str|None=None,
                         is_active:bool|None=None,
                         sort_by:str|None=None,
                         sort_of:str|None=None,
                         db:Session=Depends(get_db)):

    all_params = {
        "colour_code":colour_code,
        "colour_commercial_name":colour_commercial_name,
        "colour_police_name":colour_police_name,
        "brand_id":brand_id,
        "is_active":is_active
    }

    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }

    results,pages,err = await UnitColourService.get_unit_colour_list_all(db,page,limit,all_params,sort_params)
    if results == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],results)


@router.get("/unit-colour/{id}")
async def get_unit_colour_by_id(id:int,db:Session=Depends(get_db)):
    result, err = await UnitColourService.get_unit_colour_by_id(db,id)
    if result == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",result)


@router.post("/unit-colour")
async def post_unit_colour(req:UnitColourRequest,db:Session=Depends(get_db)):
    created_data, err = await UnitColourService.post_unit_colour(db,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(201,"Created",created_data)
        
        
@router.patch("/unit-colour")
async def patch_unit_colour(id:int,db:Session=Depends(get_db)):
    active_status, err = await UnitColourService.patch_unit_colour(db,id)
    if err != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return payload_response(201,"updated",active_status)