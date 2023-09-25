from sqlalchemy.orm import Session
from src.entities.transaction.VehicleSalesOrderTakeEntity import TrxVehicleSalesOrderTake as spmtake
from src.entities.transaction.VehicleSalesOrderTakeDetailEntity import TrxVehicleSalesOrderTakeDetail as spmtakedetail
from src.entities.transaction.VehicleSalesOrderFormRegistrationEntity import TrxVehicleSalesOrderFormRegistration as spmreg
from src.entities.transaction.VehicleSalesOrderFormRegistrationDetailEntity import TrxVehicleSalesOrderFormRegistrationDetail as spmregdetail
from src.payloads.schemas.transaction.PreprintedSpmTakeSchema import TrxSpmFormTakeRequestDetail
from sqlalchemy import select,delete
from sqlalchemy.orm import load_only
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination_search,get_the_pagination_search_spm
from datetime import datetime
import math

async def get_spm_takes_search(db:Session,page:int,limit:int,all_params:dict()):
    #claims
    company_id = 1

    if page <= 0:
        page = 1
    try:
        query_set = select(spmtake.taken_system_number,
                           spmtake.taken_document_number,
                           spmtake.spm_issued_to,
                           spmtake.spm_issued_date,
                           spmtake.spm_issued_by,
                           spmtakedetail.vehicle_sales_order_document_number).join(
            spmtakedetail,spmtake.taken_system_number==spmtakedetail.taken_system_number)
        query_check,counter = await get_the_pagination_search(db,query_set,all_params)
        query_check =  query_check.order_by(spmtake.taken_document_number).offset((page*limit)-limit).limit(limit)
        results = db.execute(query_check).all()

        total_rows = len(results)
        total_pages = math.ceil(counter/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }

        finalresults = []
        for taken_id,taken_doc,issued_to,issued_date,issued_by,spm_doc_no in results:

            #get from the user-service using API
            get_issued_to_id = "50642"
            get_issued_by_id = "50655"
            data = {
                "taken_system_number":taken_id,
                "taken_document_number": taken_doc,
                "spm_issued_to": get_issued_to_id,
                "spm_issued_date": issued_date,
                "spm_issued_by": get_issued_by_id,
                "vehicle_sales_order_document_number":spm_doc_no
            }
            finalresults.append(data)

        return finalresults, page_results, None
    except Exception as err:
        return None, None, err
    
async def get_all_spm_takes_assigned(db:Session,page:int, limit:int):
    #claims
    company_id = 1
    issued_by = 1
    issued_to = 1 # call API from user service to get employee number, name, role/position, and status

    all_params = {
        "company_id" : company_id,
        "spm_issued_by" : issued_by,
        "spm_issued_to" : issued_to
    }

    if page <= 0:
        page = 1
    try:
        query_set = select(spmtakedetail).join(spmtake)
        query_check,counter = await get_the_pagination_search(db,query_set,all_params)
        query_final = query_check.order_by(spmtakedetail.vehicle_sales_order_document_number).offset((page*limit)-limit).limit(limit).options(
            load_only(
            spmtake.taken_document_number
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
    

async def get_all_spm_take_by_id(db:Session,get_id:int,page:int,limit:int) :
    try:
        #header
        query_header = select(spmtake).where(spmtake.taken_system_number==get_id)
        header_result = db.scalars(query_header).first()

        #detail
        query_detail = select(spmtakedetail).join(spmtake,spmtake.taken_system_number==spmtakedetail.taken_system_number).where(spmtakedetail.taken_system_number==get_id)
        query_detail = query_detail.order_by(spmtakedetail.taken_detail_system_number).offset(page*limit).limit(limit).options(
            load_only(spmtakedetail.vehicle_sales_order_document_number,
                      spmtakedetail.vehicle_sales_order_system_number))

        detail_result = db.scalars(query_detail).all()

        n_data = len(detail_result)

        total_rows = n_data
        total_pages = int(total_rows/limit)  

        pages = {
            "total_rows":total_rows,
            "total_pages":total_pages
        }  

        return header_result,detail_result,pages,None
    except Exception as err:
        return None,None,None,err


async def post_taken_spm(db:Session,req_data:TrxSpmFormTakeRequestDetail):
    inp_data = spmtake()
    
    #claims
    taken_system_number_old = 1
    req_data_spm_issued_by = 1 # get from user-service

    company_id = 1
    taken_document_number = "xx"
    brand_id = 1
    inp_data.print_counter = 0

    try:
        db.begin()
        inp_data.company_id = company_id
        inp_data.taken_document_number = taken_document_number
        inp_data.brand_id = brand_id
        inp_data.spm_issued_date = datetime.now()
        inp_data.spm_issued_by = req_data_spm_issued_by
        inp_data.spm_issued_to = req_data.spm_issued_to # get from user-service
        inp_data.total_spm_taken = 0
        inp_data.taken_system_number_old = taken_system_number_old
       
        db.add(inp_data)
        db.flush()

        allocation_spm = []
        vehicle_sales_order_system_number = []
        get_object = req_data.spm_list
        for get_alloc_spm in get_object:
            allocation_spm.append(get_alloc_spm.vehicle_sales_order_document_number)
            vehicle_sales_order_system_number.append(get_alloc_spm.vehicle_sales_order_system_number)

        status_created,err = await post_detail_taken_spm(db,inp_data.taken_system_number,
                                                         allocation_spm,
                                                         vehicle_sales_order_system_number)

        if status_created == True:
            db.commit()
            db.refresh(inp_data)
            return inp_data,None
        else:
            db.rollback()
            return None,err

    except Exception as err:
        db.rollback()
        return None, err

async def post_detail_taken_spm(db:Session,id_spm_take:int,allocated_spm:list[str],vehicle_sales_order_system_number:list[int]):
    try:
        for idx in range(len(allocated_spm)):
            spm_take_detail = spmtakedetail()
            spm_take_detail.taken_detail_system_number_old = 1 
            spm_take_detail.vehicle_sales_order_system_number = vehicle_sales_order_system_number[idx]
            spm_take_detail.taken_system_number = id_spm_take
            spm_take_detail.vehicle_sales_order_document_number = allocated_spm[idx]
            db.add(spm_take_detail)
        db.flush()
        db.refresh(spm_take_detail)
        return True,None
    except Exception as err:
        return False,err

async def update_detail_taken_spm(db:Session,id:int,rev_data:TrxSpmFormTakeRequestDetail):
    try:
        db.begin()
        query_init = select(spmtake).where(spmtake.taken_system_number==id)
        update_data = db.scalars(query_init).first()
        update_data.spm_issued_date = datetime.now()

        query_detail = select(spmtakedetail.vehicle_sales_order_document_number).where(spmtakedetail.taken_system_number==id)
        spm_take_detail = db.scalars(query_detail).all()
        get_list = []
        rev_list = []
        for idx_spm_data in range(len(spm_take_detail)):
            get_list.append(spm_take_detail[idx_spm_data])
            rev_list.append(rev_data.spm_list[idx_spm_data].vehicle_sales_order_document_number)

        if (get_list != rev_list) or (update_data.spm_issued_to != rev_data.spm_issued_to):
            #insert mode on
            update_data.spm_issued_to = rev_data.spm_issued_to
            del_query = delete(spmtakedetail).where(spmtakedetail.taken_system_number==id)
            db.execute(del_query)
            db.flush()

        allocation_spm = []
        vehicle_sales_order_system_number = []
        get_object = rev_data.spm_list
        for get_alloc_spm in get_object:
            allocation_spm.append(get_alloc_spm.vehicle_sales_order_document_number)
            vehicle_sales_order_system_number.append(get_alloc_spm.vehicle_sales_order_system_number)

        status_created,err = await post_detail_taken_spm(db,id,
                                                    allocation_spm,
                                                    vehicle_sales_order_system_number)
        if status_created == True:
            db.commit()
            db.refresh(update_data)
            return update_data,None
        else:
            db.rollback()
            return None, err
    except Exception as err:
        db.rollback()
        return None,err
    
async def get_available_spm_doc_no_by_id(db:Session,id:int):
    try:
        query_set = select(spmregdetail).where(spmregdetail.spm_form_registration_detail_id==id).options(load_only(
            spmregdetail.spm_form_registration_detail_id,
            spmregdetail.spm_document_number
        ))
        results = db.scalars(query_set).first()
        return results,None
    except Exception as err:
        return None,err

async def get_available_spm_doc_no(db:Session,page:int,limit:int,all_params:dict()):
    #claims
    company_id = 1
    if page <= 0:
        page = 1
    try:    
        query_set = select(spmregdetail).join(spmreg,isouter=True).join(
            spmtakedetail,spmtakedetail.vehicle_sales_order_document_number==spmregdetail.spm_document_number,isouter=True
        ).where(
            spmreg.company_id==company_id).where(
            spmtakedetail.vehicle_sales_order_document_number==None)
        
        query_check,counter = await get_the_pagination_search_spm(db,query_set,all_params)
        query_final = query_check.order_by(spmregdetail.spm_document_number).offset((page*limit)-limit).limit(limit).options(
            load_only(
            spmregdetail.register_system_number_id,
            spmregdetail.spm_document_number
        ))

        results = db.scalars(query_final).all()

        total_rows = counter
        total_pages = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results,page_results,None
    except Exception as err:
        return None, None, err
    
async def submit_preprinted_spm_taken(db:Session,id:int):
    try:
        db.begin()
        query_init = select(spmtake).where(spmtake.taken_system_number==id)
        updated_data = db.scalars(query_init).first()
        if updated_data.taken_document_number == "xx":
            document_number = create_taken_documents_number(updated_data.taken_system_number)
            updated_data.taken_document_number = document_number
            db.commit()
            db.refresh(updated_data)
            return updated_data, None
        else:
            db.rollback()
            return None, err
    except Exception as err:
        db.rollback()
        return None, err
    
async def delete_spm_taken_assigned(db:Session,deleted_spm:dict()):
    try:
        db.begin()
        for del_id in deleted_spm.taken_detail_system_number:
            query_del = delete(spmtakedetail).where(spmtakedetail.taken_detail_system_number==del_id)
            db.execute(query_del)
        db.commit()
        return None
    except Exception as err:
        db.rollback()
        return err

def create_taken_documents_number(id:int):
    SD = 'SMPTK' # get from mtr_document general service
    BR = 'N' # get from mtr_document general service
    N = id # get last document number from general service
    dateyear = datetime.now()
    M = dateyear.month
    Y = dateyear.year - 2000
    document_generated = SD + "/" + BR + "/" + str(M) + "/" + str(Y) + "/" + str(N).zfill(int(5))
    return document_generated