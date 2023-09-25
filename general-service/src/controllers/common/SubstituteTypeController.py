from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import SubstituteTypeService
from src.payloads.schemas.common.SubstituteTypeSchema import MtrSubstituteTypeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Substitute Type"],prefix="/api/general")

@router.get("/substitute-types", status_code=200)
async def get_all_substitute_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = SubstituteTypeService.get_all_substitute_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/substitute-type/{substitute_type_id}", status_code=200)
async def get_by_id_substitute_type(substitute_type_id:int):
    get_result, err = SubstituteTypeService.get_by_id_substitute_type(substitute_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/substitute-type",status_code=201)
async def post_substitute_type(req:MtrSubstituteTypeGetSchema):
    created_data, err = SubstituteTypeService.post_substitute_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/substitute-type/{substitute_type_id}",status_code=201)
async def put_substitute_type(substitute_type_id:int,req:MtrSubstituteTypeGetSchema):
    updated_data, err = SubstituteTypeService.put_substitute_type(substitute_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/substitute-type/{substitute_type_id}",status_code=204)
async def delete_substitute_type(substitute_type_id:int):
    erase_data, err = SubstituteTypeService.delete_substitute_type(substitute_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/substitute-type/{substitute_type_id}",status_code=201)
async def patch_substitute_type(substitute_type_id:int):
    updated_data, err = SubstituteTypeService.patch_substitute_type(substitute_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    