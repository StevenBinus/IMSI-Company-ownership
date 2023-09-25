from src.repositories.common import BusinessScopeRepo
from src.payloads.schemas.common.BusinessScopeSchema import MtrBusinessScopeGetSchema
from fastapi import Request

def get_all_business_scopes(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BusinessScopeRepo.get_all_business_scopes(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_business_scope(id:int):
    result, err = BusinessScopeRepo.get_by_id_business_scope(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_business_scope(req:MtrBusinessScopeGetSchema):
    created_data, err = BusinessScopeRepo.post_business_scope(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_business_scope(id:int,req:MtrBusinessScopeGetSchema):
    updated_data, err = BusinessScopeRepo.put_business_scope(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_business_scope(id:int):
    erase_data, err = BusinessScopeRepo.delete_business_scope(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_business_scope(id:int):
    updated_data, err = BusinessScopeRepo.patch_business_scope(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
