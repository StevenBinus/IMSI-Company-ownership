from sqlalchemy import select
from src.entities.master.DealerRepresentativeEntity import MtrDealerRepresentative
from src.payloads.schemas.master import DealerRepresentativeSchema
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination

def get_all_dealers_representative(page:int, limit:int, query_of:list[str], query_by:list[str]):
    db = get_db()
    
    try:
        total_rows = db.query(MtrDealerRepresentative).count()
        total_pages  = int(total_rows/limit)

        query_check = get_the_pagination(MtrDealerRepresentative,query_of,query_by)   
        query_final = query_check.order_by(MtrDealerRepresentative.dealer_representative_id).offset(page*limit).limit(limit)

        results = db.scalars(query_final).all()

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    

def get_by_id_dealer_representative(id: int):
    db = get_db()
    try:
        check_query = select(MtrDealerRepresentative).where(MtrDealerRepresentative.dealer_representative_id==id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err
    
def post_dealer_representative(req:DealerRepresentativeSchema.MtrDealerRepresentativeSchema):
    db = get_db()
    try:
        db.begin()
        _new_data = MtrDealerRepresentative()
        _new_data.dealer_representative_code  = req.dealer_representative_code
        _new_data.dealer_representative_name  = req.dealer_representative_name
        _new_data.dealer_representative_cost_center_sequence  = req.dealer_representative_cost_center_sequence
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def put_dealer_representative(id:int, req:DealerRepresentativeSchema.MtrDealerRepresentativeSchema):
    db = get_db()
    try:
        query_check = select(MtrDealerRepresentative).where(MtrDealerRepresentative.dealer_representative_id==id)
        _updated_data = db.scalars(query_check).first()
        _updated_data.dealer_representative_code  = req.dealer_representative_code
        _updated_data.dealer_representative_name  = req.dealer_representative_name
        _updated_data.dealer_representative_cost_center_sequence  = req.dealer_representative_cost_center_sequence
        db.commit()
        db.refresh(_updated_data)
        return _updated_data, None
    
    except Exception as err:
        db.rollback()
        return None, err
    
def delete_dealer_representative(id:int):
    db = get_db()
    try:
        query_check = select(MtrDealerRepresentative).where(MtrDealerRepresentative.dealer_representative_id==id)
        erase_data = db.scalars(query_check).first()

        db.delete(erase_data)
        db.commit()

        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err
