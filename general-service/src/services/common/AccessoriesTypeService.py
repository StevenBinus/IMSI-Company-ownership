from src.repositories.common import AccessoriesTypeRepo
from src.payloads.schemas.common.AccessoriesTypeSchema import MtrAccessoriesTypeGetSchema
from fastapi import Request

def get_all_accessories_types(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = AccessoriesTypeRepo.get_all_accessories_types(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_accessories_type(id:int):
    result, err = AccessoriesTypeRepo.get_by_id_accessories_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_accessories_type(req:MtrAccessoriesTypeGetSchema):
    created_data, err = AccessoriesTypeRepo.post_accessories_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_accessories_type(id:int,req:MtrAccessoriesTypeGetSchema):
    updated_data, err = AccessoriesTypeRepo.put_accessories_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_accessories_type(id:int):
    erase_data, err = AccessoriesTypeRepo.delete_accessories_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_accessories_type(id:int):
    updated_data, err = AccessoriesTypeRepo.patch_accessories_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
