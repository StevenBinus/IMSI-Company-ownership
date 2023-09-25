from src.repositories.common import ReferenceTypePurchaseRequestRepo
from src.payloads.schemas.common import ReferenceTypePurchaseRequestSchema
from fastapi import Request

def get_reference_type_purchase_requests_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = ReferenceTypePurchaseRequestRepo.get_reference_type_purchase_requests_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_reference_type_purchase_request_cruds(id:int):
    result, err = ReferenceTypePurchaseRequestRepo.get_reference_type_purchase_request_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_reference_type_purchase_request_cruds(req:ReferenceTypePurchaseRequestSchema.MtrReferenceTypePurchaseRequestGetSchema,request:Request):
    created_data, err = ReferenceTypePurchaseRequestRepo.post_reference_type_purchase_request_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_reference_type_purchase_request_cruds(id:int,request:Request):
    updated_data, err = ReferenceTypePurchaseRequestRepo.patch_reference_type_purchase_request_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err