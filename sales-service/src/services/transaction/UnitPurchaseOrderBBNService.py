from src.repositories.transaction import UnitPurchaseOrderBBNRepo
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNRequest, TrxUnitPurchaseOrderBBNDetailRequest, TrxUnitPurchaseOrderBBNCostDetailRequest
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNRequestUpdate
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNCostDetailRequestUpdate
from fastapi import Request

def get_unit_purchase_order_bbn_search(page:int,limit:int,all_params:dict()):
    get_data, page_results, err = UnitPurchaseOrderBBNRepo.get_unit_purchase_order_bbn_search(page,limit,all_params)
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err

def post_unit_purchase_order_bbn(req_form:TrxUnitPurchaseOrderBBNRequest):
    post_data,err = UnitPurchaseOrderBBNRepo.post_unit_purchase_order_bbn(req_form)
    if err == None:
        return post_data, None
    else:
        return post_data, err
    
def post_unit_purchase_order_bbn_detail(req_form:TrxUnitPurchaseOrderBBNDetailRequest):
    post_data,err = UnitPurchaseOrderBBNRepo.post_unit_purchase_order_bbn_detail(req_form)
    if err == None:
        return post_data, None
    else:
        return post_data, err
    
def post_unit_purchase_order_bbn_cost_detail(req_form:TrxUnitPurchaseOrderBBNCostDetailRequest):
    post_data,err = UnitPurchaseOrderBBNRepo.post_unit_purchase_order_bbn_cost_detail(req_form)
    if err == None:
        return post_data, None
    else:
        return post_data, err
    
def get_unit_purchase_order_bbn_by_id(id:int):
    get_data_header, get_data_detail, err = UnitPurchaseOrderBBNRepo.get_unit_purchase_order_bbn_by_id(id)
    if err == None:
        return get_data_header, get_data_detail, None
    else:
        return get_data_header, get_data_detail, err
    
def get_unit_purchase_order_bbn_detail_by_id(id:int):
    get_data_detail, err = UnitPurchaseOrderBBNRepo.get_unit_purchase_order_bbn_detail_by_id(id)
    if err == None:
        return get_data_detail, None
    else:
        return get_data_detail,  err
    
def get_unit_purchase_order_bbn_cost_detail_by_id(id:int):
    result, err = UnitPurchaseOrderBBNRepo.get_unit_purchase_order_bbn_cost_detail_by_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def update_unit_purchase_order_bbn(id: int, req:TrxUnitPurchaseOrderBBNRequestUpdate):
    updated_data, err = UnitPurchaseOrderBBNRepo.update_unit_purchase_order_bbn(id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def update_unit_purchase_order_bbn_cost_detail(id: int, req:TrxUnitPurchaseOrderBBNCostDetailRequestUpdate):
    updated_data, err = UnitPurchaseOrderBBNRepo.update_unit_purchase_order_bbn_cost_detail(id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_submit_unit_purchase_order_bbn_approval_status(id: int):
    updated_data, err = UnitPurchaseOrderBBNRepo.patch_submit_unit_purchase_order_bbn_approval_status(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_approve_unit_purchase_order_bbn_approval_status(id: int):
    updated_data, err = UnitPurchaseOrderBBNRepo.patch_approve_unit_purchase_order_bbn_approval_status(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_close_order_unit_purchase_order_bbn_approval_status(id: int):
    updated_data, err = UnitPurchaseOrderBBNRepo.patch_close_order_unit_purchase_order_bbn_approval_status(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_unit_purchase_order_bbn_cost_detail(id:int):
    deleted_data, err = UnitPurchaseOrderBBNRepo.delete_unit_purchase_order_bbn_cost_detail(id)
    if err == None:
        return deleted_data, None
    else:
        return None, err
    
def delete_unit_purchase_order_bbn_detail(id:int):
    deleted_data, err = UnitPurchaseOrderBBNRepo.delete_unit_purchase_order_bbn_detail(id)
    if err == None:
        return deleted_data, None
    else:
        return None, err