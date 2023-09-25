from sqlalchemy import select,column
import math
from src.entities.master.CompanyEntity import MtrCompany
from src.entities.master.CostProfitMapEntity import MtrCostProfitMap
from src.entities.master.ProfitCenterEntity import MtrProfitCenter
from src.entities.master.CostCenterEntity import MtrCostCenter
from src.payloads.schemas.master import CostProfitMapSchema
from src.configs.database import get_db
from src.utils import AddPagination

def get_all_cost_profit_maps(page:int, limit:int, all_params:dict(), sort_params:dict()):
    db = get_db()
    try:
        query_set = select(
            MtrCostProfitMap.company_id,
            MtrCompany.company_name,
            MtrCostProfitMap.profit_center_id,
            MtrCostProfitMap.cost_center_id,
            MtrCostProfitMap.mapping_description
        ).join(
            MtrCompany, 
            MtrCostProfitMap.company_id == MtrCompany.company_id
        )

        join_tables = [MtrCostProfitMap,MtrCompany]
        query_check,counter = AddPagination.get_the_pagination_search_list_with_join(db, query_set, all_params, join_tables)

        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check = query_check.order_by(MtrCostProfitMap.company_id.asc())
        else:
            if sort_params("sort_of") == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())

        query_final = query_check.offset(page*limit).limit(limit)
        data = db.execute(query_final).all()

        results = []
        for company_id, company_name, profit_center_id, cost_center_id, mapping_description in data:
            output = {
                "company_id": company_id,
                "company_name": company_name,
                "profit_center_id": profit_center_id,
                "cost_center_id": cost_center_id,
                "mapping_description": mapping_description
            }
            results.append(output)

        page_results = {
            "total_rows" : counter,
            "total_pages" :  math.ceil(counter/limit)
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    
def get_by_id_cost_profit_map(id: int):
    db = get_db()
    try:
        check_query = select(
            MtrCostProfitMap.is_acitve,
            MtrCostProfitMap.company_id,
            MtrCompany.company_name,
            MtrCostProfitMap.profit_center_id,
            MtrProfitCenter.profit_center_name,
            MtrCostProfitMap.cost_center_id,
            MtrCostCenter.cost_center_name,
            MtrCostProfitMap.mapping_description,
            ).join(
                MtrCompany,
                MtrCostProfitMap.company_id == MtrCompany.company_id
            ).join(
                MtrProfitCenter,
                MtrCostProfitMap.profit_center_id == MtrProfitCenter.profit_center_id
            ).join(
                MtrCostCenter,
                MtrCostProfitMap.cost_center_id == MtrCostCenter.cost_center_id
            ).where(MtrCostProfitMap.cost_profit_id==id)
        result = db.execute(check_query).first()
        output = {
            "is_acitve": result[0],
            "company_id": result[1],
            "company_name": result[2],
            "profit_center_id": result[3],
            "profit_center_name": result[4],
            "cost_center_id": result[5],
            "cost_center_name": result[6],
            "mapping_description": result[7]
        }
        return output, None
    except Exception as err:
        return None, err
    
def post_cost_profit_map(req:CostProfitMapSchema.MtrCostProfitMapSchema):
    db = get_db()
    try:
        db.begin()
        _new_data = MtrCostProfitMap()
        _new_data.company_id  = req.company_id
        _new_data.profit_center_id  = req.profit_center_id
        _new_data.cost_center_id  = req.cost_center_id
        _new_data.mapping_description  = req.mapping_description
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def put_cost_profit_map(id:int, req:CostProfitMapSchema.mtrCostProfitMapUpdateSchema):
    db = get_db()
    try:
        query_check = select(MtrCostProfitMap).where(MtrCostProfitMap.cost_profit_id==id)
        _updated_data = db.scalars(query_check).first()
        _updated_data.mapping_description  = req.mapping_description
        db.commit()
        db.refresh(_updated_data)
        return _updated_data, None
    
    except Exception as err:
        db.rollback()
        return None, err

def patch_cost_profit_map(id:int):
    db = get_db()
    check_active_status = select(MtrCostProfitMap).where(MtrCostProfitMap.cost_profit_id==id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_acitve
    try:
        if current_status == True:
            active_status.is_acitve = False
        else :
            active_status.is_acitve = True
            
        db.commit()
        db.refresh(active_status)

        return active_status, None


    except Exception as err:
        db.rollback()
        return None, err
