from src.repositories.common import AdjustmentReasonRepo
from src.payloads.schemas.common.AdjustmentReasonSchema import MtrAdjustmentReasonGetSchema
from fastapi import Request

def get_all_adjustment_reasons(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = AdjustmentReasonRepo.get_all_adjustment_reasons(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_adjustment_reason(id:int):
    result, err = AdjustmentReasonRepo.get_by_id_adjustment_reason(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_adjustment_reason(req:MtrAdjustmentReasonGetSchema):
    created_data, err = AdjustmentReasonRepo.post_adjustment_reason(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_adjustment_reason(id:int,req:MtrAdjustmentReasonGetSchema):
    updated_data, err = AdjustmentReasonRepo.put_adjustment_reason(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_adjustment_reason(id:int):
    erase_data, err = AdjustmentReasonRepo.delete_adjustment_reason(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_adjustment_reason(id:int):
    updated_data, err = AdjustmentReasonRepo.patch_adjustment_reason(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
