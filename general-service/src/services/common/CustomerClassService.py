from src.repositories.common import CustomerClassRepo
from src.payloads.schemas.common.CustomerClassSchema import MtrCustomerClassGetSchema
from fastapi import Request

def get_all_customers_class(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = CustomerClassRepo.get_all_customers_class(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_customer_class(id:int):
    result, err = CustomerClassRepo.get_by_id_customer_class(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_customer_class(req:MtrCustomerClassGetSchema):
    created_data, err = CustomerClassRepo.post_customer_class(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_customer_class(id:int,req:MtrCustomerClassGetSchema):
    updated_data, err = CustomerClassRepo.put_customer_class(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_customer_class(id:int):
    erase_data, err = CustomerClassRepo.delete_customer_class(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_customer_class(id:int):
    updated_data, err = CustomerClassRepo.patch_customer_class(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
