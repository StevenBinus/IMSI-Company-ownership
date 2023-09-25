from src.repositories.common import SkillLevelCodeRepo
from src.payloads.schemas.master import SkillLevelCodeSchema
from fastapi import Request

def get_skill_level_codes_cruds(page:int, limit:int, get_all_params:dict(),sort_fields:dict()):
    get_data, page_results, err = SkillLevelCodeRepo.get_skill_level_codes_cruds(page,limit,get_all_params,sort_fields) 
    if err == None:
        return get_data, page_results, None
    else:
        return get_data, page_results, err
    
def get_skill_level_code_cruds(id:int):
    result, err = SkillLevelCodeRepo.get_skill_level_code_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_skill_level_code_cruds(req:SkillLevelCodeSchema.MtrSkillLevelCodeGetSchema):
    created_data, err = SkillLevelCodeRepo.post_skill_level_code_cruds(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_skill_level_code_cruds(id:int):
    updated_data, err = SkillLevelCodeRepo.patch_skill_level_code_cruds(id)
    if err == None:
        return updated_data, None
    else:
        return None, err

def delete_skill_level_code(id:int):
    delete_data,err = SkillLevelCodeRepo.delete_skill_level_code_cruds(id)
    if err == None:
        return delete_data,None
    else:
        return None, err

def put_skill_level_code(id:int,req:SkillLevelCodeSchema.MtrSkillLevelCodeGetSchema):
    update_data,err = SkillLevelCodeRepo.put_skill_level_code_cruds(id,req)
    if err == None:
        return update_data,None
    else:
        return None,err