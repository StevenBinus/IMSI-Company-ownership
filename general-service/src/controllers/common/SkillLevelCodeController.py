from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.common import SkillLevelCodeService
from src.payloads.schemas.master import SkillLevelCodeSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException


router = APIRouter(tags=["Skill Level Code"],prefix="/api/general")

@router.get("/skill-level-codes", status_code=200)
async def get_skill_level_codes(page:int,limit:int,
                                is_active:bool|None=None,
                               skill_level_code_id:int|None=None,
                                skill_level_code:int|None=None,
                                 sort_of:str|None=None,
                                  sort_by:str|None=None):
    get_all_params={
        "is_active":is_active,
        "skill_level_code_id":skill_level_code_id,
        "skill_level_code":skill_level_code,
    }
    sort_fields={"sort_of":sort_of,"sort_by":sort_by}
    get_results,pages,err = SkillLevelCodeService.get_skill_level_codes_cruds(page,limit,get_all_params,sort_fields)
    if err == None:
        return pagination_response(200,"Success", page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/skill-level-code/{skill_level_code_id}", status_code=200)
async def get_skill_level_code(skill_level_code_id:int):
    get_skill_level_code_by_id,err = SkillLevelCodeService.get_skill_level_code_cruds(skill_level_code_id)
    if err == None:
        return payload_response(200,"Success",get_skill_level_code_by_id)
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.post("/skill-level-code", status_code=201)
async def post_skill_level_code(req:SkillLevelCodeSchema.MtrSkillLevelCodeGetSchema):
    create_skill_level_code,err =SkillLevelCodeService.post_skill_level_code_cruds(req)
    if err == None:
        return payload_response(201,"Success",create_skill_level_code)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.delete("/skill-level-code/{skill_level_code_id}", status_code=204)
async def delete_skill_level_code(skill_level_code_id:int):
    erase_skill_level_code,err = SkillLevelCodeService.delete_skill_level_code(skill_level_code_id)
    if err == None:
        return payload_response(204,"Success",erase_skill_level_code)
    else:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/skill-level-code/{skill_level_code_id}", status_code=202)
async def put_skill_level_code(skill_level_code_id:int,req:SkillLevelCodeSchema.MtrSkillLevelCodeGetSchema):
    update_skill_level_code,err=SkillLevelCodeService.put_skill_level_code(skill_level_code_id,req)
    if err == None:
        return payload_response(202,"Success",update_skill_level_code)
    else:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/skill-level-code/{skill_level_code_id}", status_code=202)
async def patch_skill_level_code(skill_level_code_id:int):
    status_skill_level_code,err=SkillLevelCodeService.patch_skill_level_code_cruds(skill_level_code_id)
    if err == None:
        return payload_response(202,"Success",status_skill_level_code)
    else:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))