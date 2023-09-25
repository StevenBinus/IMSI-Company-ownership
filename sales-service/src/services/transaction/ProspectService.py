from src.repositories.transaction import ProspectRepo
from src.payloads.schemas.transaction import ProspectSchema
from sqlalchemy.orm import Session


async def get_all_prospects(db:Session,page:int,limit:int,all_params:dict()):
    get_results, page_results, err = await ProspectRepo.get_all_prospects(db,page,limit,all_params)
    if err != None:
        get_results = None
        page_results = None
    return get_results, page_results, err

async def get_prospect_by_id(db:Session, id:int):
    header_result, detail_result, err = await ProspectRepo.get_prospect_by_id(db,id)
    if err != None:
        header_result = None
        detail_result = None
    return header_result, detail_result, err
    
async def post_prospect(db:Session,req:ProspectSchema.TrxProspectRequest):
    created_data,err = await ProspectRepo.post_prospect(db,req)
    if err != None:
        created_data = None
    return created_data, err

async def post_prospect_vehicle_detail(db:Session,req:ProspectSchema.TrxProspectVehicleDetailRequest):
    created_detail,err = await ProspectRepo.post_prospect_vehicle_detail(db,req)
    if err != None:
        created_detail = None
    return created_detail, err
    
async def post_prospect_follow_up(db:Session,req:ProspectSchema.TrxProspectFolloWUpRequest):
    created_followup,err = await ProspectRepo.post_prospect_follow_up(db,req)
    if err != None:
        created_followup = None
    return created_followup, err