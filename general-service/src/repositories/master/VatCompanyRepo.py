from sqlalchemy.orm import Session
from src.entities.master import VatCompanyEntity as VatEntity, CompanyEntity,TaxOfficeEntity,AddressEntity
from src.entities.common import TaxOutTransactionEntity
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from src.payloads.schemas.master.VatSchema import VatCompanyRequest
from src.utils.BoolConvert import strtobool
import math
from src.configs.database import get_db
from src.utils import AddPagination
from fastapi import Request

def get_vat_companies(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db=get_db()
    try:
        query_set = select(
            VatEntity.MtrVatCompany.is_active,
            VatEntity.MtrVatCompany.vat_company_id,
            VatEntity.MtrVatCompany.company_id,
            VatEntity.MtrVatCompany.vat_npwp_no,
            VatEntity.MtrVatCompany.vat_npwp_date,
            VatEntity.MtrVatCompany.vat_tax_out_transaction_id,
            VatEntity.MtrVatCompany.vat_tax_branch_code,
            VatEntity.MtrVatCompany.vat_name,
            VatEntity.MtrVatCompany.vat_address_id,
            VatEntity.MtrVatCompany.vat_reserve,
            VatEntity.MtrVatCompany.vat_reserve,
            VatEntity.MtrVatCompany.vat_pkp_no,
            VatEntity.MtrVatCompany.vat_pkp_date,
            VatEntity.MtrVatCompany.vat_tax_office_id
        ).join(
            CompanyEntity, VatEntity.MtrVatCompany.company_id==CompanyEntity.MtrCompany.company_id
        ).join(
            TaxOfficeEntity, VatEntity.MtrVatCompany.vat_tax_office_id==TaxOfficeEntity.MtrTaxOffice.tax_office_id
        ).join(
            AddressEntity, VatEntity.MtrVatCompany.vat_address_id==AddressEntity.MtrAddress.address_id
        ).join(
            TaxOutTransactionEntity, VatEntity.MtrVatCompany.vat_tax_out_transaction_id==TaxOutTransactionEntity.MtrVATTransactionCode.vat_transaction_code_id
        )
        counter = len(db.scalars(query_set).all())
        query_check=AddPagination.get_the_pagination_search_list(query_set,all_params,sort_params)

        if sort_params["sort_by"]==None or sort_params["sort_of"]==None:
            query_check=query_check.order_by(VatEntity.MtrVatCompany.vat_company_id.desc())
        else:
            if sort_params["sort_of"]=="desc":
                query_check=query_check.order_by(VatEntity.MtrVatCompany.vat_company_id.desc())
            else:
                query_check=query_check.order_by(VatEntity.MtrVatCompany.vat_company_id.asc())
        query_final=query_check.order_by(VatEntity.MtrVatCompany.vat_company_id).offset(page*limit).limit(limit)

        data=db.execute(query_final).all()

        total_rows=counter
        total_pages=int(total_rows/limit)
        result=[]
        for is_active,vat_company_id,company_id,vat_npwp_no,vat_npwp_date,vat_tax_out_transaction_id,vat_tax_branch_code,vat_name,vat_address_id,vat_reserve,vat_reserve,vat_pkp_no,vat_pkp_date,vat_tax_office_id in data:
            go_out= {
                    "is_active":is_active,
                    "vat_company_id":vat_company_id,
                    "company_id":company_id,
                    "vat_npwp_no":vat_npwp_no,
                    "vat_npwp_date":vat_npwp_date,
                    "vat_tax_out_transaction_id":vat_tax_out_transaction_id,
                    "vat_tax_branch_code":vat_tax_branch_code,
                    "vat_name":vat_name,
                    "vat_address_id":vat_address_id,
                    "vat_reserve":vat_reserve,
                    "vat_pkp_no":vat_pkp_no,
                    "vat_pkp_date":vat_pkp_date,
                    "vat_tax_office_id":vat_tax_office_id
            }
            result.append(go_out)
        page_result = {
            "total_rows":total_rows,
            "total_pages":total_pages
        }
        return result,page_result,None
    except Exception as err:
        return None,None,err
                    

def get_vat_company(id:int):
    db = get_db()
    try:
        query_check = select(VatEntity).where(VatEntity.MtrVatCompany.vat_company_id==id)
        result = db.scalars(query_check).first
        return result, None
    except Exception as err:
        return None, err

def post_vat_company(req:VatCompanyRequest):
    db=get_db()
    try:
        db.begin()
        new_data=VatEntity.MtrVatCompany()
        new_data.company_id=req.vat_same_company_id
        new_data.vat_npwp_no=req.vat_npwp_no
        new_data.vat_npwp_date=req.vat_npwp_date
        new_data.vat_tax_branch_code=req.vat_tax_branch_code
        new_data.vat_name=req.vat_name
        new_data.vat_reserve=req.vat_reserve
        new_data.vat_pkp_type=req.vat_pkp_type
        new_data.vat_pkp_no=req.vat_pkp_no
        new_data.vat_pkp_date=req.vat_pkp_date
        new_data.vat_address_id=req.vat_address_id
        new_data.vat_tax_out_transaction_id=req.vat_tax_out_transaction_id
        new_data.vat_tax_office_id=req.vat_tax_office_id
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

def delete_vat_company(id:int):
    db = get_db()
    try:
        query_check = select(VatEntity).where(VatEntity.MtrVatCompany.vat_company_id==id)
        result = db.scalars(query_check).first
        db.delete(result)
        db.commit()
        return result, None
    except Exception as err:
        db.rollback()
        return None, err
    
def put_vat_company(id:int,req:VatCompanyRequest):
    db=get_db()
    try:
        query_check = select(VatEntity).where(VatEntity.MtrVatCompany.vat_company_id==id)
        result = db.scalars(query_check).first
        result.vat_npwp_no=req.vat_npwp_no
        result.vat_npwp_date=req.vat_npwp_date
        result.vat_tax_branch_code=req.vat_tax_branch_code
        result.vat_name=req.vat_name
        result.vat_reserve=req.vat_reserve
        result.vat_pkp_type=req.vat_pkp_type
        result.vat_pkp_no=req.vat_pkp_no
        result.vat_pkp_date=req.vat_pkp_date
        result.vat_address_id=req.vat_address_id
        result.vat_tax_out_transaction_id=req.vat_tax_out_transaction_id
        result.vat_tax_office_id=req.vat_tax_office_id
        db.commit()
        db.refresh(result)
        return result,None
    except Exception as err:
        return None, err
    
def patch_vat_company(id:int):
    db = get_db()
    check_active=select(VatEntity.MtrVatCompany).where(VatEntity.MtrVatCompany.vat_company_id==id)
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
       db.rollback
       return None, err