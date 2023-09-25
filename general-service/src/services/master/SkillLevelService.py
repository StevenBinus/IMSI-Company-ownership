from src.repositories.master import SkillLevelRepo
from src.payloads.schemas.master import SkillLevelSchema
from fastapi import Request

def get_skill_levels_cruds(page:int, limit:int, all_params:dict(), sort_params:dict()):
    get_data, page_results, err = SkillLevelRepo.get_skill_levels_cruds(page,limit,all_params,sort_params) 
    if err == None:
        return get_data, page_results, None
    else:
        return None, None, err
    
def get_skill_level_cruds(id:int):
    result, err = SkillLevelRepo.get_skill_level_cruds(id)
    if err == None:
        return result, None
    else:
        return result, err
    
    
def post_skill_level_cruds(req:SkillLevelSchema.MtrSkillLevelGetSchema):
    created_data, err = SkillLevelRepo.post_skill_level_cruds(req)
    if err == None:
        return created_data, None
    else:
        return None, err
    
def patch_skill_level_cruds(id:int):
    updated_data, err = SkillLevelRepo.patch_skill_level_cruds(id)
    if err == None:
        return updated_data, None
    else:
        return None, err
    
def put_skill_level(id,req):
    update_data,err=SkillLevelRepo.put_skill_level_cruds(id,req)
    if err == None:
        return update_data,None
    else:
        return None,err

def delete_skill_level(id):
    delete_data,err = SkillLevelRepo.delete_skill_level_cruds(id)
    if err == None:
        return delete_data,err
    else:
        return None,err
