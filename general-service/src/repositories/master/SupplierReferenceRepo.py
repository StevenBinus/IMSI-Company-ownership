from src.entities.master import SupplierReferenceEntity
from src.entities.master import SupplierReferenceBankReferenceEntity
from src.payloads.schemas.master import SupplierReferenceBankReferenceSchema
from src.payloads.schemas.master import SupplierReferencePicSchema
from src.entities.master import SupplierReferencePicEntity,DivisionEntity,JobPositionEntity,SupplierEntity,AddressEntity
from src.entities.master.SupplierReferenceEntity import MtrSupplierReferenceEntity
from src.entities.master.SupplierTypeEntity import MtrSupplierType
from src.payloads.schemas.master import SupplierReferenceSchema
from src.configs.database import get_db
from sqlalchemy import select,column
from src.utils import AddPagination
from datetime import datetime
import math



async def post_supplier_reference_pic(req:SupplierReferencePicSchema.MtrSupplierReferencePic):
    db=get_db()
    try:
        new_data = SupplierReferencePicEntity.MtrSupplierReferencePic()
        new_data.pic_code=req.pic_code
        new_data.pic_name=req.pic_name
        new_data.pic_division_id=req.pic_division_id
        new_data.pic_position_id=req.pic_position_id
        new_data.pic_mobile_phone=req.pic_mobile_phone
        new_data.supplier_reference_id=req.supplier_reference_id
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err
    
def patch_supplier_reference_pic(id:int):
    db=get_db()
    try:
        query_check = select(SupplierReferencePicEntity.MtrSupplierReferencePic).where(SupplierReferencePicEntity.MtrSupplierReferencePic.supplier_reference_pic_id==id)
        query_set = db.scalars(query_check).first()
        check_status = query_set.is_active
        if check_status ==True:
            query_set.is_active = False
        else:
            query_set.is_active = True
        db.commit()
        db.refresh(query_set)
        return query_set,None
    except Exception as err:
        db.rollback()
        return None,err
    
def get_supplier_reference_pic(id:int):
    db=get_db()
    query_set = select(
            SupplierReferencePicEntity.MtrSupplierReferencePic.pic_code,
            SupplierReferencePicEntity.MtrSupplierReferencePic.pic_name,
            DivisionEntity.MtrDivision.division_name,
            JobPositionEntity.MtrJobPosition.job_position_name,
            SupplierReferencePicEntity.MtrSupplierReferencePic.pic_mobile_phone
        ).join(DivisionEntity.MtrDivision,DivisionEntity.MtrDivision.division_id==SupplierReferencePicEntity.MtrSupplierReferencePic.pic_division_id).join(
            JobPositionEntity.MtrJobPosition,JobPositionEntity.MtrJobPosition.job_position_id==SupplierReferencePicEntity.MtrSupplierReferencePic.pic_position_id
        ).where(SupplierReferencePicEntity.MtrSupplierReferencePic.supplier_reference_id==id)
    data = db.execute(query_set).all()

    result=[]

    for pic_code,pic_name,division_name,job_position_name,pic_mobile_phone in data:
            go_out={
                "pic_code":pic_code,
                "pic_name":pic_name,
                "division_name":division_name,
                "job_position_description":job_position_name,
                "pic_mobile_phone":pic_mobile_phone
            }
            result.append(go_out)

    return result


def post_supplier_reference_bank_reference(req:SupplierReferenceBankReferenceSchema.MtrSupplierReferenceBankReference):
    db=get_db()
    try:
        new_data = SupplierReferenceBankReferenceEntity.MtrSupplierReferenceBankReference()
        new_data.bank_id=req.bank_id
        new_data.account_type=req.account_type
        new_data.account_name=req.account_name
        new_data.account_number=req.account_number
        new_data.currency_id=req.currency_id
        new_data.supplier_reference_id=req.supplier_reference_id
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err
    
def patch_supplier_reference_bank_reference(id:int):
    db=get_db()
    try:
        query_set=select(SupplierReferenceBankReferenceEntity.MtrSupplierReferenceBankReference).where(SupplierReferenceBankReferenceEntity.MtrSupplierReferenceBankReference.supplier_reference_bank_account_id==id)
        query_check = db.scalars(query_set).first()
        check_active =query_check.is_active
        if check_active==True:
            query_check.is_active=False
            db.commit()
            db.refresh(query_check)
            return query_check,None
        else:
            query_check.is_active=True
            db.commit()
            db.refresh(query_check)
            return query_check,None
    except Exception as err:
        db.rollback()
        return None,err

def get_supplier_reference_bank_reference(id:int):
    db=get_db()
    query_set=select(SupplierReferenceBankReferenceEntity.MtrSupplierReferenceBankReference).where(SupplierReferenceBankReferenceEntity.MtrSupplierReferenceBankReference.supplier_reference_id==id)
    result = db.scalars(query_set).all()
    return result




def post_supplier_reference(req:SupplierReferenceSchema.MtrSupplierReferenceSchema):
    db = get_db()
    try:
        db.begin()
        new_data=SupplierReferenceEntity.MtrSupplierReferenceEntity()
        new_data.supplier_name=req.supplier_name
        new_data.supplier_type_id=req.supplier_type_id
        new_data.supplier_class=req.supplier_class
        new_data.supplier_title_prefix=req.supplier_title_prefix
        new_data.supplier_address_id=req.supplier_address_id
        new_data.supplier_phone_number=req.supplier_phone_number
        new_data.supplier_fax_number=req.supplier_fax_number
        new_data.supplier_mobile_phone=req.supplier_mobile_phone
        new_data.supplier_email_address=req.supplier_email_address
        new_data.supplier_behaviour_id=req.supplier_behaviour_id
        new_data.term_of_payment_id=req.term_of_payment_id
        new_data.minimum_down_payment=req.minimum_down_payment
        new_data.via_binning=req.via_binning
        new_data.old_supplier_code=req.old_supplier_code
        new_data.business_group_id=req.business_group_id
        new_data.supplier_unique_code=req.supplier_unique_code
        new_data.company_id=req.company_id
        new_data.vat_npwp_no=req.vat_npwp_no
        new_data.vat_npwp_date=req.vat_npwp_date
        new_data.vat_name=req.vat_name
        new_data.vat_address_id=req.vat_address_id
        new_data.vat_pkp_type=req.vat_pkp_type
        new_data.vat_pkp_no=req.vat_pkp_no
        new_data.vat_tax_service_office_id=req.vat_tax_service_office_id
        new_data.vat_transaction_id=req.vat_transaction_id
        new_data.tax_npwp_no=req.tax_npwp_no
        new_data.tax_name=req.tax_name
        new_data.tax_address_id=req.tax_address_id
        new_data.tax_pkp_no=req.tax_pkp_no
        new_data.tax_pkp_date=req.tax_pkp_date
        new_data.tax_pkp_type=req.tax_pkp_type
        new_data.tax_tax_service_office_id=req.tax_tax_service_office_id
        new_data.vat_pkp_date=req.vat_pkp_date
        new_data.tax_npwp_date=req.tax_npwp_date
        new_data.supplier_status='15'
        db.add(new_data)
        print("hai")
        db.commit()
        print("hai")
        db.refresh(new_data)
        print("hai")
        return new_data,None
    except Exception as err:
        db.rollback()
        return None,err

def get_supplier_reference_by_id(id:int):
    db =get_db()
    try:
        query_check=select(MtrSupplierReferenceEntity).where(MtrSupplierReferenceEntity.supplier_reference_id==id)
        query_set = db.scalars(query_check).first()
        get_pic = get_supplier_reference_pic(id)
        get_bank_reference = get_supplier_reference_bank_reference(id)
        return query_set,get_pic,get_bank_reference,None
    except Exception as err:
        return None,None,None,err
    
def get_supplier_references(page:int,limit:int,all_params:dict(),sort_params:dict()):
    db=get_db()
    try:
        query_set=select(
            MtrSupplierReferenceEntity.supplier_status,
            MtrSupplierReferenceEntity.supplier_code,
            MtrSupplierReferenceEntity.supplier_name,
            MtrSupplierType.supplier_type_description,
            AddressEntity.MtrAddress.address_street_1,
            AddressEntity.MtrAddress.address_street_2
        ).join(MtrSupplierType,MtrSupplierReferenceEntity.supplier_type_id==MtrSupplierType.supplier_type_id). join(
            AddressEntity.MtrAddress, MtrSupplierReferenceEntity.supplier_address_id==AddressEntity.MtrAddress.address_id
        )
        tables=[MtrSupplierReferenceEntity,MtrSupplierType,AddressEntity.MtrAddress]
        query_check,counter = AddPagination.get_the_pagination_search_list_with_join(query_set,all_params,tables)

        if sort_params["sort_by"] == None or sort_params["sort_of"] == None:
            query_check = query_check.order_by(MtrSupplierReferenceEntity.supplier_code.desc())
        else:
            if sort_params["sort_of"] == "desc":
                query_check = query_check.order_by(column(sort_params["sort_by"]).desc())
            else:
                query_check = query_check.order_by(column(sort_params["sort_by"]).asc())
        
        query_final=query_check.offset(page*limit).limit(limit)
        data = db.execute(query_final).all()

        result=[]

        for supplier_status,supplier_code,supplier_name,supplier_type_description, address_street_1,address_street_2 in data:
            go_out={
                "supplier_status":supplier_status,
                "supplier_code":supplier_code,
                "supplier_name":supplier_name,
                "supplier_type":supplier_type_description,
                "address_street_1":address_street_1,
                "address_street_2":address_street_2
            }
            result.append(go_out)


        total_rows = counter
        total_pages = math.ceil(counter/limit)
        page_result={
            "total_rows":total_rows,
            "total_pages":total_pages
        }
        return result,page_result,None
    except Exception as err:
        return None,None,err
    
        
    
def patch_supplier_reference(id:int):
    db=get_db()
    try:
        query_check = select(MtrSupplierReferenceEntity).where(MtrSupplierReferenceEntity.supplier_reference_id==id)
        query_set = db.scalars(query_check).first()
        query_set.supplier_status='20'
        if query_set.supplier_code == None:
            now = datetime.now()
            year = now.strftime("%y")
            supp_name = query_set.supplier_name
            firts_supp_name = supp_name[0].capitalize()
            supplier_prefix = f"S{firts_supp_name}{year}"
            check_prefix =select(MtrSupplierReferenceEntity.supplier_code).filter(MtrSupplierReferenceEntity.supplier_code.like(f"{supplier_prefix}%")).order_by(MtrSupplierReferenceEntity.supplier_code.desc())
            set_prefix=db.scalars(check_prefix).first()
            
            if set_prefix:
                get_prefix = int(set_prefix[-5:])
                num_prefix=(get_prefix+1)%10000
                res_suffix=f"{num_prefix:05}"
            else:
                num_prefix=1%100000
                res_suffix=f"{num_prefix:05}"        
            supplier_code = f"{supplier_prefix}{res_suffix}"
            query_set.supplier_code=supplier_code  
            new_data =post_supplier_master(query_set)
            db.commit()
            db.refresh(query_set)
            print(query_set)
            return query_set,None
        else:
            return query_set,None
    except Exception as err:
        db.rollback()
        return None,err
    
def post_supplier_master(query_set: object):
    db = get_db()
    try:
        db.begin()
        new_data = SupplierEntity.MtrSupplier()
        new_data.company_id=query_set.company_id
        new_data.supplier_unique_id = query_set.supplier_unique_code
        new_data.supplier_code = query_set.supplier_code
        new_data.supplier_title_prefix=query_set.supplier_title_prefix
        new_data.supplier_name=query_set.supplier_name
        new_data.supplier_title_suffix=query_set.supplier_title_suffix
        new_data.supplier_type_id=query_set.supplier_type_id
        new_data.term_of_payment_id=query_set.term_of_payment_id
        new_data.via_binning=query_set.via_binning
        new_data.supplier_address_id=query_set.supplier_address_id
        new_data.supplier_phone_no=query_set.supplier_phone_number
        new_data.supplier_fax_no=query_set.supplier_fax_number
        new_data.supplier_mobile_phone=query_set.supplier_mobile_phone
        new_data.supplier_email_address=query_set.supplier_email_address
        new_data.minimum_down_payment=query_set.minimum_down_payment
        new_data.supplier_behaviour_id=query_set.supplier_behaviour_id
        new_data.vat_npwp_no = query_set.vat_npwp_no
        new_data.vat_npwp_date=query_set.vat_npwp_date
        new_data.vat_pkp_type=query_set.vat_pkp_type
        new_data.vat_pkp_no = query_set.vat_pkp_no
        new_data.vat_pkp_date=query_set.vat_pkp_date
        new_data.vat_transaction_id=query_set.vat_transaction_id
        new_data.vat_name=query_set.vat_name
        new_data.vat_address_id=query_set.vat_address_id
        new_data.vat_tax_office=query_set.vat_tax_service_office_id
        new_data.tax_npwp_no=query_set.tax_npwp_no
        new_data.tax_npwp_date=query_set.tax_npwp_date
        new_data.tax_pkp_type=query_set.tax_pkp_type
        new_data.tax_pkp_no=query_set.tax_pkp_no
        new_data.tax_pkp_date=query_set.tax_pkp_date
        new_data.tax_name=query_set.tax_name
        new_data.tax_address_id=query_set.tax_address_id
        new_data.tax_tax_office_id=query_set.tax_tax_service_office_id
        db.add(new_data)
        db.commit()
        db.refresh(new_data)
        return new_data
        
    except Exception as err:
        db.rollback()
        return None, err
        
