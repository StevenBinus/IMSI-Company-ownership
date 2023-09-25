from src.repositories.common import GeneralLedgerProcessRepo
from src.payloads.schemas.common import GeneralLedgerProcessSchema
from fastapi import Request

def get_general_ledger_processs_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = GeneralLedgerProcessRepo.get_general_ledger_processs_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_general_ledger_process_cruds(id:int):
    result, err = GeneralLedgerProcessRepo.get_general_ledger_process_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_general_ledger_process_cruds(req:GeneralLedgerProcessSchema.MtrGeneralLedgerProcessGetSchema,request:Request):
    created_data, err = GeneralLedgerProcessRepo.post_general_ledger_process_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_general_ledger_process_cruds(id:int,request:Request):
    updated_data, err = GeneralLedgerProcessRepo.patch_general_ledger_process_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err