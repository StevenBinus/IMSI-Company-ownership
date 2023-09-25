from src.repositories.common import TransactionTypeRepo
from src.payloads.schemas.common.TransactionTypeSchema import MtrTransactionTypeGetSchema
from fastapi import Request


def get_all_transaction_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TransactionTypeRepo.get_all_transaction_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_transaction_type(id:int):
    result, err = TransactionTypeRepo.get_by_id_transaction_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_transaction_type(req:MtrTransactionTypeGetSchema):
    created_data, err = TransactionTypeRepo.post_transaction_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_transaction_type(id:int,req:MtrTransactionTypeGetSchema):
    updated_data, err = TransactionTypeRepo.put_transaction_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_transaction_type(id:int):
    erase_data, err = TransactionTypeRepo.delete_transaction_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_transaction_type(id:int):
    updated_data, err = TransactionTypeRepo.patch_transaction_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err