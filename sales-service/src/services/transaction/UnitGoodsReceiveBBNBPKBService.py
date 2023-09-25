from src.repositories.transaction import UnitGoodsReceiveBBNBPKBRepo
from src.payloads.schemas.transaction.UnitGoodsReceiveBBNBPKBSchema import TrxUnitGoodsReceiveBBNBPKBRequest, TrxUnitGoodsReceiveBBNBPKBInputSendRequest, TrxUnitGoodsReceiveBBNBPKBUpdateRequest
from fastapi import Request
from sqlalchemy.orm import Session

def get_unit_goods_receive_bbn_bpkb_search(db: Session, page:int,limit:int,all_params:dict()):
    get_data, page_results, err = UnitGoodsReceiveBBNBPKBRepo.get_unit_goods_receive_bbn_bpkb_search(db, page,limit,all_params)
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err

def post_unit_goods_receive_bbn_bpkb(db: Session, req_form:TrxUnitGoodsReceiveBBNBPKBRequest):
    post_data,err = UnitGoodsReceiveBBNBPKBRepo.post_unit_goods_receive_bbn_bpkb(db, req_form)
    if err == None:
        return post_data, None
    else:
        return post_data, err
    
def get_unit_goods_receive_bbn_bpkb_by_id(db: Session, id:int):
    get_data, err = UnitGoodsReceiveBBNBPKBRepo.get_unit_goods_receive_bbn_bpkb_by_id(db, id)
    if err == None:
        return get_data, None
    else:
        return get_data,  err
    
def patch_submit_unit_goods_receive_bbn_bpkb(db: Session, id: int):
    updated_data, err = UnitGoodsReceiveBBNBPKBRepo.patch_submit_unit_goods_receive_bbn_bpkb(db, id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_unit_goods_receive_bbn_bpkb(db: Session, id:int):
    erase_data, err = UnitGoodsReceiveBBNBPKBRepo.delete_unit_goods_receive_bbn_bpkb(db, id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def update_unit_goods_receive_bbn_bpkb_input_send(db: Session, id: int, req:TrxUnitGoodsReceiveBBNBPKBInputSendRequest):
    updated_data, err = UnitGoodsReceiveBBNBPKBRepo.update_unit_goods_receive_bbn_bpkb_input_send(db, id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def update_unit_goods_receive_bbn_bpkb(db: Session, id: int, req:TrxUnitGoodsReceiveBBNBPKBUpdateRequest):
    updated_data, err = UnitGoodsReceiveBBNBPKBRepo.update_unit_goods_receive_bbn_bpkb(db, id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err