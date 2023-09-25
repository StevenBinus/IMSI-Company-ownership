from fastapi import Request
from sqlalchemy import select, column, extract, func
from sqlalchemy.orm import load_only
from src.entities.transaction.UnitPurchaseOrderBBNEntity import TrxUnitPurchaseOrderBBN
from src.entities.transaction.UnitPurchaseOrderBBNDetailEntity import TrxUnitPurchaseOrderBBNDetail
from src.entities.transaction.UnitPurchaseOrderBBNCostDetailEntity import TrxUnitPurchaseOrderBBNCostDetail
from src.entities.master.VehicleEntity import MtrVehicle
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNRequest, TrxUnitPurchaseOrderBBNDetailRequest
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNRequestUpdate, TrxUnitPurchaseOrderBBNCostDetailRequest
from src.payloads.schemas.transaction.UnitPurchaseOrderBBNSchema import TrxUnitPurchaseOrderBBNCostDetailRequestUpdate
from src.entities.master.BrandEntity import MtrBrand
from src.configs.database import get_db
from src.utils.AddPagination import get_the_pagination, get_the_pagination_search_with_join
from datetime import datetime, date
import logging
from dataclasses import asdict
import requests

def get_unit_purchase_order_bbn_search(page:int,limit:int,all_params:dict()):
    db = get_db()
    try:    
        query_set = select(
            TrxUnitPurchaseOrderBBN.purchase_order_bbn_document_number,
            TrxUnitPurchaseOrderBBN.purchase_order_date,
            TrxUnitPurchaseOrderBBN.supplier_id,
            MtrBrand.brand_name,
            MtrVehicle.vehicle_chassis_number,
            TrxUnitPurchaseOrderBBN.purchase_order_status_id
        )
        join_tables = [TrxUnitPurchaseOrderBBNDetail, MtrBrand, MtrVehicle]

        query_check = get_the_pagination_search_with_join(query_set,all_params,TrxUnitPurchaseOrderBBN,join_tables)
        query_final = query_check.join(
            TrxUnitPurchaseOrderBBNDetail,
            TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number
        ).join(
            MtrBrand,
            TrxUnitPurchaseOrderBBN.brand_id == MtrBrand.brand_id
        ).join(
            MtrVehicle,
            TrxUnitPurchaseOrderBBNDetail.vehicle_id == MtrVehicle.vehicle_id
        ).order_by(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number).offset(page*limit).limit(limit)

        data = db.execute(query_final).all()

        results=[]
        for purchase_order_bbn_document_number, purchase_order_date, supplier_id, brand_name, vehicle_chassis_number, purchase_order_status_id in data:
            go_out = {
                "purchase_order_bbn_document_number": purchase_order_bbn_document_number,
                "purchase_order_date": purchase_order_date,
                "supplier_id": supplier_id,
                "brand_name": brand_name,
                "vehicle_chassis_number": vehicle_chassis_number,
                "purchase_order_status_id": purchase_order_status_id,
            }
            results.append(go_out)

        for result in results:
            id_supplier = result["supplier_id"]
            supplier_url = f"http://10.1.32.26:8000/general-service/api/general/supplier-master/{id_supplier}"
            id_approval = result["purchase_order_status_id"] 
            approval_status_url = f"http://10.1.32.26:8000/general-service/api/general/approval-status/{id_approval}"
            try:
                supplier_response = requests.get(supplier_url)
                supplier_data = supplier_response.json()
                result["supplier_name"] = result.pop("supplier_id")
                result["supplier_name"] = supplier_data["data"]["supplier_name"]

                approval_status_response = requests.get(approval_status_url)
                approval_data = approval_status_response.json()
                result["purchase_order_status_description"] = result.pop("purchase_order_status_id")
                result["purchase_order_status_description"] = approval_data["data"]["approval_status_description"]

            except Exception:
                print(Exception)

        total_rows = len(results)
        total_pages  = int(total_rows/limit)

        page_results = {
            "total_rows" : total_rows,
            "total_pages" : total_pages
        }

        return results,page_results,None
    except Exception as err:
        return None, None, err

def post_unit_purchase_order_bbn(req: TrxUnitPurchaseOrderBBNRequest):
    db = get_db()
    try:
        db.begin()
        _new_data = TrxUnitPurchaseOrderBBN()
        _new_data.company_id = req.company_id
        _new_data.dealer_representative_id = req.dealer_representative_id
        _new_data.cost_center_id = req.cost_center_id
        _new_data.purchase_order_date = req.purchase_order_date
        _new_data.purchase_order_remark = req.purchase_order_remark
        _new_data.brand_id = req.brand_id
        _new_data.supplier_id = req.supplier_id
        _new_data.term_of_payment_id = req.term_of_payment_id
        _new_data.bill_code_id = req.bill_code_id
        _new_data.down_payment_request = req.down_payment_request
        
        cost_center_url = f"http://10.1.32.26:8000/general-service/api/general/get-master-cost-center/{req.cost_center_id}"
        cost_center_response = requests.get(cost_center_url)
        cost_center_data = cost_center_response.json()

        supplier_url = f"http://10.1.32.26:8000/general-service/api/general/supplier-master/{req.supplier_id}"
        supplier_response = requests.get(supplier_url)
        supplier_data = supplier_response.json()

        if cost_center_data['message'] != "Success" or supplier_data['status_code'] != 200:
            raise Exception

        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def post_unit_purchase_order_bbn_detail(req: TrxUnitPurchaseOrderBBNDetailRequest):
    db = get_db()
    try:
        db.begin()
        _new_data = TrxUnitPurchaseOrderBBNDetail()
        _new_data.purchase_order_bbn_system_number = req.purchase_order_bbn_system_number
        _new_data.vehicle_id = req.vehicle_id
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def post_unit_purchase_order_bbn_cost_detail(req: TrxUnitPurchaseOrderBBNCostDetailRequest):
    db = get_db()
    try:
        db.begin()
        _new_data = TrxUnitPurchaseOrderBBNCostDetail()
        _new_data.purchase_order_bbn_detail_system_number = req.purchase_order_bbn_detail_system_number
        _new_data.cost_type_id = req.cost_type_id
        _new_data.cost_amount = req.cost_amount
        _new_data.vat_charged = req.vat_charged
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)

        # update trx_unit_purchase_order_bbn_detail
        update_price_unit_purchase_order_bbn_detail(req.purchase_order_bbn_detail_system_number)

        # update trx_unit_purchase_order_bbn
        update_price_unit_purchase_order_bbn(req.purchase_order_bbn_detail_system_number)

        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def get_unit_purchase_order_bbn_by_id(id: int):
    db = get_db()
    try:
        header_query = select(TrxUnitPurchaseOrderBBN).where(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == id)
        header_result = db.scalars(header_query).first()

        detail_query = select(
            MtrVehicle.vehicle_chassis_number,
            MtrVehicle.vehicle_engine_number,
            TrxUnitPurchaseOrderBBNDetail.purchase_price
        ).join(
            MtrVehicle,
            TrxUnitPurchaseOrderBBNDetail.vehicle_id == MtrVehicle.vehicle_id
        ).where(TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number == id)
        detail_data = db.execute(detail_query).all()

        detail_result = []
        for vehicle_chassis_number, vehicle_engine_number, purchase_price in detail_data:
            go_out = {
                "vehicle_chassis_number": vehicle_chassis_number,
                "vehicle_engine_number": vehicle_engine_number,
                "purchase_price": purchase_price
            }
            detail_result.append(go_out)
        
        return header_result, detail_result, None
    except Exception as err:
        return None, None, err

def get_unit_purchase_order_bbn_detail_by_id(id: int):
    db = get_db()
    try:
        detail_query = select(
            MtrVehicle.vehicle_chassis_number,
            MtrVehicle.vehicle_engine_number,
            TrxUnitPurchaseOrderBBN.supplier_id,
            TrxUnitPurchaseOrderBBNDetail.purchase_price
        ).join(
            MtrVehicle,
            TrxUnitPurchaseOrderBBNDetail.vehicle_id == MtrVehicle.vehicle_id
        ).join(
            TrxUnitPurchaseOrderBBN,
            TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number == TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number
        ).where(TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_detail_system_number == id)
        detail_data = db.execute(detail_query).all()

        detail_result = []

        for vehicle_chassis_number, vehicle_engine_number, supplier_id, purchase_price in detail_data:
            go_out = {
                "vehicle_chassis_number": vehicle_chassis_number,
                "vehicle_engine_number": vehicle_engine_number,
                "supplier_id": supplier_id,
                "purchase_price": purchase_price
            }
            detail_result.append(go_out)

        detail_final = detail_result[0]

        id_supplier = detail_final["supplier_id"]
        supplier_url = f"http://10.1.32.26:8000/general-service/api/general/supplier-master/{id_supplier}"

        try:
            supplier_response = requests.get(supplier_url)
            supplier_data = supplier_response.json()
            detail_final["supplier_name"] = detail_final.pop("supplier_id")
            detail_final["supplier_name"] = supplier_data["data"]["supplier_name"]
        except Exception:
            print(Exception)

        cost_detail_query = select(
            TrxUnitPurchaseOrderBBNCostDetail.purchase_order_bbn_cost_detail_system_number,
            TrxUnitPurchaseOrderBBNCostDetail.cost_type_id,
            TrxUnitPurchaseOrderBBNCostDetail.cost_amount,
            TrxUnitPurchaseOrderBBNCostDetail.vat_charged
        ).where(TrxUnitPurchaseOrderBBNCostDetail.purchase_order_bbn_detail_system_number == id)
        cost_detail_result = db.execute(cost_detail_query).all()

        cost_detail_final = []
        for purchase_order_bbn_cost_detail_system_number, cost_type_id, cost_amount, vat_charged in cost_detail_result:
            cost_go_out = {
                "purchase_order_bbn_cost_detail_system_number": purchase_order_bbn_cost_detail_system_number,
                "cost_type_id": cost_type_id,
                "cost_amount": cost_amount,
                "vat_charged": vat_charged
            }
            cost_detail_final.append(cost_go_out)

        detail_final["cost_detail"] = cost_detail_final

        return detail_final, None
    except Exception as err:
        return None,  err

def get_unit_purchase_order_bbn_cost_detail_by_id(id: int):
    db = get_db()
    try:
        query_check = select(TrxUnitPurchaseOrderBBNCostDetail).where(TrxUnitPurchaseOrderBBNCostDetail.purchase_order_bbn_cost_detail_system_number == id)
        result = db.scalars(query_check).first()

        return result, None
    except Exception as err:
        return None, err

def update_unit_purchase_order_bbn(id: int, req: TrxUnitPurchaseOrderBBNRequestUpdate):
    db = get_db()
    check_data = select(TrxUnitPurchaseOrderBBN).where(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.purchase_order_date = req.purchase_order_date
        updated_data.purchase_order_remark = req.purchase_order_remark
        updated_data.down_payment_request = req.down_payment_request
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def update_unit_purchase_order_bbn_cost_detail(id: int, req: TrxUnitPurchaseOrderBBNCostDetailRequestUpdate):
    db = get_db()
    check_data = select(TrxUnitPurchaseOrderBBNCostDetail).where(TrxUnitPurchaseOrderBBNCostDetail.purchase_order_bbn_cost_detail_system_number == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.cost_type_id = req.cost_type_id
        updated_data.cost_amount = req.cost_amount
        updated_data.vat_charged = req.vat_charged
        db.commit()
        db.refresh(updated_data)

        # update trx_unit_purchase_order_bbn_detail
        update_price_unit_purchase_order_bbn_detail(updated_data.purchase_order_bbn_detail_system_number)

        # update trx_unit_purchase_order_bbn
        update_price_unit_purchase_order_bbn(updated_data.purchase_order_bbn_detail_system_number)

        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def patch_submit_unit_purchase_order_bbn_approval_status(id: int):
    db = get_db()
    check_data = select(TrxUnitPurchaseOrderBBN).where(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.purchase_order_status_id = 2
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def patch_approve_unit_purchase_order_bbn_approval_status(id: int):
    db = get_db()
    check_data = select(TrxUnitPurchaseOrderBBN).where(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.purchase_order_status_id = 3
        updated_data.purchase_order_bbn_document_number = get_doc_no(updated_data.brand_id)
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err

def patch_close_order_unit_purchase_order_bbn_approval_status(id: int):
    db = get_db()
    check_data = select(TrxUnitPurchaseOrderBBN).where(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == id)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.purchase_order_status_id = 4
        db.commit()
        db.refresh(updated_data)
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err
    
def delete_unit_purchase_order_bbn_cost_detail(id: int):
    db = get_db()
    try:
        query_check = select(TrxUnitPurchaseOrderBBNCostDetail).where(TrxUnitPurchaseOrderBBNCostDetail.purchase_order_bbn_cost_detail_system_number == id)
        deleted_data = db.scalars(query_check).first()

        db.delete(deleted_data)
        db.commit()

        detail_id = deleted_data.purchase_order_bbn_detail_system_number

        update_price_unit_purchase_order_bbn_detail(detail_id)

        update_price_unit_purchase_order_bbn(detail_id)

        return deleted_data, None
    except Exception as err:
        db.rollback()
        return None, err

def delete_unit_purchase_order_bbn_detail(id: int):
    db = get_db()
    try:
        query_delete_cost_detail = select(TrxUnitPurchaseOrderBBNCostDetail).where(TrxUnitPurchaseOrderBBNCostDetail.purchase_order_bbn_detail_system_number == id)
        cost_detail_deleted_datas = db.scalars(query_delete_cost_detail).all()

        for cost_detail_deleted_data in cost_detail_deleted_datas:
            db.delete(cost_detail_deleted_data)
            db.commit()

        query_delete_detail = select(TrxUnitPurchaseOrderBBNDetail).where(TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_detail_system_number == id)
        detail_deleted_data = db.scalars(query_delete_detail).first()

        db.delete(detail_deleted_data)
        db.commit()

        query_check = select(TrxUnitPurchaseOrderBBN).where(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == detail_deleted_data.purchase_order_bbn_system_number)
        header_data = db.scalars(query_check).first()

        header_data.net_amount -= detail_deleted_data.purchase_order_line_net_amount
        header_data.total_after_vat -= detail_deleted_data.purchase_price

        db.commit()
        db.refresh(header_data)

        return detail_deleted_data, None
    except Exception as err:
        db.rollback()
        return None, err

# Yang dibawah ini tidk dipanggil service, dipakai di file ini saja

def get_doc_no(id: int):
    db = get_db()
    bbn_code = "SABO"
    current_date = datetime.now()
    period_month = current_date.month
    period_year = current_date.year - 2000
    try:
        spec_code_query = select(MtrBrand.brand_name).where(MtrBrand.brand_id == id)
        spec_result = db.execute(spec_code_query).scalar()
        spec_generate = spec_result[0].upper()
        document_number_query = select(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number)
        final_query = db.execute(document_number_query).all()
        document_number = len(final_query)
        if  document_number < 1:
            document_number += 1
            doc_format = f"{bbn_code}/{spec_generate}/{period_month}/{period_year}/{document_number:05}"
        else :
            document_number += 1
            doc_format = f"{bbn_code}/{spec_generate}/{period_month}/{period_year}/{document_number:05}"

        return doc_format
    except Exception as err:
        return None, err
    
def get_line_net_amount_and_purchase_price(id: int):
    db = get_db()
    try:
        query = select(
            TrxUnitPurchaseOrderBBNCostDetail.cost_amount,
            TrxUnitPurchaseOrderBBNCostDetail.vat_charged
        ).where(TrxUnitPurchaseOrderBBNCostDetail.purchase_order_bbn_detail_system_number == id)
        query_exec = db.execute(query).all()
        line_net_amount = 0
        purchase_price = 0
        for data in query_exec:
            line_net_amount += data[0]
            if data[1] == 1:
                price_after_tax = data[0] * 1.11
            else:
                price_after_tax = data[0]
            purchase_price += price_after_tax

        return line_net_amount, purchase_price
        
    except Exception:
        return Exception

def get_net_amount_and_total_after_vat(id: int):
    db = get_db()
    try:
        query_check = select(
            TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number
        ).where(TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_detail_system_number == id)
        query_execute = db.execute(query_check).first()
        id_header = query_execute[0]

        query = select(
            TrxUnitPurchaseOrderBBNDetail.purchase_order_line_net_amount,
            TrxUnitPurchaseOrderBBNDetail.purchase_price
        ).where(TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number == id_header)
        query_exec = db.execute(query).all()
        net_amount = 0
        total_after_vat = 0
        for data in query_exec:
            net_amount += data[0]
            total_after_vat += data[1]

        return id_header, net_amount, total_after_vat

    except Exception:
        return Exception

def update_price_unit_purchase_order_bbn_detail(id: int):
    db = get_db()
    check_data = select(TrxUnitPurchaseOrderBBNDetail).where(TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_detail_system_number == id)
    updated_data = db.scalars(check_data).first()
    linet_net_amount, price_after_tax = get_line_net_amount_and_purchase_price(id)
    try:
        updated_data.purchase_order_line_net_amount = linet_net_amount
        updated_data.purchase_price = price_after_tax
        db.commit()
        db.refresh(updated_data)
    except Exception:
        print(Exception)

def update_price_unit_purchase_order_bbn(id: int):
    db = get_db()
    id_header, net_amount, total_after_vat = get_net_amount_and_total_after_vat(id)
    check_data = select(TrxUnitPurchaseOrderBBN).where(TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == id_header)
    updated_data = db.scalars(check_data).first()
    try:
        updated_data.net_amount = net_amount
        updated_data.total_after_vat = total_after_vat
        db.commit()
        db.refresh(updated_data)
    except Exception:
        print(Exception)