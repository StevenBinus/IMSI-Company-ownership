from fastapi import Request
from sqlalchemy import select, column
from sqlalchemy.orm import load_only, joinedload, subqueryload, Bundle
from src.entities.master.SupplierEntity import MtrSupplier
from src.entities.master.SupplierPICEntity import MtrSupplierPIC
from src.entities.master.SupplierBankAccount import MtrSupplierBankAccount
from src.entities.master.AddressEntity import MtrAddress
from src.entities.master.JobTitleEntity import MtrJobTitle
from src.entities.common.BankAccountTypeEntity import MtrBankAccountType
from datetime import datetime
import calendar
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search_list, get_the_pagination_search_list_with_join

def get_supplier_list(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db = get_db()
    try:
        query_set = select(
            MtrSupplier.supplier_code,
            MtrSupplier.supplier_name,
            MtrSupplier.supplier_type_id,
            MtrAddress.address_street_1,
            MtrAddress.address_street_2,
            MtrSupplier.is_active
        ).join(
            MtrAddress,
            MtrSupplier.supplier_address_id == MtrAddress.address_id
        )

        tables = [MtrSupplier, MtrAddress]
        counter = len(db.scalars(query_set).all())
        query_check = get_the_pagination_search_list_with_join(db, query_set, all_params, tables)
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrSupplier.supplier_code.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        
        query_final = query_check.offset(page*limit).limit(limit)
        datas = db.execute(query_final).all()

        results = []
        for supplier_code, suppler_name, supplier_type_id, address_street_1, address_street_2, is_active in datas:
            go_out = {
                "supplier_code": supplier_code,
                "supplier_name": suppler_name,
                "supplier_type_id": supplier_type_id,
                "address_street_1": address_street_1,
                "address_street_2": address_street_2,
                "is_active": is_active
            }
            results.append(go_out)
        
        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
            "total_rows": total_rows,
            "total_pages": total_pages
        }
        return results, page_results, None
    except Exception as err:
        return None, None, err

def get_supplier_by_id(id: int):
    db = get_db()
    try:
        header_check_query = select(MtrSupplier).where(MtrSupplier.supplier_id==id)
        header_result = db.scalars(header_check_query).first()

        detail_pic_results = get_supplier_detail_pic(id)

        detail_bank_account_results = get_supplier_detail_bank_account(id)

        return header_result, detail_pic_results, detail_bank_account_results, None
    except Exception as err:
        return None, None, None, err
    
def get_supplier_detail_pic(id: int):
    db = get_db()
    try:
        check_query = select(
            MtrSupplierPIC.pic_name,
            MtrSupplierPIC.pic_division_id,
            MtrJobTitle.job_title_name,
            MtrSupplierPIC.pic_mobile_phone,
            MtrSupplierPIC.is_active
        ).join(
            MtrJobTitle,
            MtrSupplierPIC.pic_job_title_id == MtrJobTitle.job_title_id
        ).where(MtrSupplierPIC.supplier_id == id)
        datas = db.execute(check_query).all()

        results = []
        for pic_name, pic_division_id, job_title_name, pic_mobile_phone, is_active in datas:
            go_out = {
                "pic_name": pic_name,
                "pic_division_id": pic_division_id,
                "pic_job_title": job_title_name,
                "pic_mobile_phone": pic_mobile_phone,
                "status": is_active
            }
            results.append(go_out)

        return results
    except Exception:
        return None
    
def get_supplier_detail_bank_account(id: int):
    db = get_db()
    try:
        check_query = select(
            MtrSupplierBankAccount.bank_id,
            MtrBankAccountType.bank_account_type_name,
            MtrSupplierBankAccount.currency_id,
            MtrSupplierBankAccount.account_no,
            MtrSupplierBankAccount.account_name,
            MtrSupplierBankAccount.is_active
        ).join(
            MtrBankAccountType,
            MtrSupplierBankAccount.account_type_id == MtrBankAccountType.bank_account_type_id
        ).where(MtrSupplierBankAccount.supplier_id == id)
        datas = db.execute(check_query).all()

        results = []
        for bank_id, bank_account_type_name, currency_id, account_no, account_name, is_active in datas:
            go_out = {
                "bank_id": bank_id,
                "account_type": bank_account_type_name,
                "currency": currency_id,
                "account_no": account_no,
                "name": account_name,
                "status": is_active
            }
            results.append(go_out)

        return results
    except Exception:
        return None