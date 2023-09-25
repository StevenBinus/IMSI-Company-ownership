from src.repositories.common import ApprovalCodeRepo
from src.payloads.schemas.common.ApprovalCodeSchema import MtrApprovalCodeGetSchema
from fastapi import Request

def get_all_approval_codes(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ApprovalCodeRepo.get_all_approval_codes(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_approval_code(id:int):
    result, err = ApprovalCodeRepo.get_by_id_approval_code(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_approval_code(req:MtrApprovalCodeGetSchema):
    created_data, err = ApprovalCodeRepo.post_approval_code(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_approval_code(id:int,req:MtrApprovalCodeGetSchema):
    updated_data, err = ApprovalCodeRepo.put_approval_code(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_approval_code(id:int):
    erase_data, err = ApprovalCodeRepo.delete_approval_code(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_approval_code(id:int):
    updated_data, err = ApprovalCodeRepo.patch_approval_code(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
