from src.repositories.common import GeneralLedgerAccountTypeRepo
from src.payloads.schemas.common.GeneralLedgerAccountTypeSchema import MtrGeneralLedgerAccountTypeGetSchema
from fastapi import Request

def get_all_general_ledger_account_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = GeneralLedgerAccountTypeRepo.get_all_general_ledger_account_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_general_ledger_account_type(id:int):
    result, err = GeneralLedgerAccountTypeRepo.get_by_id_general_ledger_account_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_general_ledger_account_type(req:MtrGeneralLedgerAccountTypeGetSchema):
    created_data, err = GeneralLedgerAccountTypeRepo.post_general_ledger_account_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_general_ledger_account_type(id:int,req:MtrGeneralLedgerAccountTypeGetSchema):
    updated_data, err = GeneralLedgerAccountTypeRepo.put_general_ledger_account_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_general_ledger_account_type(id:int):
    erase_data, err = GeneralLedgerAccountTypeRepo.delete_general_ledger_account_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_general_ledger_account_type(id:int):
    updated_data, err = GeneralLedgerAccountTypeRepo.patch_general_ledger_account_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
