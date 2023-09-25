from src.repositories.master import PriceCodeRepo
from src.payloads.schemas.master.PriceCodeSchema import PriceCodeRequest

from fastapi import Request

def get_price_code_search(page:int,limit:int,all_params:dict()):
    get_data, page_results, err = PriceCodeRepo.get_price_code_search(page,limit,all_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_price_code_by_id(id:int):
    result, err = PriceCodeRepo.get_price_code_by_id(id)
    if err == None:
        return result, None
    else:
        return None, err
    
def post_price_code(req_data:PriceCodeRequest,request:Request):
    get_results, err = PriceCodeRepo.post_price_code(req_data,request)
    if err == None:
        return get_results, None
    else:
        return None, err

def update_price_code(id:int, req:PriceCodeRequest, request:Request):
    updated_data,err = PriceCodeRepo.update_price_code(id,req,request)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def patch_price_code(id:int,request:Request):
    updated_data, err = PriceCodeRepo.patch_price_code(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err