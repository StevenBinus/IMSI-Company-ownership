from src.repositories.common import BusinessTypeRepo
from src.payloads.schemas.common.BusinessTypeSchema import MtrBusinessTypeGetSchema
from fastapi import Request

def get_all_business_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BusinessTypeRepo.get_all_business_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_business_type(id:int):
    result, err = BusinessTypeRepo.get_by_id_business_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_business_type(req:MtrBusinessTypeGetSchema):
    created_data, err = BusinessTypeRepo.post_business_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_business_type(id:int,req:MtrBusinessTypeGetSchema):
    updated_data, err = BusinessTypeRepo.put_business_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_business_type(id:int):
    erase_data, err = BusinessTypeRepo.delete_business_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_business_type(id:int):
    updated_data, err = BusinessTypeRepo.patch_business_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
