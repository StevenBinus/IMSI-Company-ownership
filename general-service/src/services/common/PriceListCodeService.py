from src.repositories.common import PriceListCodeRepo
from src.payloads.schemas.common import PriceListCodeSchema
from fastapi import Request

def get_price_list_codes_cruds(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = PriceListCodeRepo.get_price_list_codes_cruds(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_price_list_code_cruds(id:int):
    result, err = PriceListCodeRepo.get_price_list_code_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_price_list_code_cruds(req:PriceListCodeSchema.MtrPriceListCodeGetSchema,request:Request):
    created_data, err = PriceListCodeRepo.post_price_list_code_cruds(req,request)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_price_list_code_cruds(id:int,request:Request):
    updated_data, err = PriceListCodeRepo.patch_price_list_code_cruds(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err