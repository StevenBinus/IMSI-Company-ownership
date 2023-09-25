from src.repositories.common import OrderStatusRepo
from src.payloads.schemas.common.OrderStatusSchema import MtrOrderStatusGetSchema
from fastapi import Request

def get_order_statuss_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = OrderStatusRepo.get_order_statuss_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_order_status_cruds(id:int):
    result, err = OrderStatusRepo.get_order_status_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_order_status_cruds(req:MtrOrderStatusGetSchema,request:Request):
    created_data, err = OrderStatusRepo.post_order_status_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_order_status_cruds(id:int,request:Request):
    updated_data, err = OrderStatusRepo.patch_order_status_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err