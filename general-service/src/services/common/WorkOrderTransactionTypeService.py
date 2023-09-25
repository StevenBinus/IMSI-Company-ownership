from src.repositories.common import WorkOrderTransactionTypeRepo
from src.payloads.schemas.common.WorkOrderTransactionTypeSchema import MtrWorkOrderTransactionTypeGetSchema
from fastapi import Request

def get_all_work_order_transaction_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = WorkOrderTransactionTypeRepo.get_all_work_order_transaction_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_work_order_transaction_type(id:int):
    result, err = WorkOrderTransactionTypeRepo.get_work_order_transaction_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_work_order_transaction_type(req:MtrWorkOrderTransactionTypeGetSchema):
    created_data, err = WorkOrderTransactionTypeRepo.post_work_order_transaction_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_work_order_transaction_type(id:int):
    updated_data, err = WorkOrderTransactionTypeRepo.patch_work_order_transaction_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_work_order_type(id:int,req:MtrWorkOrderTransactionTypeGetSchema):
    updated_data, err = WorkOrderTransactionTypeRepo.put_work_order_transaction_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_work_order_type(id:int):
    erase_data, err = WorkOrderTransactionTypeRepo.delete_work_order_transaction_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err