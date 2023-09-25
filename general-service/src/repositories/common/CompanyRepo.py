from sqlalchemy.orm import Session
from sqlalchemy import select, column
from sqlalchemy.orm import load_only
from src.utils.AddPagination import get_the_pagination_search_list
from fastapi import Request
from src.entities.master.CompanyEntity import MtrCompany
from src.payloads.schemas.common.CompanySchema import MtrCompanyRequest
from src.configs.database import get_db


def get_company_all(page: int, limit: int, all_params: dict(), sort_params: dict()):
    db = get_db()
    # try:
    query_init = select(MtrCompany)
    query_check = get_the_pagination_search_list(
        query_init, all_params, sort_params, MtrCompany.company_code
    )
    # print("get attrr: " + str(MtrCompany.__tablename__.column(sort_params["sort_by"])))
    # if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
    # query_check = query_check.order_by(MtrCompany.company_code.asc())
    # else:
    #     if sort_params["sort_of"] == "desc":
    #         query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
    #     else:
    #         query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
    query_final = query_check.offset(page * limit).limit(limit)
    results = db.scalars(query_final).all()

    total_rows = len(results)
    total_pages = int(total_rows / limit)

    page_results = {"total_rows": total_rows, "total_pages": total_pages}

    return results, page_results, None

    # except Exception as err:
    #     return None, None, err


def get_company_by_id(id: int):
    db = get_db()
    try:
        check_query = select(MtrCompany).where(MtrCompany.company_id == id)
        result = db.scalars(check_query).first()
        return result, None
    except Exception as err:
        return None, err


def post_company(req: MtrCompanyRequest):
    db = get_db()
    try:
        insert_data = MtrCompany(
            is_active=True,
            company_code=req.company_code,
            company_type=req.company_type,
            company_name=req.company_name,
        )
        db.add(insert_data)
        db.commit()
        db.refresh(insert_data)
        return insert_data, None
    except Exception as err:
        db.rollback()
        return None, err


def put_company(id: int, req: MtrCompanyRequest):
    db = get_db()
    try:
        query_check = select(MtrCompany).where(MtrCompany.company_id == id)
        update_data = db.scalars(query_check).first()
        update_data.company_code = req.company_code
        update_data.company_name = req.company_name
        db.commit()
        db.refresh(update_data)
        return update_data, None
    except Exception as err:
        db.rollback()
        return None, err


def delete_company(id: int):
    db = get_db()
    try:
        query_check = select(MtrCompany).where(MtrCompany.company_id == id)
        delete_data = db.scalars(query_check).first()
        db.delete(delete_data)
        db.commit()
        return delete_data, None
    except Exception as err:
        db.rollback()
        return None, err


def patch_company(id: int):
    db = get_db()
    check_active_status = select(MtrCompany).where(MtrCompany.company_id == id)
    active_status = db.scalars(check_active_status).first()
    current_status = active_status.is_active
    try:
        if current_status == True:
            active_status.is_active = False
            db.commit()
            db.refresh(active_status)
            return active_status, None
        else:
            active_status.is_active = True
            db.commit()
            db.refresh(active_status)
            return active_status, None
    except Exception as err:
        db.rollback()
        return None, err
