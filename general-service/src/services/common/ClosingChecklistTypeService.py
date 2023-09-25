from src.repositories.common import ClosingChecklistTypeRepo
from src.payloads.schemas.common.ClosingChecklistTypeSchema import MtrClosingChecklistTypeGetSchema
from fastapi import Request

def get_all_closing_checklist_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ClosingChecklistTypeRepo.get_all_closing_checklist_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_closing_checklist_type(id:int):
    result, err = ClosingChecklistTypeRepo.get_by_id_closing_checklist_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_closing_checklist_type(req:MtrClosingChecklistTypeGetSchema):
    created_data, err = ClosingChecklistTypeRepo.post_closing_checklist_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_closing_checklist_type(id:int,req:MtrClosingChecklistTypeGetSchema):
    updated_data, err = ClosingChecklistTypeRepo.put_closing_checklist_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_closing_checklist_type(id:int):
    erase_data, err = ClosingChecklistTypeRepo.delete_closing_checklist_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_closing_checklist_type(id:int):
    updated_data, err = ClosingChecklistTypeRepo.patch_closing_checklist_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
