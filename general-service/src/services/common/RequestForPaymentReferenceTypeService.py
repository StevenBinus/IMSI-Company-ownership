from src.repositories.common import RequestForPaymentReferenceTypeRepo
from src.payloads.schemas.common import RequestForPaymentReferenceTypeSchema
from fastapi import Request

def get_all_request_for_payment_reference_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = RequestForPaymentReferenceTypeRepo.get_all_request_for_payment_reference_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_request_for_payment_reference_type(id:int):
    result, err = RequestForPaymentReferenceTypeRepo.get_by_id_request_for_payment_reference_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_request_for_payment_reference_type(req:RequestForPaymentReferenceTypeSchema):
    created_data, err = RequestForPaymentReferenceTypeRepo.post_request_for_payment_reference_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_request_for_payment_reference_type(id:int,req:RequestForPaymentReferenceTypeSchema):
    updated_data, err = RequestForPaymentReferenceTypeRepo.put_request_for_payment_reference_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_request_for_payment_reference_type(id:int):
    erase_data, err = RequestForPaymentReferenceTypeRepo.delete_request_for_payment_reference_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_request_for_payment_reference_type(id:int):
    updated_data, err = RequestForPaymentReferenceTypeRepo.patch_request_for_payment_reference_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
