from sqlalchemy import select, func
from src.entities.transaction.PDIRequestEntity import TrxPDIRequest
from src.entities.transaction.PDIRequestDetailEntity import TrxPDIRequestDetail
from src.entities.master.BrandEntity import MtrBrand
from src.entities.master.VehicleEntity import MtrVehicle
from src.entities.master.ModelVariantColourEntity import MtrModelVariantColour
# from src.entities.transaction.PDIStatusEntity import MtrPDIStatus
from src.payloads.schemas.transaction import PDIRequestSchema
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination, get_the_pagination_search_with_join
from datetime import datetime, date
import logging
from dataclasses import asdict


def get_all_pdi_requests(page:int, limit:int, query_of:list[str], query_by:list[str]):
    db = get_db()
    
    
    try:
        total_rows = db.query(TrxPDIRequest).count()
        total_pages  = int(total_rows/limit)

        #for pagination purposes
        query_check = get_the_pagination(TrxPDIRequest,query_of,query_by)   
        query_final = query_check.order_by(TrxPDIRequest.pdi_request_system_number).offset(page*limit).limit(limit)

        results = db.scalars(query_final).all()

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        
        return results, page_results, None
    except Exception as err:
        return None, None, err
    
    

def get_by_search_pdi_request(page:int,limit:int,all_params:dict()):
    db = get_db()
    try:    
        query_set = select(
            TrxPDIRequest.pdi_request_document_number,
            TrxPDIRequest.pdi_request_date,
            TrxPDIRequest.issued_by_id,
            TrxPDIRequest.service_dealer_id,
            MtrVehicle.vehicle_chassis_number,
            MtrModelVariantColour.model_variant_colour_description,
            TrxPDIRequest.pdi_request_status_id
        )
        join_tables = [TrxPDIRequestDetail, MtrVehicle, MtrModelVariantColour]

        query_check = get_the_pagination_search_with_join(query_set,all_params,TrxPDIRequest,join_tables)
        query_final = query_check.join(
            TrxPDIRequestDetail,
            TrxPDIRequest.pdi_request_system_number == TrxPDIRequestDetail.pdi_request_system_number
        ).join(
            MtrVehicle,
            TrxPDIRequestDetail.vehicle_id == MtrVehicle.vehicle_id
        ).join(
            MtrModelVariantColour,
            MtrVehicle.vehicle_variant_id == MtrModelVariantColour.variant_id
        ).order_by(TrxPDIRequest.pdi_request_system_number).offset(page*limit).limit(limit)


        data = db.execute(query_final).all()

        results=[]
        for pdi_request_document_number, pdi_request_date, issued_by_id, service_dealer_id, vehicle_chassis_number, model_variant_colour_description, pdi_request_status_id in data:
            go_out = {
                "pdi_request_document_number": pdi_request_document_number,
                "pdi_request_date": pdi_request_date,
                "issued_by_id": issued_by_id,
                "service_dealer_id": service_dealer_id,
                "vehicle_chassis_number": vehicle_chassis_number,
                "model_variant_colour_description": model_variant_colour_description,
                "pdi_request_status_id": pdi_request_status_id
            }
            results.append(go_out)

        total_rows = len(results)
        total_pages  = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }
        return results,page_results,None
    except Exception as err:
        logging.error("An error occurred: %s", str(err))

        
        error_response = {
            "error": "An error occurred while processing your request.",
            "details": str(err)
        }
        return None, None, error_response

def get_by_id_pdi_request(id: int):
    db = get_db()
    try:
        check_query = select(TrxPDIRequest).where(TrxPDIRequest.pdi_request_system_number==id)
        result = db.scalars(check_query).first()
        
        return result, None
    except Exception as err:
        return None, err
    
    
def get_full_detail_pdi_request_by_id(id: int):
    db = get_db()
    try:
        header_query = select(TrxPDIRequest).where(TrxPDIRequest.pdi_request_system_number == id)
        header_result = db.execute(header_query).scalar()


        detail_query = select(
                            MtrModelVariantColour.model_variant_colour_description,
                            TrxPDIRequestDetail.operation_number_id,
                            MtrVehicle.vehicle_chassis_number,
                            TrxPDIRequestDetail.estimated_delivery,
                            TrxPDIRequestDetail.frt,
                            TrxPDIRequestDetail.service_date,
                            TrxPDIRequestDetail.service_time,
                            TrxPDIRequestDetail.pdi_request_detail_line_status_id

                      ).join(TrxPDIRequest, TrxPDIRequestDetail.pdi_request_system_number == TrxPDIRequest.pdi_request_system_number
                      ).join(MtrVehicle, TrxPDIRequestDetail.vehicle_id == MtrVehicle.vehicle_id
                      ).join(MtrModelVariantColour, MtrVehicle.vehicle_variant_id == MtrModelVariantColour.variant_id
                      ).filter(TrxPDIRequestDetail.pdi_request_system_number==id)


        
        detail_data = db.execute(detail_query).all()

        detail_result = []

        for model_variant_colour_description, operation_number_id, vehicle_chassis_number, estimated_delivery, frt, service_date, service_time, pdi_request_detail_line_status_id in detail_data:
            go_out = {
                "model_variant_colour_description" : model_variant_colour_description,
                "operation_number_id" : operation_number_id,
                "vehicle_chassis_number" : vehicle_chassis_number,
                "estimated_delivery" : estimated_delivery,
                "frt" : frt,
                "service_date" : service_date,
                "service_time" : service_time,
                "pdi_request_detail_line_status_id" : pdi_request_detail_line_status_id

            }
            detail_result.append(go_out)

        return header_result, detail_result, None

    except Exception as err:
        logging.error("An error occurred: %s", str(err))

        error_response = {
            "error": "An error occurred while processing your request.",
            "details": str(err)
        }
        return None, None, error_response



    
def post_pdi_request_detail(req: TrxPDIRequestDetail):

    db = get_db()
    try:
        db.begin()
        _new_data = TrxPDIRequestDetail()
        _new_data.pdi_request_system_number = req.pdi_request_system_number
        _new_data.vehicle_id = req.vehicle_id
        _new_data.operation_number_id = req.operation_number_id
        _new_data.estimated_delivery = req.estimated_delivery
        _new_data.frt = req.frt
        _new_data.service_date = req.service_date
        _new_data.service_time = req.service_time
        _new_data.pdi_request_detail_line_status_id = req.pdi_request_detail_line_status_id 
        _new_data.pdi_request_detail_line_remark = req.pdi_request_detail_line_remark
        _new_data.pdi_request_detail_line_number = get_line_no(req.pdi_request_system_number)

        update_totalfrt_query = select(TrxPDIRequest).where(TrxPDIRequest.pdi_request_system_number==req.pdi_request_system_number)
        result_totalfrt = db.scalars(update_totalfrt_query).first()
        sum_detail_query = select(func.sum(TrxPDIRequestDetail.frt)).where(TrxPDIRequestDetail.pdi_request_system_number == req.pdi_request_system_number)
        result_sum_list = db.scalars(sum_detail_query).all()

        if result_sum_list :
            result_sum = result_sum_list[0] 
            result_int = int(result_sum)
            result_totalfrt.total_frt = result_int + req.frt
        else:
            result_totalfrt.total_frt = 0 


        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:

        db.rollback()
        return None, err



def get_line_no(id: int):
    db = get_db()
    try:
        max_result = db.query(
            func.max(TrxPDIRequestDetail.pdi_request_detail_line_number)
        ).filter(TrxPDIRequestDetail.pdi_request_system_number == id).scalar()

        if max_result is None:
            final_result = 1
        else:
            final_result = max_result + 1

        return final_result

    except Exception as err:
        logging.error("An error occurred: %s", str(err))

        error_response = {
            "error": "An error occurred while processing your request.",
            "details": str(err)
        }
        return None, error_response





def post_pdi_request(req: TrxPDIRequest):
    db = get_db()
    try:
        db.begin()
        _new_data = TrxPDIRequest()
        _new_data.brand_id = req.brand_id
        _new_data.pdi_request_document_number = get_doc_no(req.brand_id)
        _new_data.pdi_request_date = req.pdi_request_date
        _new_data.company_id = req.company_id
        _new_data.issued_by_id = req.issued_by_id
        _new_data.service_dealer_id = req.service_dealer_id
        _new_data.service_by_id = req.service_by_id
        _new_data.total_frt = req.total_frt
        _new_data.pdi_request_remark = req.pdi_request_remark

        db.add(_new_data)
        db.commit()

        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def get_doc_no(id:int):
    db = get_db()
    pdi_code = "SAPR"  # get from general-service document master
    current_date = datetime.now()
    period_month = current_date.month
    period_year = current_date.year - 2000

    try:
        # Generate code for document
        spec_code_query = select(MtrBrand.brand_name).where(MtrBrand.brand_id == id)
        
        spec_result = db.execute(spec_code_query).scalar()
        spec_generate = spec_result[0].upper()



        document_number_query = select(TrxPDIRequest.pdi_request_system_number)
       
        final_query = db.execute(document_number_query).all()
        document_number = len(final_query)

  

        if  document_number < 1:
            document_number += 1
            doc_format = f"{pdi_code}/{spec_generate}/{period_month}/{period_year}/{document_number:05}"

        else :
            document_number += 1
            doc_format = f"{pdi_code}/{spec_generate}/{period_month}/{period_year}/{document_number:05}"
       
        

        return doc_format

    except Exception as err:

        return None, err


def delete_pdi_request(id:int):
    db = get_db()
    try:
        query_check = select(TrxPDIRequest).where(TrxPDIRequest.pdi_request_system_number==id)
        erase_data = db.scalars(query_check).first()

        db.delete(erase_data)
        db.commit()

        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err


class WorkOrderNotCreatedError(Exception):
    pass

class PDIInvoiceNotCreatedError(Exception):
    pass

class PDIInvoiceStatusError(Exception):
    pass


def patch_pdi_request(pdi_request_system_number:int, pdi_request_detail_line_number:int):
    db = get_db()
    try:
        check_validate = select(TrxPDIRequestDetail
                        ).where((TrxPDIRequestDetail.pdi_request_system_number==pdi_request_system_number)
                                & (TrxPDIRequestDetail.pdi_request_detail_line_number == pdi_request_detail_line_number))

        check_result = db.scalars(check_validate).first()

 
        current_wo = check_result.work_order_system_number
        current_inv = check_result.invoice_payable_system_no

        #dapat digunakan hanya kasus bila service telah dihubungkan
        # query_status = select(MtrPDIStatus).where(MtrPDIStatus.pdi_status_description == 'CLOSED')
        # status_result = db.scalar(query_status)

        #Data dummy sementara untuk run code
        query_status = "CLOSED"
        if query_status == "CLOSED":
            status_id = 4
        elif query_status == "ACCEPT":
            status_id = 5

        inv_status = 'APPROVED'

        if current_wo is None or current_wo == 0:
            raise WorkOrderNotCreatedError("Work Order has not been created for this PDI. Please proceed to creating Work Order for this PDI before continuing.")
        elif current_inv is None or current_inv == 0 :
            raise PDIInvoiceNotCreatedError("PDI is not Invoiced yet. Please proceed to creating Invoice Work Order for this PDI before continuing.")
            ## Validasi mengharuskan untuk mengecek data INV_SYS_NO pada wtWorkorder2, dimana untuk saat ini wtWorkOrder2 belum dibuat
        elif inv_status == 'DRAFT':
            raise PDIInvoiceStatusError("Invoice Process is not completed (DRAFT). Please proceed to process Invoice Work Order for this PDI before continuing.")
        else : 
            # check_result.pdi_request_detail_line_status_id = status_result.pdi_status_id
            check_result.pdi_request_detail_line_status_id = status_id

        db.commit()
        db.refresh(check_result)

        return check_result, None


    except Exception as err:
        db.rollback()
        return None, err