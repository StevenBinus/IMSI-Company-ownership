from sqlalchemy import select
from sqlalchemy.orm import load_only, Session
from src.entities.transaction.VehicleSalesOrderFormRegistrationEntity import TrxVehicleSalesOrderFormRegistration as vehiclesalesorderform
from src.entities.transaction.VehicleSalesOrderFormRegistrationDetailEntity import TrxVehicleSalesOrderFormRegistrationDetail as vehiclesalesorderdetail
from src.payloads.schemas.transaction import PreprintedSpmRegisterSchema
from datetime import datetime
import calendar
from src.utils.AddPagination import get_the_pagination_search
import math

async def get_header_preprinted_spm_register_search(db:Session,page:int,limit:int,all_params:dict()):
    if page <= 0:
        page = 1
    try:    
        query_set = select(vehiclesalesorderform)
        query_check,counter = await get_the_pagination_search(db,query_set,all_params)
        query_final = query_check.order_by(vehiclesalesorderform.register_system_number).offset((page*limit)-limit).limit(limit).options(
            load_only(
            vehiclesalesorderform.register_document_number,
            vehiclesalesorderform.spm_received_by,
            vehiclesalesorderform.spm_received_date,
            vehiclesalesorderform.spm_number_format,
            vehiclesalesorderform.total_spm,
            vehiclesalesorderform.spm_number_from
        ))
        results = db.scalars(query_final).all()
        total_rows = len(results)
        total_pages  = math.ceil(counter/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        return results,page_results,None
    except Exception as err:
        return None, None, err
    
async def get_header_preprinted_spm_register_by_id(db:Session,id:int):
    try:
        #header
        query_get_by_id = select(vehiclesalesorderform).where(vehiclesalesorderform.register_system_number==id)
        header_result = db.scalars(query_get_by_id).first()
        #detail
        query_get_by_id = select(vehiclesalesorderdetail
            ).join(vehiclesalesorderform).where(
            vehiclesalesorderform.register_system_number==id 
            ).options(load_only(
            vehiclesalesorderdetail.spm_document_number
            ))
        detail_result = db.scalars(query_get_by_id).all()        
        return header_result, detail_result, None
    except Exception as err:
        return None,None, err

async def post_preprinted_spm_register(db:Session,request_data:PreprintedSpmRegisterSchema.SpmFormRegisterRequest):
    try:
        db.begin()
        _preprinted_register = vehiclesalesorderform()
        _preprinted_register.company_id = request_data.company_id
        _preprinted_register.register_document_number = get_doc_no()
        _preprinted_register.spm_received_by = request_data.spm_received_by
        inp_data = request_data.spm_received_date.strftime("%Y-%m-%d")
        _preprinted_register.spm_received_date = inp_data
        _preprinted_register.spm_number_format = request_data.spm_number_format
        _preprinted_register.spm_number_from = request_data.spm_number_from
        _preprinted_register.total_spm = request_data.total_spm
        _preprinted_register.reference_document_number = request_data.reference_document_number
        db.add(_preprinted_register)
        db.commit()

        doc_generated = new_preprinted_spm_register(_preprinted_register.spm_number_format,
                                                    _preprinted_register.spm_number_from,
                                                    _preprinted_register.total_spm)
        for doc in doc_generated:
            _inp_data = vehiclesalesorderdetail()
            _inp_data.register_system_number_id = _preprinted_register.register_system_number
            _inp_data.register_document_number = 0
            _inp_data.spm_document_number = doc
            _inp_data.last_taken_system_number = 0
            _inp_data.last_return_system_number = 0
            _inp_data.last_spm_status = "None"
            _data_detail_spm = await post_detail_preprinted_spm_register(inp_data)
            db.add(_data_detail_spm)
        db.commit()
        db.refresh(_data_detail_spm)
        db.refresh(_preprinted_register)
        return _preprinted_register,None
    except Exception as err:
        db.rollback()
        return None,err

async def get_detail_preprinted_spm_register(db:Session):
    try:
        query_results = select(vehiclesalesorderdetail)
        results = db.scalars(query_results).all()
        return results, None
    except Exception as err:
        return None, err
    
async def post_detail_preprinted_spm_register(req_detail:PreprintedSpmRegisterSchema.SPMFormRegisterDetailRequest):
    _form_detail = vehiclesalesorderdetail()
    _form_detail.register_system_number_id = req_detail.register_system_number_id
    _form_detail.register_document_number = req_detail.register_document_number
    _form_detail.spm_document_number = req_detail.spm_document_number
    _form_detail.last_taken_system_number = req_detail.last_taken_system_number
    _form_detail.last_return_system_number = req_detail.last_return_system_number
    _form_detail.last_spm_status = req_detail.last_spm_status
    return _form_detail

def new_preprinted_spm_register(spm_form_format:str,start_from:int,total:int):
    check_M = spm_form_format.find("@M2")
    check_Y = spm_form_format.find("@Y4")
    check_N = spm_form_format.find("@N")
    curr_date = datetime.now()
    month_fmt = curr_date.month
    year_fmt = curr_date.year
    num_digits = spm_form_format[check_N+2]

    spm_month = spm_form_format.replace("@M3",calendar.month_abbr[month_fmt]) if check_M==-1 else spm_form_format.replace("@M2",format(curr_date,"%m"))
    spm_year = spm_month.replace("@Y2",str(year_fmt-2000)) if check_Y==-1 else spm_month.replace("@Y4",format(curr_date,"%Y"))

    document_generated = []
    end_to = total + start_from
    for idx in range(start_from,end_to):
        document_generated.append(spm_year.replace(spm_form_format[check_N:check_N+3],str(idx).zfill(int(num_digits))))  
    return document_generated

# create function to get from general service then combine to create the results
def get_doc_no():
    SPM_doc = "SMPRG" # get from general-service document master
    current_date = datetime.now()
    period_month = current_date.month
    period_year = current_date.year - 2000

    #parameters
    Spec_code = 'N' # get from general-service document master
    total_spm = 2
    doc_format = SPM_doc + "/" + Spec_code + "/" + str(period_month) + "/" + str(period_year) + "/" + str(total_spm).zfill(int(5))
    return doc_format