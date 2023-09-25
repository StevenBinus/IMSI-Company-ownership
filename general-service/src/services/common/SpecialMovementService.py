from src.repositories.common import SpecialMovementRepo
from src.payloads.schemas.common.SpecialMovementSchema import MtrSpecialMovementGetSchema
from fastapi import Request

def get_all_special_movements(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = SpecialMovementRepo.get_all_special_movements(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_special_movement(id:int):
    result, err = SpecialMovementRepo.get_by_id_special_movement(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_special_movement(req:MtrSpecialMovementGetSchema):
    created_data, err = SpecialMovementRepo.post_special_movement(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_special_movement(id:int,req:MtrSpecialMovementGetSchema):
    updated_data, err = SpecialMovementRepo.put_special_movement(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_special_movement(id:int):
    erase_data, err = SpecialMovementRepo.delete_special_movement(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_special_movement(id:int):
    updated_data, err = SpecialMovementRepo.patch_special_movement(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
