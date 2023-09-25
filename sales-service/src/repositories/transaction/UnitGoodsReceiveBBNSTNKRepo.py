from fastapi import Request
from sqlalchemy import select, column, extract, func
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.entities.transaction.UnitGoodsReceiveBBNSTNKEntity import TrxUnitGoodsReceiveBBNSTNK
from src.entities.master.VehicleEntity import MtrVehicle
from src.entities.transaction.UnitPurchaseOrderBBNDetailEntity import TrxUnitPurchaseOrderBBNDetail
from src.entities.transaction.UnitPurchaseOrderBBNEntity import TrxUnitPurchaseOrderBBN
from src.entities.master.UnitModelEntity import MtrUnitModel
from src.entities.master.UnitVariantEntity import MtrUnitVariant
from src.entities.master.UnitColourEntity import MtrColour
from src.entities.master.VariantCylinderEntity import MtrVariantCylinder
from src.entities.master.VariantFuelEntity import MtrVariantFuel
from src.payloads.schemas.transaction.UnitGoodsReceiveBBNSTNKSchema import TrxUnitGoodsReceiveBBNSTNKRequest, TrxUnitGoodsReceiveBBNSTNKInputSendRequest, TrxUnitGoodsReceiveBBNSTNKUpdateRequest
from src.entities.master.BrandEntity import MtrBrand
from src.utils.AddPagination import get_the_pagination, get_the_pagination_search_with_join
from datetime import datetime, date
import logging
from dataclasses import asdict
import requests

def get_unit_goods_receive_bbn_stnk_search(db: Session, page:int,limit:int,all_params:dict()):
    try:
        query_set = select(
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number,
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_document_number,
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_date,
            MtrVehicle.vehicle_chassis_number,
            TrxUnitGoodsReceiveBBNSTNK.stnk_send_date,
            TrxUnitGoodsReceiveBBNSTNK.stnk_send_document_number
        )
        join_tables = [TrxUnitPurchaseOrderBBNDetail, MtrVehicle, TrxUnitPurchaseOrderBBN]
        query_check = get_the_pagination_search_with_join(query_set,all_params,TrxUnitGoodsReceiveBBNSTNK,join_tables)
        query_final = query_check.join(
            TrxUnitPurchaseOrderBBNDetail,
            TrxUnitGoodsReceiveBBNSTNK.purchase_order_bbn_detail_system_number == TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_detail_system_number
        ).join(
            MtrVehicle,
            TrxUnitPurchaseOrderBBNDetail.vehicle_id == MtrVehicle.vehicle_id
        ).join(
            TrxUnitPurchaseOrderBBN,
            TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number == TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number
        ).order_by(TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number).offset(page*limit).limit(limit)

        data = db.execute(query_final).all()

        results = []
        for goods_receive_bbn_stnk_system_number, goods_receive_bbn_stnk_document_number, goods_receive_bbn_stnk_date, vehicle_chassis_number, stnk_send_date, stnk_send_document_number in data:
            go_out = {
                "goods_receive_bbn_stnk_system_number": goods_receive_bbn_stnk_system_number,
                "goods_receive_bbn_stnk_document_number": goods_receive_bbn_stnk_document_number,
                "goods_receive_bbn_stnk_date": goods_receive_bbn_stnk_date,
                "vehicle_chassis_number": vehicle_chassis_number,
                "stnk_send_date": stnk_send_date,
                "stnk_send_document_number": stnk_send_document_number
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
        return None, None, err

def get_unit_goods_receive_bbn_stnk_by_id(db: Session, id: int):
    try:
        query_set = select(
            TrxUnitPurchaseOrderBBN.purchase_order_bbn_document_number,
            TrxUnitPurchaseOrderBBN.purchase_order_date,
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_document_number,
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_date,
            TrxUnitPurchaseOrderBBN.supplier_id,
            TrxUnitGoodsReceiveBBNSTNK.police_invoice_number,
            MtrBrand.brand_name,
            MtrUnitModel.model_description,
            MtrUnitVariant.variant_description,
            MtrColour.colour_commercial_name,
            MtrUnitVariant.production_year,
            MtrVariantCylinder.variant_cylinder_name,
            MtrVariantFuel.variant_fuel_name,
            MtrVehicle.vehicle_chassis_number,
            MtrVehicle.vehicle_engine_number,
            TrxUnitGoodsReceiveBBNSTNK.stnk_number,
            TrxUnitGoodsReceiveBBNSTNK.stnk_expired_date,
            TrxUnitGoodsReceiveBBNSTNK.stnk_received_date,
            TrxUnitGoodsReceiveBBNSTNK.stnk_received_by,
            TrxUnitGoodsReceiveBBNSTNK.stnk_send_document_number,
            TrxUnitGoodsReceiveBBNSTNK.stnk_send_date,
            TrxUnitGoodsReceiveBBNSTNK.supplier_reference_number,
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_remark
        ).join(
            TrxUnitPurchaseOrderBBNDetail,
            TrxUnitGoodsReceiveBBNSTNK.purchase_order_bbn_detail_system_number == TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_detail_system_number
        ).join(
            MtrVehicle,
            TrxUnitPurchaseOrderBBNDetail.vehicle_id == MtrVehicle.vehicle_id
        ).join(
            TrxUnitPurchaseOrderBBN,
            TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number == TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number
        ).join(
            MtrBrand,
            MtrVehicle.vehicle_brand_id == MtrBrand.brand_id
        ).join(
            MtrUnitModel,
            MtrVehicle.vehicle_model_id == MtrUnitModel.model_id
        ).join(
            MtrUnitVariant,
            MtrVehicle.vehicle_variant_id == MtrUnitVariant.variant_id
        ).join(
            MtrColour,
            MtrVehicle.vehicle_colour_id == MtrColour.colour_id
        ).join(
            MtrVariantCylinder,
            MtrUnitVariant.cylinder_id == MtrVariantCylinder.variant_cylinder_id
        ).join(
            MtrVariantFuel,
            MtrUnitVariant.fuel_id == MtrVariantFuel.variant_fuel_id
        ).where(TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number == id)

        data = db.execute(query_set).all()

        results = []

        for purchase_order_bbn_document_number, purchase_order_date, goods_receive_bbn_stnk_document_number, goods_receive_bbn_stnk_date, supplier_id, police_invoice_number, brand_name, model_description, variant_description, colour_commercial_name, production_year, variant_cylinder_name, variant_fuel_name, vehicle_chassis_number, vehicle_engine_number, stnk_number, stnk_expired_date, stnk_received_date, stnk_received_by, stnk_send_document_number, stnk_send_date, supplier_reference_number, goods_receive_bbn_stnk_remark in data:
            go_out = {
                "purchase_order_bbn_document_number": purchase_order_bbn_document_number,
                "purchase_order_date": purchase_order_date,
                "goods_receive_bbn_stnk_document_number": goods_receive_bbn_stnk_document_number,
                "goods_receive_bbn_stnk_date": goods_receive_bbn_stnk_date,
                "supplier_id": supplier_id,
                "police_invoice_number": police_invoice_number,
                "brand_name": brand_name,
                "model_description": model_description,
                "variant_description": variant_description,
                "colour_commercial_name": colour_commercial_name,
                "production_year": production_year,
                "variant_cylinder_name": variant_cylinder_name,
                "variant_fuel_name": variant_fuel_name,
                "vehicle_chassis_number": vehicle_chassis_number,
                "vehicle_engine_number": vehicle_engine_number,
                "stnk_number": stnk_number,
                "stnk_expired_date": stnk_expired_date,
                "stnk_received_date": stnk_received_date,
                "stnk_received_by": stnk_received_by,
                "stnk_send_document_number": stnk_send_document_number,
                "stnk_send_date": stnk_send_date,
                "supplier_reference_number": supplier_reference_number,
                "goods_receive_bbn_stnk_remark": goods_receive_bbn_stnk_remark
            }
            results.append(go_out)
        
        result = results[0]

        id_supplier = result["supplier_id"]
        supplier_url = f"http://10.1.32.26:8000/general-service/api/general/supplier-master/{id_supplier}"

        try:
            supplier_response = requests.get(supplier_url)
            supplier_data = supplier_response.json()
            result["supplier_name"] = result.pop("supplier_id")
            result["supplier_name"] = supplier_data["data"]["supplier_name"]
        except Exception:
            print(Exception)

        return result, None

    except Exception as err:
        return None, err

def post_unit_goods_receive_bbn_stnk(db: Session, req: TrxUnitGoodsReceiveBBNSTNKRequest):
    try:
        db.begin()
        _new_data = TrxUnitGoodsReceiveBBNSTNK()
        _new_data.company_id = req.company_id
        _new_data.goods_receive_bbn_stnk_date = req.goods_receive_bbn_stnk_date
        _new_data.purchase_order_bbn_detail_system_number = req.purchase_order_bbn_detail_system_number
        _new_data.police_invoice_number = req.police_invoice_number
        _new_data.stnk_number = req.stnk_number
        _new_data.stnk_expired_date = req.stnk_expired_date
        _new_data.stnk_received_date = req.stnk_received_date
        _new_data.stnk_received_by = req.stnk_received_by
        _new_data.supplier_reference_number = req.supplier_reference_number
        _new_data.goods_receive_bbn_stnk_remark = req.goods_receive_bbn_stnk_remark
        db.add(_new_data)
        db.commit()
        db.refresh(_new_data)
        return _new_data, None
    except Exception as err:
        db.rollback()
        return None, err

def patch_submit_unit_goods_receive_bbn_stnk(db: Session, id: int):
    check_data = select(TrxUnitGoodsReceiveBBNSTNK).where(TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number == id)
    updated_data = db.scalars(check_data).first()

    brand_id = get_brand_id(db, id)

    try:
        if updated_data.goods_receive_bbn_stnk_document_number == "":
            updated_data.goods_receive_bbn_stnk_document_number = get_doc_no(db, brand_id)
            db.commit()
            db.refresh(updated_data)
        else:
            raise Exception
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err

def update_unit_goods_receive_bbn_stnk_input_send(db: Session, id: int, req: TrxUnitGoodsReceiveBBNSTNKInputSendRequest):
    check_data = select(TrxUnitGoodsReceiveBBNSTNK).where(TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number == id)
    updated_data = db.scalars(check_data).first()

    brand_id = get_brand_id(id)

    try:
        if not updated_data.stnk_send_document_number:
            updated_data.stnk_send_date = req.stnk_send_date
            updated_data.stnk_send_document_number = get_send_doc_no(req.stnk_send_date, brand_id)
            updated_data.stnk_receiver_name = req.stnk_receiver_name
            updated_data.stnk_receiver_id_number = req.stnk_receiver_id_number
            db.commit()
            db.refresh(updated_data)
        else:
            raise Exception
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err

def delete_unit_goods_receive_bbn_stnk(db: Session, id:int):
    try:
        query_check = select(TrxUnitGoodsReceiveBBNSTNK).where(TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number==id)
        erase_data = db.scalars(query_check).first()

        if erase_data.goods_receive_bbn_stnk_document_number == "":
            db.delete(erase_data)
            db.commit()
        else:
            raise Exception
        return erase_data, None
    except Exception as err:
        db.rollback()
        return None, err

def update_unit_goods_receive_bbn_stnk(db: Session, id: int, req: TrxUnitGoodsReceiveBBNSTNKUpdateRequest):
    check_data = select(TrxUnitGoodsReceiveBBNSTNK).where(TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number == id)
    updated_data = db.scalars(check_data).first()
    try:
        if updated_data.goods_receive_bbn_stnk_document_number == "":
            updated_data.goods_receive_bbn_stnk_date = req.goods_receive_bbn_stnk_date
            updated_data.police_invoice_number = req.police_invoice_number
            updated_data.stnk_expired_date = req.stnk_expired_date
            updated_data.stnk_received_date = req.stnk_received_date
            updated_data.stnk_received_by = req.stnk_received_by
            updated_data.supplier_reference_number = req.supplier_reference_number
            updated_data.goods_receive_bbn_stnk_remark = req.goods_receive_bbn_stnk_remark
            db.commit()
            db.refresh(updated_data)
        else:
            raise Exception
        return updated_data, None
    except Exception as err:
        db.rollback()
        return None, err

# Yang dibawah ini tidk dipanggil service, dipakai di file ini saja

def get_brand_id(db: Session, id: int):
    check_brand = select(
        TrxUnitPurchaseOrderBBN.brand_id
    ).join(
        TrxUnitPurchaseOrderBBNDetail,
        TrxUnitPurchaseOrderBBN.purchase_order_bbn_system_number == TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_system_number
    ).join(
        TrxUnitGoodsReceiveBBNSTNK,
        TrxUnitPurchaseOrderBBNDetail.purchase_order_bbn_detail_system_number == TrxUnitGoodsReceiveBBNSTNK.purchase_order_bbn_detail_system_number
    ).where(TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_system_number == id)
    brand_data = db.execute(check_brand).first()
    brand_id = brand_data[0]

    return brand_id

def get_doc_no(db:Session, id: int):
    receive_code = "SABR"
    current_date = datetime.now()
    period_month = current_date.month
    period_year = current_date.year - 2000
    try:
        spec_code_query = select(MtrBrand.brand_name).where(MtrBrand.brand_id == id)
        spec_result = db.execute(spec_code_query).scalar()
        spec_generate = spec_result[0].upper()
        document_number_query = select(
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_document_number
        ).where(
            TrxUnitGoodsReceiveBBNSTNK.goods_receive_bbn_stnk_document_number.like(f"%{period_month}/{period_year}%")
        )
        final_query = db.execute(document_number_query).all()
        document_number = len(final_query)
        if  document_number < 1:
            document_number += 1
            doc_format = f"{receive_code}/{spec_generate}/{period_month:02}/{period_year}/{document_number:05}"
        else :
            document_number += 1
            doc_format = f"{receive_code}/{spec_generate}/{period_month:02}/{period_year}/{document_number:05}"

        return doc_format
    except Exception as err:
        return None, err

def get_send_doc_no(db:Session, send_date: datetime, id: int):
    send_code = "SASS"
    send_month = send_date.month
    send_year = send_date.year - 2000
    try:
        spec_code_query = select(MtrBrand.brand_name).where(MtrBrand.brand_id == id)
        spec_result = db.execute(spec_code_query).scalar()
        spec_generate = spec_result[0].upper()
        send_document_number_query = select(
            TrxUnitGoodsReceiveBBNSTNK.stnk_send_document_number
        ).where(
            TrxUnitGoodsReceiveBBNSTNK.stnk_send_document_number.like(f"%{send_month}{send_year}%")
        )
        final_query = db.execute(send_document_number_query).all()
        send_document_number = len(final_query)
        if  send_document_number < 1:
            send_document_number += 1
            send_doc_format = f"{send_code}/{spec_generate}/{send_month:02}{send_year}/{send_document_number:05}"
        else :
            send_document_number += 1
            send_doc_format = f"{send_code}/{spec_generate}/{send_month:02}{send_year}/{send_document_number:05}"

        return send_doc_format
    except Exception as err:
        return None, err