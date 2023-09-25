from src.repositories.master import CustomerVirtualAccountRepo 
from src.payloads.schemas.master import CustomerVirtualAccountSchema 
from fastapi import Request

def get_all_customer_virtual_accounts(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_result, err = CustomerVirtualAccountRepo.get_all_customer_virtual_accounts(page, limit, all_params, sort_params)
    if err == None:
        return get_data, page_result, None
    else:
        return None, None, err
    
def get_by_id_customer_virtual_account(id:int):
    result, err = CustomerVirtualAccountRepo.get_by_id_customer_virtual_account(id)
    if err == None:
        return result, None
    else:
        return None, err
    
def post_customer_virtual_account(req:CustomerVirtualAccountSchema.MtrCustomerVirtualAccountSchema):
    created_data, err = CustomerVirtualAccountRepo.post_customer_virtual_account(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def delete_customer_virtual_account(id:int):
    erase_data, err = CustomerVirtualAccountRepo.delete_customer_virtual_account(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
    
    
