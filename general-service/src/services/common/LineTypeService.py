from src.repositories.common import LineTypeRepo
from src.payloads.schemas.common import LineTypeSchema
from fastapi import Request

def get_line_types_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = LineTypeRepo.get_line_types_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_line_type_cruds(id:int):
    result, err = LineTypeRepo.get_line_type_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_line_type_cruds(req:LineTypeSchema.MtrLineTypeGetSchema,request:Request):
    created_data, err = LineTypeRepo.post_line_type_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_line_type_cruds(id:int,request:Request):
    updated_data, err = LineTypeRepo.patch_line_type_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err