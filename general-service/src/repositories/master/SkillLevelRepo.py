from fastapi import Request
from sqlalchemy import select, column
from src.entities.master import SkillLevelEntity
from src.payloads.schemas.master.SkillLevelSchema import MtrSkillLevelGetSchema
from src.utils.AddPagination import get_the_pagination_search_list
from src.configs.database import get_db
from src.utils.Activation import activation
import math

def get_skill_levels_cruds(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(SkillLevelEntity.MtrSkillLevel)
        counter = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(SkillLevelEntity.MtrSkillLevel.skill_level_id.desc())
        else:
                    if sort_params["sort_by"]=="desc":
                        query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
                    else:
                        query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final=query_check.offset(page*limit).limit(limit)
                
        result = db.scalars(query_final).all()

        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
                    "total_rows" : total_rows,
                    "total_pages" : total_pages
                }
        return result, page_results, None
    except Exception as err:
         return None,None,err

def get_skill_level_cruds(id:int):
    db = get_db()
    try:
        query_set=select(SkillLevelEntity.MtrSkillLevel).where(SkillLevelEntity.MtrSkillLevel.skill_level_id==id)
        query_check=db.scalars(query_set).first()
        return query_check,None
    except Exception as err:
        return None,err

def post_skill_level_cruds(req:MtrSkillLevelGetSchema):
    db = get_db()
    try:
        db.begin()
        new_data = SkillLevelEntity.MtrSkillLevel()
        new_data.skill_level_code=req.skill_level_code
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None, err


def delete_skill_level_cruds(id:int):
    db = get_db()
    try:
        query_set=select(SkillLevelEntity.MtrSkillLevel).where(SkillLevelEntity.MtrSkillLevel.skill_level_id==id)
        query_check=db.scalars(query_set).first()
        db.delete(query_check)
        db.commit()
        return query_check,None
    except Exception as err:
        db.rollback()
        return None, err
        
def put_skill_level_cruds(id:int,req:MtrSkillLevelGetSchema):
    db=get_db()
    try:
        query_check=select(SkillLevelEntity.MtrSkillLevel).where(SkillLevelEntity.MtrSkillLevel.skill_level_id==id)
        query_set=db.scalars(query_check).first()
        query_set.skill_level_code=req.skill_level_code
        db.commit()
        db.refresh(query_set)
        return query_set,None
    except Exception as err:
        db.rollback()
        return None,err

def patch_skill_level_cruds(id:int):
    db=get_db()
    query_check=select(SkillLevelEntity.MtrSkillLevel).where(SkillLevelEntity.MtrSkillLevel.skill_level_id==id)
    query_set=db.scalars(query_check).first()
    try:
        active = query_set.is_active
        if active == True:
            query_set.is_active==False
        else:
            query_set.is_active==True
        db.commit()
        db.refresh(query_set)
        return query_set,None

    except Exception as err:
        return None,err      

