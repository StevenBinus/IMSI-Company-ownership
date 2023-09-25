from src.repositories.master import VatCompanyRepo as VatRepo
from src.payloads.schemas.master import VatSchema
from fastapi import Request

def get_vat_companies(page:int,limit:int,get_all_params:dict(),sort_fields:dict()):
    get_data, page_results, err = VatRepo.get_vat_companies(page,limit,get_all_params,sort_fields) 
    if err == None:
        return get_data, page_results, None
    else:
        return None,None, err
    
def get_vat_company(id:int):
    result, err = VatRepo.get_vat_company(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_vat_company(req:VatSchema.VatCompanyRequest):
    created_data, err = VatRepo.post_vat_company(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_vat_company(id:int,request:Request):
    updated_data, err = VatRepo.patch_vat_company(id,request)
    if err == None:
        return updated_data, None
    else:
        return None, err

def delete_vat_company(id:int):
    deleted_data,err=VatRepo.delete_vat_company(id)
    if err == None:
        return deleted_data,None
    else:
        return None, err

def put_vat_company(id:int,req:VatSchema.VatCompanyRequest):
    updated_data,err=VatRepo.put_vat_company(id,req)
    if err == None:
        return updated_data , None
    else:
        return None ,err