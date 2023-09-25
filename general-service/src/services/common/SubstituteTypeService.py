from src.repositories.common import SubstituteTypeRepo
from src.payloads.schemas.common.SubstituteTypeSchema import MtrSubstituteTypeGetSchema
from fastapi import Request

def get_all_substitute_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = SubstituteTypeRepo.get_all_substitute_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_substitute_type(id:int):
    result, err = SubstituteTypeRepo.get_by_id_substitute_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_substitute_type(req:MtrSubstituteTypeGetSchema):
    created_data, err = SubstituteTypeRepo.post_substitute_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_substitute_type(id:int,req:MtrSubstituteTypeGetSchema):
    updated_data, err = SubstituteTypeRepo.put_substitute_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_substitute_type(id:int):
    erase_data, err = SubstituteTypeRepo.delete_substitute_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_substitute_type(id:int):
    updated_data, err = SubstituteTypeRepo.patch_substitute_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err