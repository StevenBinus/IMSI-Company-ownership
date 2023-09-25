from fastapi import Request
from sqlalchemy import select, column
from src.payloads.schemas.master import CompanyReferenceSchema
from src.utils import AddPagination
from src.configs.database import get_db
from src.utils.Activation import activation
import math
from src.entities.common import ApprovalSPMEntity,AdjustmentReasonEntity
from src.entities.master import CompanyEntity
from src.entities.master.MtrCompanyReferenceEntity import MtrCompanyReference



def get_all_company_references(page:int,limit:int, all_params:dict(), sort_params:dict()):
    db = get_db()
    try:
        query_set = select(
            MtrCompanyReference.is_active,
            MtrCompanyReference.company_id,
            MtrCompanyReference.currency_id,
            MtrCompanyReference.margin_outer_kpp,
            MtrCompanyReference.adjustment_reason_id,
            MtrCompanyReference.lead_time_unit_etd,
            MtrCompanyReference.bank_acc_receive_company_id,
            MtrCompanyReference.vat_code,
            MtrCompanyReference.item_broken_warehouse_id,
            MtrCompanyReference.unit_warehouse_id,
            MtrCompanyReference.use_dms,
            MtrCompanyReference.time_difference,
            MtrCompanyReference.operation_discount_outer_kpp,
            MtrCompanyReference.check_month_end,
            MtrCompanyReference.coa_group_id,
            MtrCompanyReference.with_vat,
            MtrCompanyReference.approval_spm_id,
            MtrCompanyReference.is_use_tax_industry,
            MtrCompanyReference.markup_percentage,
            MtrCompanyReference.is_external_pdi,
            MtrCompanyReference.hide_cost,
            MtrCompanyReference.use_price_code,
            MtrCompanyReference.disable_edit_draft_soinvoice
            ).join(
            CompanyEntity.MtrCompany, MtrCompanyReference.company_id==CompanyEntity.MtrCompany.company_id
            ).join(
            AdjustmentReasonEntity.MtrAdjustmentReason, MtrCompanyReference.adjustment_reason_id==AdjustmentReasonEntity.MtrAdjustmentReason.adjustment_reason_id
            ).join(
            ApprovalSPMEntity.MtrApprovalSpm,MtrCompanyReference.approval_spm_id==ApprovalSPMEntity.MtrApprovalSpm.approval_spm_id
            )
        tables =[MtrCompanyReference,CompanyEntity.MtrCompany,AdjustmentReasonEntity.MtrAdjustmentReason,ApprovalSPMEntity.MtrApprovalSpm]
        query_check,counter = AddPagination.get_the_pagination_search_list_with_join(db,query_set,all_params,tables)
        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrCompanyReference.company_id.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        query_final = query_check.offset(page*limit).limit(limit)
    
        data = db.execute(query_final).all()

        results=[]
        for is_active,company_id,currency_id,margin_outer_kpp,adjustment_reason_id,lead_time_unit_etd,bank_acc_receive_company_id,vat_code,item_broken_warehouse_id,unit_warehouse_id,use_dms,time_difference,operation_discount_outer_kpp,check_month_end,coa_group_id,with_vat,approval_spm_id,is_use_tax_industry,markup_percentage,is_external_pdi,hide_cost,use_price_code,disable_edit_draft_soinvoice in data:
                go_out = {
                    "is_active":is_active,
                    "company_id": company_id,
                    "currency_id": currency_id,
                    "margin_outer_kpp": margin_outer_kpp,
                    "adjustment_reason_id": adjustment_reason_id,
                    "lead_time_unit_etd": lead_time_unit_etd,
                    "bank_acc_receive_company_id":bank_acc_receive_company_id,
                    "vat_code":vat_code,
                    "item_broken_warehouse_id": item_broken_warehouse_id,
                    "unit_warehouse_id": unit_warehouse_id,
                    "use_dms": use_dms,
                    "time_difference": time_difference,
                    "operation_discount_outer_kpp": operation_discount_outer_kpp,
                    "check_month_end":check_month_end,
                    "coa_group_id":coa_group_id,
                    "with_vat": with_vat,
                    "approval_spm_id": approval_spm_id,
                    "is_use_tax_industry": is_use_tax_industry,
                    "markup_percentage": markup_percentage,
                    "is_external_pdi": is_external_pdi,
                    "hide_cost":hide_cost,
                    "use_price_code":use_price_code,
                    "disable_edit_draft_soinvoice": disable_edit_draft_soinvoice}
                results.append(go_out)

        total_rows = counter
        total_pages = math.ceil(total_rows/limit)
        page_results = {
                "total_rows" : total_rows,
                "total_pages" : total_pages
            }
        return results,page_results,None
    except Exception as err:
        return None, None, err
    
def get_tax_industry_with_vat_by_company_id(id:int):
    db = get_db()
    try:
        query_check=select(MtrCompanyReference.company_id,MtrCompanyReference.is_use_tax_industry,MtrCompanyReference.with_vat).where(MtrCompanyReference.company_id==id)
        result = db.scalars(query_check).first()
        return result,None
    except Exception as err:
        return None, err
    
def get_company_reference_by_company_id(id:int):
    db = get_db()
    try:
        query_check=select(MtrCompanyReference).where(MtrCompanyReference.company_id==id)
        result = db.scalars(query_check).all()
        return result,None
    except Exception as err:
        return None, err

def post_company_reference(req:CompanyReferenceSchema.MtrCompanyreferenceGet):
     db=get_db()
     try:
          db.begin()
          _new_data=MtrCompanyReference
          _new_data.company_id=req.company_id
          _new_data.currency_id=req.currency_id
          _new_data.margin_outer_kpp=req.margin_outer_kpp
          _new_data.adjustment_reason_id=req.adjustment_reason_id
          _new_data.lead_time_unit_etd=req.lead_time_unit_etd
          _new_data.bank_acc_receive_company_id=req.bank_acc_receive_company_id
          _new_data.vat_code=req.vat_code
          _new_data.item_broken_warehouse_id=req.item_broken_warehouse_id
          _new_data.unit_warehouse_id=  req.unit_warehouse_id
          _new_data.use_dms_new_datas=req.use_dm_new_datas
          _new_data.time_difference=req.time_difference
          _new_data.operation_discount_outer_kpp=req.operation_discount_outer_kpp
          _new_data.check_month_end=req.check_month_end
          _new_data.coa_group_id=req.coa_group_id
          _new_data.with_vat=req.with_vat
          db.add(_new_data)
          db.commit()

          db.refresh(_new_data)
          return _new_data,None
     except Exception as err:
        db.rollback()
        return None,err
     
def put_company_reference(id:int,req:CompanyReferenceSchema.MtrCompanyreferenceGet):
     db=get_db()
     try:
        query_check=select(MtrCompanyReference).where(MtrCompanyReference.company_id==id)
        update_data=db.scalars(query_check).First()
        update_data.company_id=req.company_id
        update_data.currency_id=req.currency_id
        update_data.margin_outer_kpp=req.margin_outer_kpp
        update_data.adjustment_reason_id=req.adjustment_reason_id
        update_data.lead_time_unit_etd=req.lead_time_unit_etd
        update_data.bank_acc_receive_company_id=req.bank_acc_receive_company_id
        update_data.vat_code=req.vat_code
        update_data.item_broken_warehouse_id=req.item_broken_warehouse_id
        update_data.unit_warehouse_id=  req.unit_warehouse_id
        update_data.use_dms_new_datas=req.use_dm_new_datas
        update_data.time_difference=req.time_difference
        update_data.operation_discount_outer_kpp=req.operation_discount_outer_kpp
        update_data.check_month_end=req.check_month_end
        update_data.coa_group_id=req.coa_group_id
        update_data.with_vat=req.with_vat
        db.commit()
        db.refresh(update_data)
        return update_data,None
     
     except Exception as err:
         return None,err
     

def patch_company_reference(id:int):
   db = get_db()
   check_active=select(MtrCompanyReference).where(MtrCompanyReference.company_id==id)
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
       
