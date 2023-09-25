from src.payloads.schemas.master import SkillLevelCodeSchema
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.utils.BoolConvert import strtobool
import math
from src.configs.database import get_db
from src.utils import AddPagination
from src.entities.master import SkillLevelCodeEntity
from src.entities.master.SkillLevelCodeEntity import MtrSkillLevelCode


def get_skill_level_codes_cruds(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set=select(SkillLevelCodeEntity.MtrSkillLevelCode)
        counter = len(db.scalars(query_set).all())
        query_check = AddPagination.get_the_pagination_search_list(query_set,all_params,sort_params)
            
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
                    query_check = query_check.order_by(SkillLevelCodeEntity.MtrSkillLevelCode.skill_level_code_id.desc())
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

def get_skill_level_code_cruds(id:int):
    db = get_db()    
    try:
        query_check = select(MtrSkillLevelCode).where(MtrSkillLevelCode.skill_level_code_id==id)
        query_set=db.scalars(query_check).first()
        return query_set,None
    except Exception as err:
        return None,err

def post_skill_level_code_cruds(req:SkillLevelCodeEntity.MtrSkillLevelCode):
    db =get_db()
    try:
        db.begin()
        new_data=MtrSkillLevelCode()
        new_data.skill_level_code=req.skill_level_code
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

def delete_skill_level_code_cruds(id:int):
    db=get_db()
    try:
        query_check=select(MtrSkillLevelCode).where(MtrSkillLevelCode.skill_level_code_id==id)
        query_set=db.scalars(query_check).first()
        db.delete(query_set)
        return query_set,None
    except Exception as err:
        db.rollback()
        return None,err
    
def put_skill_level_code_cruds(id:int,req:SkillLevelCodeSchema.MtrSkillLevelCodeGetSchema):
    db=get_db()
    try:
        query_check = select(MtrSkillLevelCode).where(MtrSkillLevelCode.skill_level_code_id==id)
        query_set = db.scalars(query_check).first()
        query_set.skill_level_code=req.skill_level_code
        db.commit()
        db.refresh(query_set)
        return query_set,None
    except Exception as err:
        db.rollback()
        return None, err



def patch_skill_level_code_cruds(id:int):
    db=get_db()
    check_active=select(MtrSkillLevelCode).where(MtrSkillLevelCode.skill_level_code_id==id)
    current_status=db.scalars(check_active).first()
    active=current_status.is_active
    try:
       if active==True:
           current_status.is_active=False
       else:
           current_status.is_active=True

       db.commit()
       db.refresh(current_status)

       return current_status, None
   
    except Exception as err:
       db.rollback()
       return None, err