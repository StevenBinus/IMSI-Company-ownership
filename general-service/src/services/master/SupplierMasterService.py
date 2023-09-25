from src.repositories.master import SupplierMasterRepo
from fastapi import Request

def get_supplier_list(page:int,limit:int,get_all_params:dict(),sort_fields:dict()):
    get_data, page_results, err = SupplierMasterRepo.get_supplier_list(page,limit,get_all_params,sort_fields) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_supplier_by_id(id:int):
    header_result, detail_pic_results, detail_bank_account_results, err = SupplierMasterRepo.get_supplier_by_id(id)
    if err == None:
        return header_result, detail_pic_results, detail_bank_account_results, None
    else:
        return header_result, detail_pic_results, detail_bank_account_results, err