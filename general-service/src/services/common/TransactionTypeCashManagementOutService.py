from src.repositories.common import TransactionTypeCashManagementOutRepo
from src.payloads.schemas.common.TransactionTypeCashManagementOutSchema import MtrTransactionTypeCashManagementOutGetSchema
from fastapi import Request

def get_all_transaction_type_cash_management_outs(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TransactionTypeCashManagementOutRepo.get_all_transaction_type_cash_management_outs(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_transaction_type_cash_management_out(id:int):
    result, err = TransactionTypeCashManagementOutRepo.get_by_id_transaction_type_cash_management_out(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_transaction_type_cash_management_out(req:MtrTransactionTypeCashManagementOutGetSchema):
    created_data, err = TransactionTypeCashManagementOutRepo.post_transaction_type_cash_management_out(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_transaction_type_cash_management_out(id:int,req:MtrTransactionTypeCashManagementOutGetSchema):
    updated_data, err = TransactionTypeCashManagementOutRepo.put_transaction_type_cash_management_out(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_transaction_type_cash_management_out(id:int):
    erase_data, err = TransactionTypeCashManagementOutRepo.delete_transaction_type_cash_management_out(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_transaction_type_cash_management_out(id:int):
    updated_data, err = TransactionTypeCashManagementOutRepo.patch_transaction_type_cash_management_out(id)
    if err == None:
        return updated_data, None
    else:
        return None, err