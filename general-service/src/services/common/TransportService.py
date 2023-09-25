from src.repositories.common import TransportRepo
from src.payloads.schemas.common.TransportSchema import MtrTransportGetSchema
from fastapi import Request

def get_all_transports(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TransportRepo.get_all_transports(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_transport(id:int):
    result, err = TransportRepo.get_by_id_transport(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_transport(req:MtrTransportGetSchema):
    created_data, err = TransportRepo.post_transport(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_transport(id:int):
    updated_data, err = TransportRepo.patch_transport(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_transport(id:int,req:MtrTransportGetSchema):
    updated_data, err = TransportRepo.put_transport(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_transport(id:int):
    erase_data, err = TransportRepo.delete_transport(id)
    if err == None:
        return erase_data, None
    else:
        return None, err