from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import BusinessScopeService
from src.payloads.schemas.common.BusinessScopeSchema import MtrBusinessScopeGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Business Scope"],prefix="/api/general")

@router.get("/business-scopes", status_code=200)
async def get_all_business_scopes(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = BusinessScopeService.get_all_business_scopes(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/business-scope/{business_scope_id}", status_code=200)
async def get_by_id_business_scope(business_scope_id:int):
    get_result, err = BusinessScopeService.get_by_id_business_scope(business_scope_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/business-scope",status_code=201)
async def post_business_scope(req:MtrBusinessScopeGetSchema):
    created_data, err = BusinessScopeService.post_business_scope(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/business-scope/{business_scope_id}",status_code=201)
async def put_business_scope(business_scope_id:int,req:MtrBusinessScopeGetSchema):
    updated_data, err = BusinessScopeService.put_business_scope(business_scope_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/business-scope/{business_scope_id}",status_code=204)
async def delete_business_scope(business_scope_id:int):
    erase_data, err = BusinessScopeService.delete_business_scope(business_scope_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/business-scope/{business_scope_id}",status_code=201)
async def patch_business_scope(business_scope_id:int):
    updated_data, err = BusinessScopeService.patch_business_scope(business_scope_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



