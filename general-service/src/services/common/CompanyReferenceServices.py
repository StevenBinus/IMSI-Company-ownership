from src.repositories.common import CompanyReferenceRepo
from src.payloads.schemas.master.CompanyReferenceSchema import MtrCompanyreferenceGet
from fastapi import Request

def get_all_company_references(page:int, limit:int,all_params:dict(), sort_params:dict()):
    get_data, page_results, err = CompanyReferenceRepo.get_all_company_references(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_company_reference_by_id(id:int):
    result, err = CompanyReferenceRepo.get_company_reference_by_company_id(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def get_tax_industry_by_company_id(id:int):
    result, err = CompanyReferenceRepo.get_company_reference_by_company_id(id)
    if err == None:
        return result, None
    else:
        return result, err


def post_company_reference(req:MtrCompanyreferenceGet):
    created_data, err = CompanyReferenceRepo.post_company_reference(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_company_reference(id:int):
    updated_data, err = CompanyReferenceRepo.patch_company_reference(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_company_reference(id:int,req:MtrCompanyreferenceGet):
    updated_data, err = CompanyReferenceRepo.put_company_reference(id,req)
    if err == None:
        return updated_data, None
    else:
        return None, err