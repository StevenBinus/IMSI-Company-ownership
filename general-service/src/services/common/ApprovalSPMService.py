from src.repositories.common import ApprovalSPMRepo
from src.payloads.schemas.common.ApprovalSPMSchema import MtrApprovalSPMGetSchema
from fastapi import Request

def get_all_approvals_spm(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ApprovalSPMRepo.get_all_approvals_spm(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_approval_spm(id:int):
    result, err = ApprovalSPMRepo.get_by_id_approval_spm(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_approval_spm(req:MtrApprovalSPMGetSchema):
    created_data, err = ApprovalSPMRepo.post_approval_spm(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_approval_spm(id:int,req:MtrApprovalSPMGetSchema):
    updated_data, err = ApprovalSPMRepo.put_approval_spm(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_approval_spm(id:int):
    erase_data, err = ApprovalSPMRepo.delete_approval_spm(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_approval_spm(id:int):
    updated_data, err = ApprovalSPMRepo.patch_approval_spm(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
