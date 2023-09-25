from fastapi import APIRouter, HTTPException, status, Query, Request
from src.payloads.schemas.common.WorkOrderTypeSchema import MtrWorkOrderTypeGetSchema
from src.services.common import WorkOrderTypeService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException


router = APIRouter(tags=["Work Order Type"],prefix="/api/general")

@router.get("/work-order-types", status_code=200)
def get_all_work_order_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = WorkOrderTypeService.get_all_work_order_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))


@router.get("/work-order-type/{work_order_type_id}", status_code=200)
def get_work_order_type(work_order_type_id:int):
    get_result, err = WorkOrderTypeService.get_work_order_type(work_order_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)


@router.post("/work-order-type", status_code=201)
def post_work_order_type(req:MtrWorkOrderTypeGetSchema):
    created_data, err = WorkOrderTypeService.post_work_order_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/work-order-type/{work_order_type_id}", status_code=204)
async def delete_work_order_type(work_order_type_id:int):
    erase_data, err = WorkOrderTypeService.delete_work_order_type(work_order_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/work-order-type/{work_order_type_id}", status_code=202)
async def put_work_order_type(work_order_type_id:int,req:MtrWorkOrderTypeGetSchema):
    updated_data, err = WorkOrderTypeService.put_work_order_type(work_order_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/work-order-type/{work_order_type_id}", status_code=202)
def patch_work_order_type(work_order_type_id:int):
    updated_data, err = WorkOrderTypeService.patch_work_order_type(work_order_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))