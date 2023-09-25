from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import BusinessGroupService
from src.payloads.schemas.common.BusinessGroupSchema import MtrBusinessGroupGetSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Business Group"],prefix="/api/general")

@router.get("/business-groups", status_code=200)
async def get_all_business_groups(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = BusinessGroupService.get_all_business_groups(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/business-group/{business_group_id}", status_code=200)
async def get_by_id_business_group(business_group_id:int):
    get_result, err = BusinessGroupService.get_by_id_business_group(business_group_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/business-group",status_code=201)
async def post_business_group(req:MtrBusinessGroupGetSchema):
    created_data, err = BusinessGroupService.post_business_group(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/business-group/{business_group_id}",status_code=201)
async def put_business_group(business_group_id:int,req:MtrBusinessGroupGetSchema):
    updated_data, err = BusinessGroupService.put_business_group(business_group_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/business-group/{business_group_id}",status_code=204)
async def delete_business_group(business_group_id:int):
    erase_data, err = BusinessGroupService.delete_business_group(business_group_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/business-group/{business_group_id}",status_code=201)
async def patch_business_group(business_group_id:int):
    updated_data, err = BusinessGroupService.patch_business_group(business_group_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    



