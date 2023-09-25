from src.repositories.master import VehicleMasterRepo
from src.payloads.schemas.master.VehicleMasterSchema import VehicleMasterRequest

from fastapi import Request

def get_vehicle_master_search(page:int,limit:int,all_params:dict()):
    get_data, page_results, err = VehicleMasterRepo.get_vehicle_master_search(page,limit,all_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err


async def get_vehicle_master_by_id(id:int):
    result, err = await VehicleMasterRepo.get_vehicle_master_by_id(id)
    if err != None:
        result = None
    return result, err
    