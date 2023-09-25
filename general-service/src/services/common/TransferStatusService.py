from src.repositories.common import TransferStatusRepo
from src.payloads.schemas.common.TransferStatusSchema import MtrTransferStatusGetSchema
from fastapi import Request

def get_all_transfer_statuses(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TransferStatusRepo.get_all_transfer_statuses(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_transfer_status(id:int):
    result, err = TransferStatusRepo.get_by_id_transfer_status(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_transfer_status(req:MtrTransferStatusGetSchema):
    created_data, err = TransferStatusRepo.post_transfer_status(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_transfer_status(id:int,req:MtrTransferStatusGetSchema):
    updated_data, err = TransferStatusRepo.put_transfer_status(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_transfer_status(id:int):
    erase_data, err = TransferStatusRepo.delete_transfer_status(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_transfer_status(id:int):
    updated_data, err = TransferStatusRepo.patch_transfer_status(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
