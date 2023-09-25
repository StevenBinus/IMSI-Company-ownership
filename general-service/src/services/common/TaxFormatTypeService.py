from src.repositories.common import TaxFormatTypeRepo
from src.payloads.schemas.common.TaxFormatTypeSchema import MtrTaxFormatTypeGetSchema
from fastapi import Request

def get_all_tax_format_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TaxFormatTypeRepo.get_all_tax_format_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_tax_format_type(id:int):
    result, err = TaxFormatTypeRepo.get_by_id_tax_format_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_tax_format_type(req:MtrTaxFormatTypeGetSchema):
    created_data, err = TaxFormatTypeRepo.post_tax_format_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_tax_format_type(id:int,req:MtrTaxFormatTypeGetSchema):
    updated_data, err = TaxFormatTypeRepo.put_tax_format_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_tax_format_type(id:int):
    erase_data, err = TaxFormatTypeRepo.delete_tax_format_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_tax_format_type(id:int):
    updated_data, err = TaxFormatTypeRepo.patch_tax_format_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err