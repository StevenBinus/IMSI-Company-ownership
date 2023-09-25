from fastapi import APIRouter,HTTPException,status,Request
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.master import SkillLevelSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.services.master import SkillLevelService


router = APIRouter(tags=["Skill Level"],prefix="/api/general")

@router.get("/skill-levels", status_code=200)
async def get_skill_levels(page:int,limit:int,
                           is_active:bool|None=None,
                           skill_level_id:int|None=None,
                           skill_level_code:str|None=None,
                           sort_of:str|None=None,
                           sort_by:str|None=None):
    all_params={"is_active":is_active,"skill_level_id":skill_level_id,"skill_level_code":skill_level_code}
    sort_params={"sort_of":sort_of,"sort_by":sort_by}
    get_params, pages,err =SkillLevelService.get_skill_levels_cruds(page,limit,all_params,sort_params)
    if get_params !=[] and err ==None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_params)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404)) 

@router.get("/skill-level/{skill_level_id}", status_code=200)
async def get_skill_level(skill_level_id:int):
    get_skill_level,err = SkillLevelService.get_skill_level_cruds(skill_level_id)
    if err == None:
        return payload_response(200,"Success",get_skill_level)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.post("/skill-level", status_code=201)
async def post_skill_level(req:SkillLevelSchema.MtrSkillLevelGetSchema):
    post_data,err=SkillLevelService.post_skill_level_cruds(req)
    if err == None:
        return payload_response(201,"Success",post_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))


@router.delete("/skill-level/{skill_level_id}", status_code=204)
async def delete_skill_level(skill_level_id:int):
    delete_data,err=SkillLevelService.delete_skill_level(skill_level_id)
    if err == None:
        return payload_response(204,"Success",delete_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/skill-level/{skill_level_id}", status_code=202)
async def put_skill_level(skill_level_id:int,req:SkillLevelSchema.MtrSkillLevelGetSchema):
    update_data,err=SkillLevelService.put_skill_level(id,req)
    if err == None:
        return payload_response(202,"Success",update_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/skill-level/{skill_level_id}", status_code=202)
async def patch_skill_level(skill_level_id:int):
    active_skill_level,err=SkillLevelService.patch_skill_level_cruds(skill_level_id)
    if err == None:
        return payload_response(202,"Success",active_skill_level)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
