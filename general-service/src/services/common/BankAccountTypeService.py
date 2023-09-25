from src.repositories.common import BankAccountTypeRepo
from src.payloads.schemas.common.BankAccountTypeSchema import MtrBankAccountTypeGetSchema
from fastapi import Request

def get_all_bank_account_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BankAccountTypeRepo.get_all_bank_account_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_bank_account_type(id:int):
    result, err = BankAccountTypeRepo.get_by_id_bank_account_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_bank_account_type(req:MtrBankAccountTypeGetSchema):
    created_data, err = BankAccountTypeRepo.post_bank_account_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_bank_account_type(id:int,req:MtrBankAccountTypeGetSchema):
    updated_data, err = BankAccountTypeRepo.put_bank_account_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_bank_account_type(id:int):
    erase_data, err = BankAccountTypeRepo.delete_bank_account_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_bank_account_type(id:int):
    updated_data, err = BankAccountTypeRepo.patch_bank_account_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
