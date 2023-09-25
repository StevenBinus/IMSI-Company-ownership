from src.repositories.common import FinanceAreaRepo
from src.payloads.schemas.common.FinanceAreaSchema import MtrFinanceAreaGetSchema
from fastapi import Request

def get_all_finance_areas(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = FinanceAreaRepo.get_all_finance_areas(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_finance_area(id:int):
    result, err = FinanceAreaRepo.get_by_id_finance_area(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_finance_area(req:MtrFinanceAreaGetSchema):
    created_data, err = FinanceAreaRepo.post_finance_area(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_finance_area(id:int,req:MtrFinanceAreaGetSchema):
    updated_data, err = FinanceAreaRepo.put_finance_area(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_finance_area(id:int):
    erase_data, err = FinanceAreaRepo.delete_finance_area(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_finance_area(id:int):
    updated_data, err = FinanceAreaRepo.patch_finance_area(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
