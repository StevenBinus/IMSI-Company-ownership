from sqlalchemy.orm import Session,load_only
from sqlalchemy import select, column
from src.entities.master import KppEntity,VillageEntity
from src.entities.master.KppEntity import MtrKpp
from src.payloads.schemas.master.KppSchema import MtrKppPost,MtrKppUpdate
from src.configs.database import get_db
from src.utils import AddPagination
from sqlalchemy.orm import Session

async def get_all_kpps(db:Session,page:int,limit:int, all_params:dict(), sort_params:dict()):  
    try:
        query_set = select(MtrKpp)
        counter = len(db.scalars(query_set).all())
        query_check = AddPagination.get_the_pagination_search_list(db,query_set,all_params)
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrKpp.kpp_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset(page*limit).limit(limit)
        results = db.scalars(query_final).all()

        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        return results, page_results, None
    except Exception as err:
        return None, None, err
   
async def get_kpp(db:Session,id:int):
    try:
        check_query=select(MtrKpp).where(MtrKpp.kpp_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None,err


async def post_kpp(db: Session,req:MtrKppPost):
    try:
        db.begin()
        _new_data=MtrKpp()
        _new_data.kpp_code=req.kpp_code
        _new_data.kpp_name=req.kpp_name
        _new_data.kpp_phone_no=req.kpp_phone_no
        _new_data.kpp_address_1=req.kpp_address_1
        _new_data.kpp_address_2=req.kpp_address_2
        _new_data.kpp_address_3=req.kpp_address_3
        _new_data.village_id=req.village_id
        db.add(_new_data)
        db.commit() 

        db.refresh(_new_data)
        return _new_data,None
    except Exception as err:
        db.rollback()
        return None, err


async def put_kpp(db:Session,id:int, req:MtrKppUpdate):
    try:
        query_check=select(MtrKpp).where(MtrKpp.kpp_id==id)
        update_data=db.scalars(query_check).first()
        update_data.kpp_name=req.kpp_name
        update_data.kpp_phone_no=req.kpp_phone_no
        update_data.kpp_address_1=req.kpp_address_1
        update_data.kpp_address_2=req.kpp_address_2
        update_data.kpp_address_3=req.kpp_address_3
        update_data.village_id=req.village_id
        db.commit()
        db.refresh(update_data)
        return update_data,None

    except Exception as err:
        return None, err

async def patch_kpp(db:Session,id:int):
    try: 
        check_active=select(MtrKpp).where(MtrKpp.kpp_id==id)
        current_status=db.scalars(check_active).first()
        active=current_status.is_active
    
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
       
