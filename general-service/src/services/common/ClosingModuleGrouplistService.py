from src.repositories.common import ClosingModuleGrouplistRepo
from src.payloads.schemas.common.ClosingModuleGrouplistSchema import MtrClosingModuleGrouplistGetSchema
from fastapi import Request

def get_all_closing_module_grouplists(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ClosingModuleGrouplistRepo.get_all_closing_module_grouplists(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_closing_module_grouplist(id:int):
    result, err = ClosingModuleGrouplistRepo.get_by_id_closing_module_grouplist(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_closing_module_grouplist(req:MtrClosingModuleGrouplistGetSchema):
    created_data, err = ClosingModuleGrouplistRepo.post_closing_module_grouplist(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_closing_module_grouplist(id:int,req:MtrClosingModuleGrouplistGetSchema):
    updated_data, err = ClosingModuleGrouplistRepo.put_closing_module_grouplist(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_closing_module_grouplist(id:int):
    erase_data, err = ClosingModuleGrouplistRepo.delete_closing_module_grouplist(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_closing_module_grouplist(id:int):
    updated_data, err = ClosingModuleGrouplistRepo.patch_closing_module_grouplist(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
