from src.repositories.common import ItemGroupRepo
from src.payloads.schemas.common import ItemGroupSchema
from fastapi import Request

def get_item_groups_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ItemGroupRepo.get_item_groups_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_item_group_cruds(id:int):
    result, err = ItemGroupRepo.get_item_group_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_item_group_cruds(req:ItemGroupSchema.MtrItemGroupGetSchema,request:Request):
    created_data, err = ItemGroupRepo.post_item_group_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_item_group_cruds(id:int,request:Request):
    updated_data, err = ItemGroupRepo.patch_item_group_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err