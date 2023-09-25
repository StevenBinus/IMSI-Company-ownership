from fastapi import APIRouter, HTTPException, status, Query, Request, Depends
from src.services.transaction import UnitGoodsReceiveBBNSTNKService
from src.payloads.schemas.transaction.UnitGoodsReceiveBBNSTNKSchema import TrxUnitGoodsReceiveBBNSTNKRequest, TrxUnitGoodsReceiveBBNSTNKInputSendRequest, TrxUnitGoodsReceiveBBNSTNKUpdateRequest
from src.payloads.responses.CommonResponse import payload_response,payload_response_detail
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from datetime import datetime
from sqlalchemy.orm import Session
from src.configs.database import get_db

router = APIRouter(tags=["Transaction : Unit Goods Receive BBN STNK"],prefix="/api/sales")

@router.get("/unit-goods-receive-bbn-stnk", status_code=status.HTTP_200_OK)
async def get_unit_goods_receive_bbn_stnk_search(
    page:int, 
    limit:int,
    goods_receive_bbn_stnk_document_number:str|None=None,
    goods_receive_bbn_stnk_date_from:datetime|None=None,
    goods_receive_bbn_stnk_date_to:datetime|None=None,
    supplier_id:int|None=None,
    brand_id:int|None=None,
    stnk_number:str|None=None,
    vehicle_chassis_number:str|None=None,
    db:Session=Depends(get_db)
    ):
        get_all_params = {
            "goods_receive_bbn_stnk_document_number": goods_receive_bbn_stnk_document_number,
            "goods_receive_bbn_stnk_date_from": goods_receive_bbn_stnk_date_from,
            "goods_receive_bbn_stnk_date_to": goods_receive_bbn_stnk_date_to,
            "supplier_id": supplier_id,
            "brand_id": brand_id,
            "stnk_number": stnk_number,
            "vehicle_chassis_number": vehicle_chassis_number
        }

        get_results, pages, err = UnitGoodsReceiveBBNSTNKService.get_unit_goods_receive_bbn_stnk_search(db, page,limit,get_all_params)
                                                                                                      
        if not get_results or err != None:
            raise HTTPException(status_code=404, detail=str(err))
        else:
            return pagination_response(200,"success",page,limit,pages["total_pages"],pages["total_rows"],get_results)

@router.post("/unit-goods-receive-bbn-stnk",status_code=status.HTTP_201_CREATED)
async def post_unit_goods_receive_bbn_Stnk(req_data:TrxUnitGoodsReceiveBBNSTNKRequest, db:Session=Depends(get_db)):
    created_data, err = UnitGoodsReceiveBBNSTNKService.post_unit_goods_receive_bbn_Stnk(db, req_data)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=ResponseException(409))
    
@router.get("/unit-goods-receive-bbn-stnk/{id}", status_code=status.HTTP_200_OK)
async def get_unit_goods_receive_bbn_stnk_by_id(id:int, db:Session=Depends(get_db)):
    result, err = UnitGoodsReceiveBBNSTNKService.get_unit_goods_receive_bbn_stnk_by_id(db, id)
    if not result or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"success",result)

@router.patch("/unit-goods-receive-bbn-stnk/{id}",status_code=status.HTTP_201_CREATED)
async def patch_submit_unit_goods_receive_bbn_stnk(id:int, db:Session=Depends(get_db)):
    updated_data, err = UnitGoodsReceiveBBNSTNKService.patch_submit_unit_goods_receive_bbn_stnk(db, id)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/unit-goods-receive-bbn-stnk-input-send/{id}",status_code=status.HTTP_201_CREATED)
async def update_unit_goods_receive_bbn_stnk_input_send(id:int,req:TrxUnitGoodsReceiveBBNSTNKInputSendRequest, db:Session=Depends(get_db)):
    updated_data, err = UnitGoodsReceiveBBNSTNKService.update_unit_goods_receive_bbn_stnk_input_send(db, id, req)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))
    
@router.delete("/unit-goods-receive-bbn-stnk/{id}",status_code=204)
async def delete_unit_goods_receive_bbn_stnk(id:int, db:Session=Depends(get_db)):
    erase_data, err = UnitGoodsReceiveBBNSTNKService.delete_unit_goods_receive_bbn_stnk(db, id)
    if err == None:
        return payload_response(204,"Deleted",erase_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/unit-goods-receive-bbn-stnk/{id}",status_code=status.HTTP_201_CREATED)
async def update_unit_goods_receive_bbn_stnk(id:int,req:TrxUnitGoodsReceiveBBNSTNKUpdateRequest, db: Session=Depends(get_db)):
    updated_data, err = UnitGoodsReceiveBBNSTNKService.update_unit_goods_receive_bbn_stnk(db, id, req)
    if err == None:
        return payload_response(201,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))