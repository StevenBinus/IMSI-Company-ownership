from src.utils import AddPagination
from sqlalchemy import select,column
from src.entities.master import AddressEntity,VillageEntity
from src.entities.master.AddressEntity import MtrAddress
from src.payloads.schemas.master.AddressSchema import MtrAddressRequest,MtrAddressUpdate
from src.configs.database import get_db
import math

def get_addresses(page:int, limit:int, all_params:dict(), sort_params:dict()):
    db = get_db()
    try:
        query_set = select(
            MtrAddress.is_active,
            MtrAddress.address_id,
            MtrAddress.address_latitude,
            MtrAddress.address_longitude,
            MtrAddress.address_street_1,
            MtrAddress.address_street_2,
            MtrAddress.address_street_3,
            MtrAddress.address_type,
            MtrAddress.village_id
        ).join(VillageEntity.MtrVillage,MtrAddress.village_id == VillageEntity.MtrVillage.village_id)
        tables = [MtrAddress,VillageEntity.MtrVillage]
        query_check,counter = AddPagination.get_the_pagination_search_list_with_join(db,query_set,all_params,tables)
        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check=query_check.order_by(MtrAddress.address_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final = query_check.order_by(MtrAddress.address_id).offset(page*limit).limit(limit)
        data = db.execute(query_final).all()
        results=[]

        for is_active,address_id,address_latitude,address_longitude,address_street_1,address_street_2,address_street_3,address_type,village_id in data:
            go_out={
                "is_active":is_active,
                "address_id":address_id,
                "address_latitude":address_latitude,
                "address_longitude":address_longitude,
                "address_street_1":address_street_1,
                "address_street_2":address_street_2,
                "address_street_3":address_street_3,
                "address_type":address_type,
                "village_id":village_id
            }
            results.append(go_out)
        total_rows = counter
        total_pages = math.ceil(total_rows/limit)
        page_results={
            "total_rows":total_rows,
            "total_pages":total_pages
        }
        return results,page_results,None
    except Exception as err:
        return None,None,err

    
def get_address_by_id(id:int):
    db=get_db()
    try:
        check_query = select(MtrAddress).where(MtrAddress.address_id==id)
        result=db.scalars(check_query).first()
        return result,None
    except Exception as err:
        return None,err

def post_address(req:MtrAddressRequest):
    db=get_db()
    try:
        db.begin()
        new_data=MtrAddress()
        new_data.address_latitude=req.address_latitude
        new_data.address_longitude=req.address_longitude
        new_data.address_street_1=req.address_street_1
        new_data.address_street_2=req.address_street_2
        new_data.address_street_3=req.address_street_3
        new_data.address_type=req.address_type
        new_data.village_id=req.village_id
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

def delete_address(id:int):
    db=get_db()
    try:
        check_query = select(MtrAddress).where(MtrAddress.address_id==id)
        result=db.scalars(check_query).first()
        db.delete(result)
        db.commit()
        return result,None
    except Exception as err:
        db.rollback()
        return None,err
     
def put_address(id:int,req:MtrAddressUpdate):
    db=get_db()
    try:
        check_query = select(MtrAddress).where(MtrAddress.address_id==id)
        update_data=db.scalars(check_query).first()
        update_data.address_latitude=req.address_latitude
        update_data.address_longitude=req.address_longitude
        update_data.address_street_1=req.address_street_1
        update_data.address_street_2=req.address_street_2
        update_data.address_street_3=req.address_street_3
        update_data.address_type=req.address_type
        db.commit()
        db.refresh(update_data)
        return update_data,None
    except Exception as err:
        return None,err

def patch_address(id:int):
    db = get_db() 
    check_query = select(MtrAddress).where(MtrAddress.address_id==id)
    current_status=db.scalars(check_query).first()
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
        db.rollback
        return None, err
       
