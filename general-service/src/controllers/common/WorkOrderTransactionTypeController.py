from fastapi import APIRouter,Depends,HTTPException,status,Query
from src.repositories.common import WorkOrderTransactionTypeRepo
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.common import WorkOrderTransactionTypeSchema
from src.payloads.schemas.common.WorkOrderTransactionTypeSchema import MtrWorkOrderTransactionTypeGetSchema
from src.services.common import WorkOrderTransactionTypeService
from src.payloads.responses.PaginationResponse import pagination_response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads.responses.GeneralResponse import payload_response

router = APIRouter(tags=["Work Order Transaction Type"],prefix="/api/general")

@router.get("/work-order-transaction-types", status_code=200)
def get_all_work_order_transaction_types(page:int, limit:int, query_of:list[str]=Query(None), query_by:list[str]=Query(None)):
    get_results, pages, err = WorkOrderTransactionTypeService.get_all_work_order_transaction_types(page,limit,query_of,query_by)
    if err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))


@router.get("/work-order-transaction-type/{work_order_transaction_type_id}", status_code=200)
async def get_by_id_work_order_transaction_type(work_order_ransaction_type_id:int):
    get_result, err = WorkOrderTransactionTypeService.get_work_order_transaction_type(work_order_ransaction_type_id)
    if not get_result and err == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success",get_result)

@router.post("/work-order-transaction-type", status_code=201)
def post_work_order_transaction_type(req:MtrWorkOrderTransactionTypeGetSchema):
    created_data, err = WorkOrderTransactionTypeService.post_work_order_transaction_type(req)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/work-order-transaction-type/{work_order_transaction_type_id}", status_code=204)
def delete_work_order_transaction_type(work_order_transaction_type_id:int):
    erase_data, err = WorkOrderTransactionTypeService.delete_work_order_type(work_order_transaction_type_id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/work-order-transaction-type/{work_order_transaction_type_id}", status_code=202)
def put_work_order_transaction_type(work_order_transaction_type_id:int,req:MtrWorkOrderTransactionTypeGetSchema):
    updated_data, err = WorkOrderTransactionTypeService.put_work_order_type(work_order_transaction_type_id,req)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/work-order-transaction-type/{work_order_transaction_type_id}", status_code=202)
def patch_work_order_transaction_type(work_order_transaction_type_id:int):
    updated_data, err = WorkOrderTransactionTypeService.patch_work_order_transaction_type(work_order_transaction_type_id)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))