from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.transaction import UnitPurchaseOrderBBNService
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNRequest, TrxUnitPurchaseOrderBBNDetailRequest, TrxUnitPurchaseOrderBBNCostDetailRequest, TrxUnitPurchaseOrderBBNResponse
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNRequestUpdate
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNCostDetailRequestUpdate
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNDetailResponse
from src.payloads.responses.CommonResponse import payload_response,payload_response_detail
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from datetime import datetime

router = APIRouter(tags=["Transaction : Unit Purchase Order BBN"],prefix="/api/sales")

@router.get("/unit-purchase-order-bbn", status_code=status.HTTP_200_OK)
async def get_unit_purchase_order_bbn_search(
    page:int, 
    limit:int,
    purchase_order_bbn_document_number:str|None=None,
    purchase_order_date_from:datetime|None=None,
    purchase_order_date_to:datetime|None=None,
    brand_id:int|None=None,
    supplier_id:int|None=None,
    vehicle_id:int|None=None,
    order_status_id:int|None=None
    ):
        get_all_params = {"purchase_order_bbn_document_number":purchase_order_bbn_document_number,
                    "purchase_order_date_from":purchase_order_date_from,
                    "purchase_order_date_to": purchase_order_date_to,
                    "brand_id":brand_id,
                    "supplier_id":supplier_id,
                    "vehicle_id":vehicle_id,
                    "order_status_id":order_status_id,
        }

        get_results, pages, err = UnitPurchaseOrderBBNService.get_unit_purchase_order_bbn_search(page,limit,get_all_params)
                                                                                                      
        if not get_results or err != None:
            raise HTTPException(status_code=404, detail=ResponseException(404))   
        else:
            return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)

@router.post("/unit-purchase-order-bbn",status_code=status.HTTP_201_CREATED)
async def post_unit_purchase_order_bbn(req_data:TrxUnitPurchaseOrderBBNRequest):
    created_data, err = UnitPurchaseOrderBBNService.post_unit_purchase_order_bbn(req_data)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409))
    
@router.post("/unit-purchase-order-bbn-detail",status_code=status.HTTP_201_CREATED)
async def post_unit_purchase_order_bbn_detail(req_data:TrxUnitPurchaseOrderBBNDetailRequest):
    created_data, err = UnitPurchaseOrderBBNService.post_unit_purchase_order_bbn_detail(req_data)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409))
    
@router.post("/unit-purchase-order-bbn-cost-detail",status_code=status.HTTP_201_CREATED)
async def post_unit_purchase_order_bbn_cost_detail(req_data:TrxUnitPurchaseOrderBBNCostDetailRequest):
    created_data, err = UnitPurchaseOrderBBNService.post_unit_purchase_order_bbn_cost_detail(req_data)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409))
    
@router.get("/unit-purchase-order-bbn/{id}", status_code=status.HTTP_200_OK)
async def get_unit_purchase_order_bbn_by_id(id:int):
    header_result, detail_result, err = UnitPurchaseOrderBBNService.get_unit_purchase_order_bbn_by_id(id)
    if not header_result or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",TrxUnitPurchaseOrderBBNResponse(
        purchase_order_bbn_document_number=header_result.purchase_order_bbn_document_number,
        purchase_order_date=header_result.purchase_order_date,
        brand_id=header_result.brand_id,
        supplier_id=header_result.supplier_id,
        term_of_payment_id=header_result.term_of_payment_id,
        bill_code_id=header_result.bill_code_id,
        cost_center_id=header_result.cost_center_id,
        currency_id=header_result.currency_id,
        purchase_order_remark=header_result.purchase_order_remark,
        down_payment_request=header_result.down_payment_request,
        total_after_vat=header_result.total_after_vat,
        purchase_order_bbn_detail=detail_result
    ))

@router.get("/unit-purchase-order-bbn-detail/{id}", status_code=status.HTTP_200_OK)
async def get_unit_purchase_order_bbn_detail_by_id(id:int):
    detail_result, err = UnitPurchaseOrderBBNService.get_unit_purchase_order_bbn_detail_by_id(id)
    if not detail_result or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",detail_result)

@router.get("/unit-purchase-order-bbn-cost-detail/{id}", status_code=status.HTTP_200_OK)
async def get_unit_purchase_order_bbn_cost_detail_by_id(id: int):
    result, err = UnitPurchaseOrderBBNService.get_unit_purchase_order_bbn_cost_detail_by_id(id)
    if not result or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200, "success", result)

@router.put("/unit-purchase-order-bbn/{id}",status_code=status.HTTP_201_CREATED)
async def update_unit_purchase_order_bbn(id:int,req:TrxUnitPurchaseOrderBBNRequestUpdate):
    updated_data, err = UnitPurchaseOrderBBNService.update_unit_purchase_order_bbn(id, req)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/unit-purchase-order-bbn-cost-detail/{id}",status_code=status.HTTP_201_CREATED)
async def update_unit_purchase_order_bbn_cost_detail(id:int,req:TrxUnitPurchaseOrderBBNCostDetailRequestUpdate):
    updated_data, err = UnitPurchaseOrderBBNService.update_unit_purchase_order_bbn_cost_detail(id, req)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.patch("/submit-unit-purchase-order-bbn-approval-status/{id}",status_code=status.HTTP_201_CREATED)
async def patch_submit_unit_purchase_order_bbn_approval_status(id:int):
    updated_data, err = UnitPurchaseOrderBBNService.patch_submit_unit_purchase_order_bbn_approval_status(id)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.patch("/approve-unit-purchase-order-bbn-approval-status/{id}",status_code=status.HTTP_201_CREATED)
async def patch_approve_unit_purchase_order_bbn_approval_status(id:int):
    updated_data, err = UnitPurchaseOrderBBNService.patch_approve_unit_purchase_order_bbn_approval_status(id)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.patch("/close-order-unit-purchase-order-bbn-approval-status/{id}",status_code=status.HTTP_201_CREATED)
async def patch_approve_unit_purchase_order_bbn_approval_status(id:int):
    updated_data, err = UnitPurchaseOrderBBNService.patch_close_order_unit_purchase_order_bbn_approval_status(id)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/unit-purchase-order-bbn-cost-detail/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_unit_purchase_order_bbn_cost_detail(id:int):
    deleted_data, err = UnitPurchaseOrderBBNService.delete_unit_purchase_order_bbn_cost_detail(id)
    if err == None:
        return payload_response(204,"deleted",deleted_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.delete("/unit-purchase-order-bbn-detail/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_unit_purchase_order_bbn_detail(id:int):
    deleted_data, err = UnitPurchaseOrderBBNService.delete_unit_purchase_order_bbn_detail(id)
    if err == None:
        return payload_response(204,"deleted",deleted_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))