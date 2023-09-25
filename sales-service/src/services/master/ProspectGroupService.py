from src.repositories.master import ProspectGroupRepo
from src.payloads.schemas.master.ProspectGroupSchema import ProspectGroupRequest
from sqlalchemy.orm import Session


async def get_prospect_group_all(db:Session, page: int, limit: int):
    get_data, page_results, err = await ProspectGroupRepo.get_prospect_group_all(db, page, limit)
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err


async def get_prospect_group_by_id(db:Session, id: int):
    result, err = await ProspectGroupRepo.get_prospect_group_by_id(db,id)
    if err == None:
        return result, None
    else:
        return result, err


async def post_prospect_group(db:Session, req: ProspectGroupRequest):
    created_data, err = await ProspectGroupRepo.post_prospect_group(db, req)
    if err == None:
        return created_data, None
    else:
        return None, err


async def update_prospect_group(db:Session, id: int, req: ProspectGroupRequest):
    updated_data, err = await ProspectGroupRepo.put_prospect_group(db, id, req)
    if err == None:
        return updated_data, None
    else:
        return None, err
