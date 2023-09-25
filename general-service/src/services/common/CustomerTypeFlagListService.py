from src.repositories.common import CustomerTypeFlagListRepo
from src.payloads.schemas.common.CustomerTypeFlagListSchema import MtrCustomerTypeFlagListGetSchema
from fastapi import Request

def get_all_customer_type_flag_lists(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = CustomerTypeFlagListRepo.get_all_customer_type_flag_lists(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_customer_type_flag_list(id:int):
    result, err = CustomerTypeFlagListRepo.get_by_id_customer_type_flag_list(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_customer_type_flag_list(req:MtrCustomerTypeFlagListGetSchema):
    created_data, err = CustomerTypeFlagListRepo.post_customer_type_flag_list(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_customer_type_flag_list(id:int,req:MtrCustomerTypeFlagListGetSchema):
    updated_data, err = CustomerTypeFlagListRepo.put_customer_type_flag_list(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_customer_type_flag_list(id:int):
    erase_data, err = CustomerTypeFlagListRepo.delete_customer_type_flag_list(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_customer_type_flag_list(id:int):
    updated_data, err = CustomerTypeFlagListRepo.patch_customer_type_flag_list(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
