from src.repositories.common import BankTypeRepo
from src.payloads.schemas.common.BankTypeSchema import MtrBankTypeGetSchema
from fastapi import Request

def get_all_bank_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BankTypeRepo.get_all_bank_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_bank_type(id:int):
    result, err = BankTypeRepo.get_by_id_bank_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_bank_type(req:MtrBankTypeGetSchema):
    created_data, err = BankTypeRepo.post_bank_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_bank_type(id:int,req:MtrBankTypeGetSchema):
    updated_data, err = BankTypeRepo.put_bank_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_bank_type(id:int):
    erase_data, err = BankTypeRepo.delete_bank_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_bank_type(id:int):
    updated_data, err = BankTypeRepo.patch_bank_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
