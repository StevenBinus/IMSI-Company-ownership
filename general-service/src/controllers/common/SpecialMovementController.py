from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import SpecialMovementService
from src.payloads.schemas.common.SpecialMovementSchema import MtrSpecialMovementGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Special Movement"],prefix="/api/general")

@router.get("/special-movements", status_code=200)
async def get_all_special_movements(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = SpecialMovementService.get_all_special_movements(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/special-movement/{special_movement_id}", status_code=200)
async def get_by_id_special_movement(special_movement_id:int):
    get_result, err = SpecialMovementService.get_by_id_special_movement(special_movement_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/special-movement",status_code=201)
async def post_special_movement(req:MtrSpecialMovementGetSchema):
    created_data, err = SpecialMovementService.post_special_movement(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/special-movement/{special_movement_id}",status_code=201)
async def put_special_movement(special_movement_id:int,req:MtrSpecialMovementGetSchema):
    updated_data, err = SpecialMovementService.put_special_movement(special_movement_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/special-movement/{special_movement_id}",status_code=204)
async def delete_special_movement(special_movement_id:int):
    erase_data, err = SpecialMovementService.delete_special_movement(special_movement_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/special-movement/{special_movement_id}",status_code=201)
async def patch_special_movement(special_movement_id:int):
    updated_data, err = SpecialMovementService.patch_special_movement(special_movement_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))