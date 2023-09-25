from src.repositories.common import StockOpnameStatusRepo
from src.payloads.schemas.common.StockOpnameStatusSchema import MtrStockOpnameStatusGetSchema
from fastapi import Request
def get_all_stock_opnames(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = StockOpnameStatusRepo.get_all_stock_opnames(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_stock_opname(id:int):
    result, err = StockOpnameStatusRepo.get_by_id_stock_opname(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_stock_opname(req:MtrStockOpnameStatusGetSchema):
    created_data, err = StockOpnameStatusRepo.post_stock_opname(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_stock_opname(id:int,req:MtrStockOpnameStatusGetSchema):
    updated_data, err = StockOpnameStatusRepo.put_stock_opname(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_stock_opname(id:int):
    erase_data, err = StockOpnameStatusRepo.delete_stock_opname(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_stock_opname(id:int):
    updated_data, err = StockOpnameStatusRepo.patch_stock_opname(id)
    if err == None:
        return updated_data, None
    else:
        return None, err