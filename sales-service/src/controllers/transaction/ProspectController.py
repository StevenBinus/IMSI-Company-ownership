from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.transaction import ProspectService
from src.payloads.schemas.transaction import ProspectSchema
from src.payloads.responses.CommonResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from datetime import datetime

router = APIRouter(tags=["Transaction : Prospect"],prefix="/api/sales")

@router.get("/prospect",status_code=status.HTTP_200_OK)
async def get_all_prospects(page:int, 
                            limit:int,
                            sales_repsentative_to:str|None=None,
                            prospect_date_from:datetime|None=None,
                            prospect_date_to:datetime|None=None,
                            prospect_name:str|None=None,
                            brand:int|None=None,
                            model:int|None=None,
                            variant:int|None=None,
                            prospect_status:str|None=None,
                            prospect_stage:str|None=None,
                            keyword:str|None=None,
                            db:Session=Depends(get_db)):
    
    all_params = {
        "sales_repsentative_to":sales_repsentative_to,
        "prospect_date_from":prospect_date_from,
        "prospect_date_to":prospect_date_to,
        "prospect_customer_name":prospect_name,
        "brand_id":brand,
        "model_id":model,
        "variant_id":variant,
        "prospect_status_description":prospect_status,
        "prospect_stage":prospect_stage,
        "keyword":keyword
    }

    results,pages,err = await ProspectService.get_all_prospects(db,page,limit,all_params)
    if results == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],results)

@router.get("/prospect/{id}",status_code=status.HTTP_200_OK)
async def get_prospect_by_id(id:int, db:Session=Depends(get_db)):
    header_result, detail_result, err = await ProspectService.get_prospect_by_id(db,id)
    if header_result == [] or detail_result == [] or err != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return payload_response(200,"Success", ProspectSchema.TrxProspectHeaderwithDetail(
        prospect_date = header_result.prospect_date,
        prospect_customer_system_number = header_result.prospect_customer_system_number,
        prospect_stage_id = header_result.prospect_stage_id,
        customer_id = header_result.customer_id,
        buying_plan_date = header_result.buying_plan_date,
        conduct_test_drive = header_result.conduct_test_drive,
        test_drive_date_schedule = header_result.test_drive_date_schedule,
        test_drive_date_actual = header_result.test_drive_date_actual,
        competitor_model = header_result.competitor_model,
        fund_type_id = header_result.fund_type_id,
        retail_price_unit = header_result.retail_price_unit,
        request_discount = header_result.request_discount,
        down_payment_budget = header_result.down_payment_budget,
        change_sales_rep_to = header_result.sales_repsentative_to,
        prospect_reference = header_result.prospect_reference,
        prospect_note = header_result.prospect_note,
        prospect_drop_date = header_result.prospect_drop_date,
        prospect_drop_reason_id = header_result.prospect_drop_reason_id,
        prospect_drop_remark = header_result.prospect_drop_remark,
        prospectdetail=detail_result
    ) )

@router.post("/prospect")
async def post_prospect(req:ProspectSchema.TrxProspectRequest,db:Session=Depends(get_db)):
    created_data, err = await ProspectService.post_prospect(db,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(err))
    return payload_response(201,"Created",created_data)

@router.post("/prospect-vehicle-detail",status_code=status.HTTP_201_CREATED)
async def post_prospect_vehicle_detail(req:ProspectSchema.TrxProspectVehicleDetailRequest,db:Session=Depends(get_db)):
    created_data, err = await ProspectService.post_prospect_vehicle_detail(db,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return payload_response(201,"Created",created_data)

@router.post("/prospect-followup",status_code=status.HTTP_201_CREATED)
async def post_prospect_follow_up(req:ProspectSchema.TrxProspectFolloWUpRequest,db:Session=Depends(get_db)):
    created_data,err = await ProspectService.post_prospect_follow_up(db,req)
    if err != None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=ResponseException(400))
    return payload_response(201,"Created",created_data)