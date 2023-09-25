from src.repositories.common import ApprovalStatusRepo
from src.payloads.schemas.common.ApprovalStatusSchema import MtrApprovalStatusGetSchema
from fastapi import Request

def get_all_approvals_status(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ApprovalStatusRepo.get_all_approvals_status(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_approval_status(id:int):
    result, err = ApprovalStatusRepo.get_by_id_approval_status(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_approval_status(req:MtrApprovalStatusGetSchema):
    created_data, err = ApprovalStatusRepo.post_approval_status(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_approval_status(id:int,req:MtrApprovalStatusGetSchema):
    updated_data, err = ApprovalStatusRepo.put_approval_status(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_approval_status(id:int):
    erase_data, err = ApprovalStatusRepo.delete_approval_status(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_approval_status(id:int):
    updated_data, err = ApprovalStatusRepo.patch_approval_status(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
