from src.repositories.master import CountryRepo
from src.payloads.schemas.master import CountrySchema
from fastapi import Request


def get_countries_cruds(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = CountryRepo.get_countries_cruds(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_country_cruds(id:int):
    result, err = CountryRepo.get_country_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_country_cruds(req:CountrySchema.MtrCountrySchema):
    created_data, err = CountryRepo.post_country_cruds(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_country_cruds(id:int):
    updated_data, err = CountryRepo.patch_country_cruds(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_country(id:int,req:CountrySchema.MtrCountryRequest):
    update_data, err = CountryRepo.put_country_cruds(id,req)
    if err == None:
        return update_data,err
    else:
        return None, update_data
    
def delete_country(id:int):
    deleted_data, err = CountryRepo.delete_country_cruds(id)
    if err == None:
        return deleted_data,None
    else:
        return None,deleted_data