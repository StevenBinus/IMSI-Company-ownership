from src.repositories.common import BillableToRepo
from src.payloads.schemas.common.BillableToSchema import MtrBillableToGetSchema
from fastapi import Request

def get_all_billables_to(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = BillableToRepo.get_all_billables_to(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_billable_to(id:int):
    result, err = BillableToRepo.get_by_id_billable_to(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_billable_to(req:MtrBillableToGetSchema):
    created_data, err = BillableToRepo.post_billable_to(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_billable_to(id:int,req:MtrBillableToGetSchema):
    updated_data, err = BillableToRepo.put_billable_to(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_billable_to(id:int):
    erase_data, err = BillableToRepo.delete_billable_to(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_billable_to(id:int):
    updated_data, err = BillableToRepo.patch_billable_to(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
