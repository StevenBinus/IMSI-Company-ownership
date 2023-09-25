from src.repositories.common import BrandTypeRepo
from src.payloads.schemas.common.BrandTypeSchema import MtrBrandTypeGetSchema
from fastapi import Request

def get_all_brand_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BrandTypeRepo.get_all_brand_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_brand_type(id:int):
    result, err = BrandTypeRepo.get_by_id_brand_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_brand_type(req:MtrBrandTypeGetSchema):
    created_data, err = BrandTypeRepo.post_brand_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_brand_type(id:int,req:MtrBrandTypeGetSchema):
    updated_data, err = BrandTypeRepo.put_brand_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_brand_type(id:int):
    erase_data, err = BrandTypeRepo.delete_brand_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_brand_type(id:int):
    updated_data, err = BrandTypeRepo.patch_brand_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
