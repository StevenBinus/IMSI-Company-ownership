from src.repositories.common import TaxOutTransactionRepo
from src.payloads.schemas.common.TaxOutTransactionSchema import MtrTaxOutTransactionGetSchema
from fastapi import Request

def get_all_tax_out_transaction_types(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = TaxOutTransactionRepo.get_all_tax_out_transaction_types(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_by_id_tax_out_transaction_type(id:int):
    result, err = TaxOutTransactionRepo.get_by_id_tax_out_transaction_type(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_tax_out_transaction_type(req:MtrTaxOutTransactionGetSchema):
    created_data, err = TaxOutTransactionRepo.post_tax_out_transaction_type(req)
    if err == None:
        return created_data, None
    else:
        return None, err

def put_tax_out_transaction_type(id:int,req:MtrTaxOutTransactionGetSchema):
    updated_data, err = TaxOutTransactionRepo.put_tax_out_transaction_type(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_tax_out_transaction_type(id:int):
    erase_data, err = TaxOutTransactionRepo.delete_tax_out_transaction_type(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_tax_out_transaction_type(id:int):
    updated_data, err = TaxOutTransactionRepo.patch_tax_out_transaction_type(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
