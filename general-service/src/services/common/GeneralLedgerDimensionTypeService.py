from src.repositories.common import GeneralLedgerDimensionTypeRepo
from src.payloads.schemas.common import GeneralLedgerDimensionTypeSchema
from fastapi import Request

def get_general_ledger_dimension_types_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = GeneralLedgerDimensionTypeRepo.get_general_ledger_dimension_types_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_general_ledger_dimension_type_cruds(id:int):
    result, err = GeneralLedgerDimensionTypeRepo.get_general_ledger_dimension_type_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_general_ledger_dimension_type_cruds(req:GeneralLedgerDimensionTypeSchema.MtrGeneralLedgerDimensionTypeGetSchema,request:Request):
    created_data, err = GeneralLedgerDimensionTypeRepo.post_general_ledger_dimension_type_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_general_ledger_dimension_type_cruds(id:int,request:Request):
    updated_data, err = GeneralLedgerDimensionTypeRepo.patch_general_ledger_dimension_type_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err