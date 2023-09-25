from src.repositories.common import AfterSalesAreaRepo
from src.payloads.schemas.common.AfterSalesAreaSchema import MtrAfterSalesAreaGetSchema
from fastapi import Request

def get_all_after_sales_areas(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = AfterSalesAreaRepo.get_all_after_sales_areas(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_after_sales_area(id:int):
    result, err = AfterSalesAreaRepo.get_by_id_after_sales_area(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_after_sales_area(req:MtrAfterSalesAreaGetSchema):
    created_data, err = AfterSalesAreaRepo.post_after_sales_area(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_after_sales_area(id:int,req:MtrAfterSalesAreaGetSchema):
    updated_data, err = AfterSalesAreaRepo.put_after_sales_area(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_after_sales_area(id:int):
    erase_data, err = AfterSalesAreaRepo.delete_after_sales_area(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_after_sales_area(id:int):
    updated_data, err = AfterSalesAreaRepo.patch_after_sales_area(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
