from src.repositories.common import VoidTransactionRepo
from src.payloads.schemas.common.VoidTransactionSchema import MtrVoidTransactionGetSchema
from fastapi import Request

def get_all_void_transactions(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = VoidTransactionRepo.get_all_void_transactions(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_void_transaction(id:int):
    result, err = VoidTransactionRepo.get_void_transaction(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_void_transaction(req:MtrVoidTransactionGetSchema):
    created_data, err = VoidTransactionRepo.post_void_transaction(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_void_transaction(id:int):
    updated_data, err = VoidTransactionRepo.patch_void_transaction(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_void_transaction(id:int,req:MtrVoidTransactionGetSchema):
    updated_data, err = VoidTransactionRepo.put_void_transaction(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_void_transaction_type(id:int):
    erase_data, err = VoidTransactionRepo.delete_void_transaction(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_void_transaction_type(id:int):
    updated_data, err = VoidTransactionRepo.patch_void_transaction(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
