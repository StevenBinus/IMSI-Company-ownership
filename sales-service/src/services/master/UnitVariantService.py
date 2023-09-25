from src.repositories.master import UnitVariantRepo
from src.payloads.schemas.master.UnitVariantSchema import UnitVariantRequest
from sqlalchemy.orm import Session

async def get_unit_variants_list_all(db:Session,page:int, limit:int, all_params=dict(), sort_params=dict()):
    results,page_results,err = await UnitVariantRepo.get_unit_variants_list_all(db,page,limit,all_params,sort_params)
    if err != None:
        results = None
        page_results = None
    return results, page_results, err

async def get_unit_variant_by_id(db:Session,id:int):
    result, err = await UnitVariantRepo.get_unit_variant_by_id(db,id)
    if err != None:
        result = None,
    return result, err

async def get_unit_variant_drop_down(db:Session,model_id:int):
    result, err = await UnitVariantRepo.get_unit_variant_drop_down(db,model_id)
    if err != None:
        result = None
    return result, err
    
async def post_unit_variant(db:Session,req:UnitVariantRequest):
    created_data, err = await UnitVariantRepo.post_unit_variant(db,req)
    if err != None:
        created_data = None,
    return created_data,err

async def update_unit_variant(db:Session,id:int,req:UnitVariantRequest):
    updated_data, err = await UnitVariantRepo.update_unit_variant(db,id,req)
    if err != None:
        updated_data = None,
    return updated_data,err
    
async def patch_unit_variant(db:Session, id:int):
    active_status, err = await UnitVariantRepo.patch_unit_variant(db,id)
    if err != None:
        active_status = None
    return active_status, err