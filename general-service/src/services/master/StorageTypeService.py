from src.repositories.master import StorageTypeRepo
from src.payloads.schemas.master.StorageTypeSchema import MtrStorageTypeRequest, MtrStorageTypeUpdateRequest
from fastapi import Request


def get_storage_type_list(page:int,limit:int, all_params: dict(), sort_params: dict()):
    get_data, page_results, err = StorageTypeRepo.get_storage_type_list(page,limit,all_params, sort_params)
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def post_storage_type(req:MtrStorageTypeRequest):
    created_data, err = StorageTypeRepo.post_storage_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def get_storage_type_by_id(id:int):
    result, err = StorageTypeRepo.get_storage_type_by_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def patch_storage_type(id:int):
    updated_data, err = StorageTypeRepo.patch_storage_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def update_storage_type(id: int, req:MtrStorageTypeUpdateRequest):
    updated_data, err = StorageTypeRepo.update_storage_type(id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err