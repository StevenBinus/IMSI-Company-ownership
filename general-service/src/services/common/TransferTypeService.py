from src.repositories.common import TransferTypeRepo
from src.payloads.schemas.common.TransferTypeSchema import MtrTransferTypeGetSchema
from fastapi import Request

def get_all_transfer_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TransferTypeRepo.get_all_transfer_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_transfer_type(id:int):
    result, err = TransferTypeRepo.get_by_id_transfer_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_transfer_type(req:MtrTransferTypeGetSchema):
    created_data, err = TransferTypeRepo.post_transfer_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_transfer_type(id:int,req:MtrTransferTypeGetSchema):
    updated_data, err = TransferTypeRepo.put_transfer_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_transfer_type(id:int):
    erase_data, err = TransferTypeRepo.delete_transfer_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_transfer_type(id:int):
    updated_data, err = TransferTypeRepo.patch_transfer_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
