from src.repositories.common import AddressRepo
from src.payloads.schemas.master import AddressSchema
from fastapi import Request

def get_addresses(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = AddressRepo.get_addresses(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_address_by_id(id:int):
    result, err = AddressRepo.get_address_by_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_address(req:AddressSchema.MtrAddressRequest):
    created_data, err = AddressRepo.post_address(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_address(id:int,request:Request):
    updated_data, err = AddressRepo.patch_address(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err
    

def put_address(id:int, req:AddressSchema.MtrAddressUpdate):
    update_data,err =  AddressRepo.put_address(id,req)
    if err == None:
        return update_data,None
    else:
        return None,err
    
def delete_address(id:int):
    delete_data , err = AddressRepo.delete_address(id)
    if err == None:
        return delete_data,None
    else:
        return None, err