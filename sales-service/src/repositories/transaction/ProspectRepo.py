from sqlalchemy import select
from sqlalchemy.orm import Session
from src.entities.transaction.ProspectEntity import TrxProspectHeader as TrxProspect
from src.entities.transaction.ProspectDetailEntity import TrxProspectDetail
from src.entities.transaction.ProspectFollowUpEntity import TrxProspectFollowUp
from src.entities.master.ProspectCustomerEntity import MtrProspectCustomer
from src.entities.master.ProspectCustomerEntity import MtrProspectCustomer
from src.entities.master.UnitVariantEntity import MtrUnitVariant
from src.entities.master.ProspectStageEntity import MtrProspectStage
from src.entities.master.ProspectStatusEntity import MtrProspectStatus
from src.payloads.schemas.transaction import ProspectSchema
from src.utils.AddPagination import get_the_pagination
from datetime import datetime
import math
import numpy

#claims from JWT
company_id = 1
#user_id
#roles

async def get_all_prospects(db:Session,page:int,limit:int,all_params:dict()):
    if page <= 0:
        page = 1  
    try:
        query_init = select(TrxProspect.prospect_system_number,
                    TrxProspect.sales_repsentative_to,
                    TrxProspect.prospect_document_number,
                    TrxProspect.prospect_date,
                    MtrProspectStage.prospect_stage_description,
                    MtrProspectCustomer.prospect_customer_name,
                    MtrUnitVariant.variant_description,
                    TrxProspectDetail.prospect_quantity,
                    MtrProspectStatus.prospect_status_description).join(
                        MtrProspectStage, MtrProspectStage.prospect_stage_id == TrxProspect.prospect_stage_id, isouter=True
                        ).join(
                            MtrProspectCustomer,MtrProspectCustomer.prospect_customer_system_number == TrxProspect.prospect_customer_system_number,isouter=True
                        ).join(
                            TrxProspectDetail,TrxProspectDetail.prospect_detail_system_number == TrxProspect.prospect_system_number,isouter=True
                        ).join(
                            MtrUnitVariant,MtrUnitVariant.variant_id == TrxProspectDetail.prospect_variant_id,isouter=True
                        ).join(
                            MtrProspectStatus,MtrProspectStatus.prospect_status_id == TrxProspect.prospect_status_id,isouter=True
                        )
        final_query, counter = await get_the_pagination(db,TrxProspect,query_init,all_params)
        final_query = final_query.order_by(TrxProspect.prospect_system_number.desc()).offset((page*limit)-limit).limit(limit)
        results = db.execute(final_query).all()
        total_rows = len(results)
        total_pages = math.ceil(counter/limit)
        final_results = []
        for sys_no,sales_to,doc,date,stage,cust,variant,qty,prosp_status in results:
            # getting from user service and details
            if sales_to != None:
                sales_name = "Sales Dummy"
            resp = {
                "prospect_system_number":sys_no,
                "sales_representative":sales_name,
                "prospect_number":doc,
                "prospect_date":date,
                "last_stage":stage,
                "age":180,
                "prospect_name":cust,
                "variant":variant,
                "qty":qty,
                "status":prosp_status
            }
            final_results.append(resp)

        page_results= {
            "total_rows": total_rows,
            "total_pages": total_pages
        }
        return final_results, page_results, None
    except Exception as err:
        return None, None, err

async def get_prospect_by_id(db:Session,id_prospect:int):
    try:
        query_init_header = select(TrxProspect).join(MtrProspectCustomer,TrxProspect.prospect_customer_system_number==MtrProspectCustomer.prospect_customer_system_number).where(TrxProspect.prospect_system_number==id_prospect)
        header_result = db.scalars(query_init_header).first()
        
        query_init_detail = select(MtrProspectCustomer).where(MtrProspectCustomer.prospect_customer_system_number==header_result.prospect_customer_system_number)
        detail_result = db.scalars(query_init_detail).first()
        
        return header_result, detail_result, None
    except Exception as err:
        return None, None, err

async def post_prospect(db:Session,req:ProspectSchema.TrxProspectRequest):
    try:
        db.begin()
        _created_data = TrxProspect()
        _created_data.company_id = company_id #get from general-common service mtr_company using API
        _created_data.prospect_date = req.prospect_date

        if req.prospect_customer_system_number == None:
            gen_prospect_code = create_prospect_customer_code()
            hasil,err = await create_prospect_customer(db,req,gen_prospect_code)
            _created_data.prospect_customer_system_number = hasil
            if err != None:
                db.rollback()
        else:
            _created_data.prospect_customer_system_number = req.prospect_customer_system_number
        
        _created_data.customer_id = req.customer_id
        _created_data.prospect_document_number = create_prospect_document_number(hasil)
        _created_data.prospect_status_id = None #need logic to decide the status
        _created_data.prospect_stage_id = None #need logic to decice the stage
        _created_data.buying_plan_date = req.buying_plan_date
        _created_data.conduct_test_drive = req.conduct_test_drive
        _created_data.test_drive_date_schedule = req.test_drive_date_schedule
        _created_data.test_drive_date_actual = req.test_drive_date_actual
        _created_data.competitor_model = req.competitor_model
        _created_data.fund_type_id = req.fund_type_id
        _created_data.retail_price_unit = req.retail_price_unit
        _created_data.request_discount = req.request_discount
        _created_data.down_payment_budget = req.down_payment_budget
        _created_data.sales_repsentative_to = req.change_sales_rep_to #FK to user-service
        _created_data.prospect_reference = req.prospect_reference
        _created_data.prospect_note = req.prospect_note
        _created_data.stage_date_cc = datetime.now()
        _created_data.stage_date_ch = datetime.now()
        _created_data.vehicle_sales_order_system_number = None
        _created_data.prospect_drop_date = req.prospect_drop_date
        _created_data.prospect_drop_reason_id = req.prospect_drop_reason_id # FK to mtr_prospect_drop_reason from common-general service
        _created_data.prospect_drop_remark = req.prospect_drop_remark
        db.add(_created_data)
        db.commit()
        db.refresh(_created_data)
        return _created_data, None
    except Exception as err:
        db.rollback()
        return None, err
        
async def post_prospect_vehicle_detail(db:Session,req:ProspectSchema.TrxProspectVehicleDetailRequest):
    try:
        _created_data = TrxProspectDetail()
        _created_data.prospect_system_number = req.prospect_system_number
        _created_data.prospect_brand_id = req.prospect_brand_id
        _created_data.prospect_model_id = req.prospect_model_id
        _created_data.prospect_variant_id = req.prospect_variant_id
        _created_data.accessories_option_id = req.accessories_option_id
        _created_data.prospect_colour_id = req.prospect_colour_id
        _created_data.prospect_quantity = req.prospect_quantity
        _created_data.expected_delivery_date = req.expected_delivery_date
        db.add(_created_data)
        db.commit()
        db.refresh(_created_data)
        return _created_data,None
    except Exception as err:
        db.rollback()
        return False,err
    
async def post_prospect_follow_up(db:Session,req:ProspectSchema.TrxProspectFolloWUpRequest):
    try:
        _created_data_followup = TrxProspectFollowUp()
        _created_data_followup.prospect_system_number = req.prospect_system_number
        _created_data_followup.prospect_follow_up_date = req.prospect_follow_up_date
        _created_data_followup.follow_up_id = req.follow_up_id
        _created_data_followup.prospect_follow_up_note = req.prospect_follow_up_note
        _created_data_followup.result_date = req.result_date
        _created_data_followup.result_note = req.result_note
        db.add(_created_data_followup)
        db.commit()
        db.refresh(_created_data_followup)
        return _created_data_followup,None
    except Exception as err:
        db.rollback()
        return None, err
    
async def create_prospect_customer(db:Session,req:ProspectSchema.TrxProspectRequest,prospect_code:str):
    #claims from token
    if req.change_sales_rep_to == None:
        sales_representative = 1
    else:
        sales_representative = req.change_sales_rep_to
    try:
        _created_cust = MtrProspectCustomer()
        _created_cust.company_id = company_id
        _created_cust.prospect_code = prospect_code
        _created_cust.customer_type_id = req.prospect_type
        _created_cust.prospect_customer_title_prefix = req.title_prefix
        _created_cust.prospect_customer_name = req.prospect_name
        _created_cust.prospect_customer_title_suffix = req.title_suffix
        _created_cust.business_type_id = req.customer_group_sub_category # FK to mtr_business_type from common-general service
        _created_cust.business_group_id = req.customer_group_business_category # FK to mtr_business_group from common-general service
        _created_cust.sales_representative_id = sales_representative
        _created_cust.prospect_address_id = 1 # FK to mtr_address from general service
        _created_cust.prospect_customer_mobile_phone = req.customer_mobile_phone
        _created_cust.prospect_customer_email_address = req.customer_mobile_emailaddr
        _created_cust.prospect_customer_website = req.customer_group_website
        _created_cust.prospect_customer_phone_number = req.customer_phone_no
        _created_cust.prospect_customer_fax_number = req.customer_fax_no
        _created_cust.gender_id = req.prospect_gender
        _created_cust.contact_person = req.contact_person_name
        _created_cust.job_title_id = 1  # FK to mtr_job_title from common-general service
        _created_cust.contact_mobile_phone = req.contact_person_mobile_phone
        _created_cust.contact_email_address = req.contact_person_email_addr
        _created_cust.keyword = req.search_keyword
        db.add(_created_cust)
        db.flush()
        db.refresh(_created_cust)
        return _created_cust.prospect_customer_system_number,None
    except Exception as err:
        db.rollback()
        return None,err

def create_prospect_document_number(hasil):
    curr_date = datetime.now()
    prefix_no = "SAPP"
    month_no = str(curr_date.month)
    year_no = str(curr_date.year - 2000)
    document_created = prefix_no + "/" + month_no + "/" + year_no + "/" +str(hasil)
    return document_created

def create_prospect_customer_code():
    prospect_code = "S"
    seq_no = str(math.ceil(numpy.random.rand()*100))
    return prospect_code + seq_no