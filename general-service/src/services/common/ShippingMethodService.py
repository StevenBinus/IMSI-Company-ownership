from src.repositories.common import ShippingMethodRepo
from src.payloads.schemas.common.ShippingMethodSchema import MtrShippingMethodGetSchema
from fastapi import Request

def get_all_shipping_methods(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ShippingMethodRepo.get_all_shipping_methods(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_shipping_method(id:int):
    result, err = ShippingMethodRepo.get_by_id_shipping_method(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_shipping_method(req:MtrShippingMethodGetSchema):
    created_data, err = ShippingMethodRepo.post_shipping_method(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_shipping_method(id:int,req:MtrShippingMethodGetSchema):
    updated_data, err = ShippingMethodRepo.put_shipping_method(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_shipping_method(id:int):
    erase_data, err = ShippingMethodRepo.delete_shipping_method(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_shipping_method(id:int):
    updated_data, err = ShippingMethodRepo.patch_shipping_method(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
