from fastapi import APIRouter, HTTPException, status, Query, Depends
from typing import List
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.services.master import CustomerService
from src.payloads.schemas.master.CustomerSchema import MtrCustomerSchema, MtrGetCustomerSchema
from src.payloads.schemas.master.CustomerBankAccountSchema import MtrCustomerBankAccountSchema, MtrCustomerBankAccountUpdateSchema
from src.payloads.schemas.master.CustomerByDealerSchema import MtrCustomerByDealerSchema
from src.payloads.schemas.master.CustomerContactSchema import MtrCustomerContactSchema
from src.payloads.schemas.master.CustomerDeliveryAddressSchema import MtrCustomerDeliveryAddressSchema
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException

router = APIRouter(tags=["Customer Master"],prefix="/api/general")


@router.get("/get-all-customers", status_code=200)
async def get_all_customer(page:int, limit:int, db: Session = Depends(get_db),
                           customer_code:str|None=None, 
                           customer_name:str|None=None,
                           customer_type_description:str|None=None,
                           address_street_1:str|None=None,
                           address_street_2:str|None=None,
                           address_street_3:str|None=None,
                           id_phone_no:str|None=None,
                           is_active:bool|None=None,
                           sort_by:str|None=None,
                           sort_of:str|None=None):
    get_all_params  = {
        "customer_code":customer_code,
        "customer_name":customer_name,
        "customer_type_description":customer_type_description,
        "address_street_1": address_street_1,
        "address_street_2": address_street_2,
        "address_street_3": address_street_3,
        "id_phone_no":id_phone_no,
        "is_active":is_active
    }
    sort_fields = {
        "sort_by":sort_by,
        "sort_of": sort_of
    }
    get_results, pages, err = CustomerService.get_all_customer(db, page,limit,get_all_params,sort_fields)
    if err == None or get_results!=[]:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_results)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.get("/get-customer/{customer_id}",status_code=200)
async def get_by_id_customer(customer_id:int, db:Session=Depends(get_db)):
    get_result, get_result2, get_result3, get_result4, get_result5, err = CustomerService.get_by_id_customer(customer_id, db)
    if not get_result or err != None:
        print(str(err))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    else:
        return payload_response(200,"Success",MtrGetCustomerSchema(
            company_id = get_result.company_id,
            dealer_sales_representative = get_result.dealer_sales_representative,
            customer_code = get_result.customer_code,
            customer_title_prefix = get_result.customer_title_prefix,
            customer_name = get_result.customer_name,
            customer_title_suffix = get_result.customer_title_suffix, 
            customer_type_id = get_result.customer_type_id,
            keyword = get_result.keyword,
            customer_gender_id = get_result.customer_gender_id,
            customer_birthday = get_result.customer_birthday,
            customer_birth_place = get_result.customer_birth_place,
            customer_religion_id = get_result.customer_religion_id,
            customer_marital_status_id = get_result.customer_marital_status_id,
            customer_marriage_date = get_result.customer_marriage_date,
            customer_hobby = get_result.customer_hobby,
            customer_mobile_phone = get_result.customer_mobile_phone,
            customer_mobile_phone2 = get_result.customer_mobile_phone2,
            driver_mobile_phone = get_result.driver_mobile_phone,
            customer_email_address = get_result.customer_email_address,
            customer_job_title_id = get_result.customer_job_title_id,
            id_type = get_result.id_type,
            id_number = get_result.id_number,
            id_address_id = get_result.id_address_id,
            id_phone_no = get_result.id_phone_no,
            home_address_id = get_result.home_address_id,
            home_phone_no = get_result.home_phone_no,
            home_fax_no = get_result.home_fax_no,
            office_address_id = get_result.office_address_id,
            office_phone_no = get_result.office_phone_no,
            office_fax_no = get_result.office_fax_no,
            reference_name = get_result.reference_name,
            reference_address_id = get_result.reference_address_id,
            reference_phone_number = get_result.reference_phone_number,
            reference_note = get_result.reference_note,
            tax_invoice_type_id = get_result.tax_invoice_type_id,
            tax_registration_number = get_result.tax_registration_number,
            tax_registration_date = get_result.tax_registration_date,
            tax_name = get_result.tax_name,
            tax_address_id = get_result.tax_address_id,
            pkp_number = get_result.pkp_number,
            pkp_type = get_result.pkp_type,
            pkp_date = get_result.pkp_date,
            vat_registration_number = get_result. vat_registration_number,
            vat_registration_date = get_result.vat_registration_date,
            vat_name = get_result.vat_name,
            vat_address_id = get_result.vat_address_id,
            vat_pkp_type = get_result.vat_pkp_type,
            vat_pkp_date = get_result.vat_pkp_date,
            vat_pkp_number = get_result.vat_pkp_number,
            vat_tax_service_office_id = get_result.vat_tax_office_id,
            bill_equal_to = get_result.bill_equal_to,
            correspondence_equal_to = get_result.correspondence_equal_to,
            business_type_id = get_result.business_type_id,
            business_group_id = get_result.business_group_id,
            business_website = get_result.business_website,
            dealer_name_id = get_result.dealer_name_id,
            dealer_contact_date = get_result.dealer_contact_date,
            customer_class_id = get_result.customer_class_id,
            customer_behavior_id = get_result.customer_behavior_id,
            print_state = get_result.print_state,
            collector_id = get_result.collector_id,
            term_of_payment_id = get_result.term_of_payment_id,
            tax_service_office_id = get_result.tax_office_id,
            vat_transaction_id = get_result.vat_transaction_id,
            customer_price_code = get_result.customer_price_code,
            customer_delivery_address = get_result2,
            customer_contact = get_result3,
            customer_bank_account = get_result4,
            customer_by_dealer = get_result5
        ))

@router.get("/get-customer-delivery-address/{customer_delivery_address_id}", status_code=200)
async def get_customer_delivery_address(id:int, db:Session=Depends(get_db)):
    data, err = CustomerService.get_customer_delivery_address_by_id(id,db)
    if err == None and data != None:
        return payload_response(200, "Success", data)
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=ResponseException(404))

@router.get("/get-customer-contact/{customer_contact_id}", status_code=200)
async def get_customer_contact_by_id(id:int, db:Session=Depends(get_db)):
    data, err = CustomerService.get_customer_contact_by_id(id,db)
    if err == None and data != None:
        return payload_response(200, "Success", data)
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=ResponseException(404))

@router.get("/get-customer-bank-account/{customer_bank_account_id}", status_code=200)
async def get_customer_bank_account_by_id(id:int, db:Session=Depends(get_db)):
    data, err = CustomerService.get_customer_bank_account_by_id(id,db)
    if err == None and data != None:
        return payload_response(200, "Success", data)
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=ResponseException(404))

@router.get("/get-customer-by-dealer/{customer_dealer_id}", status_code=200)
async def get_customer_by_dealer_by_id(id:int, db:Session=Depends(get_db)):
    data, err = CustomerService.get_customer_by_dealer_by_id(id,db)
    if err == None and data != None:
        return payload_response(200, "Success", data)
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=ResponseException(404))

@router.post("/post-customer",status_code=status.HTTP_201_CREATED)
async def post_customer(customer_master:MtrCustomerSchema, db:Session=Depends(get_db)):
    created_data, err = CustomerService.post_customer(customer_master,db)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.post("/post-customer-delivery-address/{customer_id}",status_code=status.HTTP_201_CREATED)
async def post_customer_delivery_address(customer_delivery_address:MtrCustomerDeliveryAddressSchema, customer_id:int, db:Session=Depends(get_db)):
    created_data, err = CustomerService.post_customer_delivery_address(customer_delivery_address,customer_id,db)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.post("/post-customer-contact/{customer_id}",status_code=status.HTTP_201_CREATED)
async def post_customer_contact(customer_contact:MtrCustomerContactSchema, customer_id:int, db:Session=Depends(get_db)):
    created_data, err = CustomerService.post_customer_contact(customer_contact, customer_id,db)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.post("/post-customer-bank-account{customer_id}",status_code=status.HTTP_201_CREATED)
async def post_customer_bank_account(customer_bank_account:MtrCustomerBankAccountSchema, customer_id:int, db:Session=Depends(get_db)):
    created_data, err = CustomerService.post_customer_bank_account(customer_bank_account, customer_id,db)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.post("/post-customer-by-dealer/{customer_id}",status_code=status.HTTP_201_CREATED)
async def post_customer_by_dealer(customer_by_dealer:MtrCustomerByDealerSchema, customer_id:int, db:Session=Depends(get_db)):
    created_data, err = CustomerService.post_customer_by_dealer(customer_by_dealer, customer_id,db)
    if err == None:
        return payload_response(201,"Created",created_data)
    else:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.put("/put-customer/{customer_id}",status_code=201)
async def put_customer(customer_id:int,req:MtrCustomerSchema, db:Session=Depends(get_db)):
    updated_data, err = CustomerService.put_customer(customer_id,req,db)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.put("/put-customer-delivery-address/{id}",status_code=200)
async def put_customer_delivery_address(id:int, req:MtrCustomerDeliveryAddressSchema, db:Session=Depends(get_db)):
    result, err = CustomerService.put_customer_delivery_address(id,req,db)
    if err == None:
        return payload_response(ResponseException(200), "Success", result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(409))

@router.put("/put-customer-contact/{id}",status_code=200)
async def put_customer_contact(id:int, req:MtrCustomerContactSchema, db:Session=Depends(get_db)):
    result, err = CustomerService.put_customer_contact(id,req,db)
    if err == None:
        return payload_response(ResponseException(200), "Success", result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(409))

@router.put("/put-customer-bank-account/{id}",status_code=200)
async def put_customer_bank_account(id:int, req:MtrCustomerBankAccountUpdateSchema, db:Session=Depends(get_db)):
    result, err = CustomerService.put_customer_bank_account(id,req,db)
    if err == None:
        return payload_response(ResponseException(200), "Success", result)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(409))

@router.patch("/patch-customer/{customer_id}",status_code=201)
async def patch_customer(customer_id:int, db:Session=Depends(get_db)):
    updated_data, err = CustomerService.patch_customer(customer_id,db)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.patch("/patch-customer-delivery-address/{customer_delivery_id}",status_code=201)
async def patch_customer_delivery_address(customer_delivery_id:int, db:Session=Depends(get_db)):
    updated_data, err = CustomerService.patch_customer_delivery_address(customer_delivery_id,db)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.patch("/patch-customer-contact/{customer_contact_id}",status_code=201)
async def patch_customer_contact(customer_contact_id:int, db:Session=Depends(get_db)):
    updated_data, err = CustomerService.patch_customer_contact(customer_contact_id,db)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))

@router.patch("/patch-customer-bank-account/{customer_bank_account_id}",status_code=201)
async def patch_customer_bank_account(customer_bank_account_id:int, db:Session=Depends(get_db)):
    updated_data, err = CustomerService.patch_customer_bank_account(customer_bank_account_id,db)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.patch("/patch-customer-by-dealer/{customer_by_dealer_id}",status_code=201)
async def patch_customer_by_dealer(customer_by_dealer_id:int, db:Session=Depends(get_db)):
    updated_data, err = CustomerService.patch_customer_by_dealer(customer_by_dealer_id,db)
    if err == None:
        return payload_response(201,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    
@router.get("/get-multiple-customers",status_code=200)
async def get_multiple_customer(id:List[int] = Query(...), db:Session=Depends(get_db)):
    data, err = CustomerService.get_multiple_customer(id,db)
    if err == None and data != []:
        return {"status": "Success", "data": data}
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=ResponseException(404))