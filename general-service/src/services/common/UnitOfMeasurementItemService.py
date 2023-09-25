from src.repositories.common import UnitOfMeasurementItemRepo
from src.payloads.schemas.common.UnitOfMeasurementItemSchema import MtrUnitOfMeasurementItemGetSchema
from fastapi import Request

def get_all_unit_of_measurement_items(page:int, limit:int, query_of:list[str], query_by:list[str]):
    get_data, page_results, err = UnitOfMeasurementItemRepo.get_all_unit_of_measurement_items(page,limit,query_of,query_by) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_unit_of_measurement_item(id:int):
    result, err = UnitOfMeasurementItemRepo.get_unit_of_measurement_item(id)
    if err == None:
        return result, None
    else:
        return result, err
    
def post_unit_of_measurement_item(req:MtrUnitOfMeasurementItemGetSchema):
    created_data, err = UnitOfMeasurementItemRepo.post_unit_of_measurement_item(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_unit_of_measurement_item(id:int):
    updated_data, err = UnitOfMeasurementItemRepo.patch_unit_of_measurement_item(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def delete_unit_of_measurement_type(id:int):
    erase_data, err = UnitOfMeasurementItemRepo.delete_unit_of_measurement_item(id)
    if err == None:
        return erase_data, None
    else:
        return None, err
    
def patch_unit_of_measurement_type(id:int):
    updated_data, err = UnitOfMeasurementItemRepo.patch_unit_of_measurement_item(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
