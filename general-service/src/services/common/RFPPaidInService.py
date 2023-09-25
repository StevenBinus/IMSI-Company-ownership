from src.repositories.common import RFPPaidInRepo
from src.payloads.schemas.common.RFPPaidInSchema import MtrRFPPaidInGetSchema
from fastapi import Request

def get_all_rfp_paid_ins(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = RFPPaidInRepo.get_all_rfp_paid_ins(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_rfp_paid_in(id:int):
    result, err = RFPPaidInRepo.get_by_id_rfp_paid_in(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_rfp_paid_in(req:MtrRFPPaidInGetSchema):
    created_data, err = RFPPaidInRepo.post_rfp_paid_in(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_rfp_paid_in(id:int,req:MtrRFPPaidInGetSchema):
    updated_data, err = RFPPaidInRepo.put_rfp_paid_in(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_rfp_paid_in(id:int):
    erase_data, err = RFPPaidInRepo.delete_rfp_paid_in(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_rfp_paid_in(id:int):
    updated_data, err = RFPPaidInRepo.patch_rfp_paid_in(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
