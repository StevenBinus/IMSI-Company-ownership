from src.repositories.common import ClosingCheckTypeRepo
from src.payloads.schemas.common.ClosingCheckTypeSchema import MtrClosingCheckTypeGetSchema
from fastapi import Request

def get_all_closing_check_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ClosingCheckTypeRepo.get_all_closing_check_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_closing_check_type(id:int):
    result, err = ClosingCheckTypeRepo.get_by_id_closing_check_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_closing_check_type(req:MtrClosingCheckTypeGetSchema):
    created_data, err = ClosingCheckTypeRepo.post_closing_check_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_closing_check_type(id:int,req:MtrClosingCheckTypeGetSchema):
    updated_data, err = ClosingCheckTypeRepo.put_closing_check_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_closing_check_type(id:int):
    erase_data, err = ClosingCheckTypeRepo.delete_closing_check_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_closing_check_type(id:int):
    updated_data, err = ClosingCheckTypeRepo.patch_closing_check_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
