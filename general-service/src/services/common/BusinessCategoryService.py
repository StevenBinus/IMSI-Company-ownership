from src.repositories.common import BusinessCategoryRepo
from src.payloads.schemas.common.BusinessCategorySchema import MtrBusinessCategoryGetSchema
from fastapi import Request

def get_all_business_categories(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BusinessCategoryRepo.get_all_business_categories(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_business_category(id:int):
    result, err = BusinessCategoryRepo.get_by_id_business_category(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_business_category(req:MtrBusinessCategoryGetSchema):
    created_data, err = BusinessCategoryRepo.post_business_category(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_business_category(id:int,req:MtrBusinessCategoryGetSchema):
    updated_data, err = BusinessCategoryRepo.put_business_category(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_business_category(id:int):
    erase_data, err = BusinessCategoryRepo.delete_business_category(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_business_category(id:int):
    updated_data, err = BusinessCategoryRepo.patch_business_category(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
