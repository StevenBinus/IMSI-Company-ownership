from src.repositories.common import BusinessGroupRepo
from src.payloads.schemas.common.BusinessGroupSchema import MtrBusinessGroupGetSchema
from fastapi import Request

def get_all_business_groups(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BusinessGroupRepo.get_all_business_groups(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_business_group(id:int):
    result, err = BusinessGroupRepo.get_by_id_business_group(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_business_group(req:MtrBusinessGroupGetSchema):
    created_data, err = BusinessGroupRepo.post_business_group(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_business_group(id:int,req:MtrBusinessGroupGetSchema):
    updated_data, err = BusinessGroupRepo.put_business_group(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_business_group(id:int):
    erase_data, err = BusinessGroupRepo.delete_business_group(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_business_group(id:int):
    updated_data, err = BusinessGroupRepo.patch_business_group(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
