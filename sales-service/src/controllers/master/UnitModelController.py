from fastapi import APIRouter, HTTPException, status, Depends
from src.configs.database import get_db
from sqlalchemy.orm import Session
from src.services.master import UnitModelService
from src.payloads.schemas.master.UnitModelSchema import MtrUnitModelRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Master : Unit Model"],prefix="/api/sales")

@router.get("/unit-model")
async def get_unitmodels(page:int,
                         limit:int,
                         model_code:str|None=None,
                         model_description:str|None=None,
                         is_active:bool|None=None,
                         sort_by:str|None=None,
                         sort_of:str|None=None,
                         db:Session=Depends(get_db)):

    all_params = {
        "model_code":model_code,
        "model_description":model_description,
        "is_active":is_active
    }

    sort_params = {
        "sort_by":sort_by,
        "sort_of":sort_of
    }

    results,pages,err = await UnitModelService.get_unit_model_list_all(db,page,limit,all_params,sort_params)
    if results == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],results)
    
@router.get("/unit-model/drop-down/{brand_id}")
async def get_unit_model_drop_down(brand_id:int,db:Session=Depends(get_db)):
    results, err = await UnitModelService.get_unit_model_drop_down(db,brand_id)
    if results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(err))
    return payload_response(200,"Success",results)  

@router.get("/unit-model/{id}")
async def get_unit_model_by_id(id:int,db:Session=Depends(get_db)):
    result, err = await UnitModelService.get_unit_model_by_id(db,id)
    if result == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",result)

@router.post("/unit-model")
async def post_unit_model(req:MtrUnitModelRequest,db:Session=Depends(get_db)):
    created_data, err = await UnitModelService.post_unit_model(db,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(201,"Created",created_data)
        
@router.patch("/unit-model")
async def patch_unit_model(id:int,db:Session=Depends(get_db)):
    active_status, err = await UnitModelService.patch_unit_model(db,id)
    if err != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return payload_response(201,"updated",active_status)