from src.repositories.transaction import UnitGoodsReceiveBBNSTNKRepo
from src.payloads.schemas.transaction.UnitGoodsReceiveBBNSTNKSchema import TrxUnitGoodsReceiveBBNSTNKRequest, TrxUnitGoodsReceiveBBNSTNKInputSendRequest, TrxUnitGoodsReceiveBBNSTNKUpdateRequest
from fastapi import Request
from sqlalchemy.orm import Session

def get_unit_goods_receive_bbn_stnk_search(db: Session, page:int,limit:int,all_params:dict()):
    get_data, page_results, err = UnitGoodsReceiveBBNSTNKRepo.get_unit_goods_receive_bbn_stnk_search(db, page,limit,all_params)
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err

def post_unit_goods_receive_bbn_Stnk(db: Session, req_form:TrxUnitGoodsReceiveBBNSTNKRequest):
    post_data,err = UnitGoodsReceiveBBNSTNKRepo.post_unit_goods_receive_bbn_stnk(db, req_form)
    if err == None:
        return post_data, None
    else:
        return post_data, err
    
def get_unit_goods_receive_bbn_stnk_by_id(db: Session, id:int):
    get_data, err = UnitGoodsReceiveBBNSTNKRepo.get_unit_goods_receive_bbn_stnk_by_id(db, id)
    if err == None:
        return get_data, None
    else:
        return get_data,  err

def patch_submit_unit_goods_receive_bbn_stnk(db: Session, id: int):
    updated_data, err = UnitGoodsReceiveBBNSTNKRepo.patch_submit_unit_goods_receive_bbn_stnk(db, id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def update_unit_goods_receive_bbn_stnk_input_send(db: Session, id: int, req:TrxUnitGoodsReceiveBBNSTNKInputSendRequest):
    updated_data, err = UnitGoodsReceiveBBNSTNKRepo.update_unit_goods_receive_bbn_stnk_input_send(db, id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_unit_goods_receive_bbn_stnk(db: Session, id:int):
    erase_data, err = UnitGoodsReceiveBBNSTNKRepo.delete_unit_goods_receive_bbn_stnk(db, id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def update_unit_goods_receive_bbn_stnk(db: Session, id: int, req:TrxUnitGoodsReceiveBBNSTNKUpdateRequest):
    updated_data, err = UnitGoodsReceiveBBNSTNKRepo.update_unit_goods_receive_bbn_stnk(db, id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err