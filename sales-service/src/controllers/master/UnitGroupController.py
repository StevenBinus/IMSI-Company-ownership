from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.master import UnitGroupService
from src.payloads.schemas.master.UnitGroupSchema import UnitGroupRequest
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Master : Unit Group"],prefix="/api/sales")

@router.get("/unit-group",status_code=status.HTTP_200_OK)
async def get_unit_group_all(page:int, 
                             limit:int, 
                             unit_group_code:str|None=None,
                             unit_group_name:str|None=None,
                             is_active:bool|None=None,
                             sort_by:str|None=None,
                             sort_of:str|None=None,
                             db:Session=Depends(get_db)):
    all_params = {
        "unit_group_code":unit_group_code,
        "unit_group_name":unit_group_name,
        "is_active":is_active
    }
    sort_params = {
        "sort_by" : sort_by,
        "sort_of" : sort_of
    }
    get_results, pages, err = await UnitGroupService.get_unit_group_all(db,page,limit,all_params,sort_params)
    if get_results == [] and err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)

@router.get("/unit-group/{id}",status_code=status.HTTP_200_OK)
async def get_unit_group_by_id(id:int,db:Session=Depends(get_db)):
    get_result, err = await UnitGroupService.get_unit_group_by_id(db,id)
    if err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(status_code=status.HTTP_200_OK,message="success",data=get_result)

@router.post("/unit-group",status_code=status.HTTP_201_CREATED)
async def post_unit_group(req:UnitGroupRequest,db:Session=Depends(get_db)):
    created_data, err = await UnitGroupService.post_unit_group(db,req)
    if err != None:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(201,"created",created_data)

@router.put("/unit-group",status_code=status.HTTP_201_CREATED)
async def put_unit_group(id:int,req:UnitGroupRequest, db:Session=Depends(get_db)):
    updated_data, err = await UnitGroupService.update_unit_group(db,id,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_201_CREATED,detail=ResponseException(409))
    return payload_response(201,"updated",updated_data)

@router.patch("/unit-group",status_code=status.HTTP_201_CREATED)
async def patch_unit_group_status(id:int, db:Session=Depends(get_db)):
    active_status, err = await UnitGroupService.patch_unit_group_status(db,id)
    if err != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    return payload_response(201,"updated",active_status)