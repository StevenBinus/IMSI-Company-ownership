from fastapi import APIRouter, HTTPException, status, Query, Request
from src.services.master import SupplierReferenceService
from src.payloads.responses.GeneralResponse import payload_response
from src.payloads.responses.PaginationResponse import pagination_response
from src.exceptions.RequestException import ResponseException
from src.payloads.schemas.master.SupplierReferenceSchema import MtrSupplierReferenceSchema,MtrSupplierReferenceSchemaGetAll
from src.payloads.schemas.master.SupplierReferenceBankReferenceSchema import MtrSupplierReferenceBankReference
from src.payloads.schemas.master.SupplierReferencePicSchema import MtrSupplierReferencePic


router = APIRouter(tags=["Supplier Reference"],prefix="/api/general")

@router.get("/supplier_references",status_code=200)
def get_supplier_references(page:int,limit:int,
                            supplier_status:str|None=None,
                            supplier_code:str|None=None,
                            supplier_name:str|None=None,
                            supplier_type:str|None=None,
                            sort_of:str|None=None,
                            sort_by:str|None=None):
    get_all_params={"supplier_status":supplier_status,
                    "supplier_code":supplier_code,
                    "supplier_name":supplier_name,
                    "supplier_type":supplier_type}
    sort_params={"sort_by":sort_by,"sort_of":sort_of}
    get_all_supplier_reference,pages,err=SupplierReferenceService.get_all_supplier_references(page,limit,get_all_params,sort_params)
    if get_all_supplier_reference!=[] and err == None:
        return pagination_response(200,"Success",page,limit,pages["total_pages"],pages["total_rows"],get_all_supplier_reference)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))

@router.post("/supplier_reference",status_code=202)
def post_supplier_reference(req:MtrSupplierReferenceSchema):
    created_data,err = SupplierReferenceService.post_supplier_reference(req)
    if err == None:
        return payload_response(200,"Success",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail = str(err))

@router.get("/supplier_reference/{supplier_reference_id}",status_code=200)
def get_supplier_reference(supplier_reference_id:int):
    supplier_reference,pic_reference,bank_reference,err = SupplierReferenceService.get_supplier_reference_by_id(supplier_reference_id)
    if err != None or supplier_reference_id==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = ResponseException(404))
    else:
         return payload_response(200,"Success",MtrSupplierReferenceSchemaGetAll(
            supplier_status=supplier_reference.supplier_status,
            supplier_reference_id = supplier_reference.supplier_reference_id,
            supplier_code=supplier_reference.supplier_code,
            supplier_name=supplier_reference.supplier_name,
            supplier_type_id=supplier_reference.supplier_type_id,
            supplier_class = supplier_reference.supplier_class,
            supplier_title_prefix=supplier_reference.supplier_title_prefix,
            supplier_title_suffix=supplier_reference.supplier_title_suffix,
            supplier_address_id=supplier_reference.supplier_address_id,
            supplier_phone_number = supplier_reference.supplier_phone_number,
            supplier_fax_number=supplier_reference.supplier_fax_number,
            supplier_mobile_phone=supplier_reference.supplier_mobile_phone,
            supplier_email_address=supplier_reference.supplier_email_address,
            supplier_behaviour_id=supplier_reference.supplier_behaviour_id,
            term_of_payment_id=supplier_reference.term_of_payment_id,
            minimum_down_payment=supplier_reference.minimum_down_payment,
            via_binning=supplier_reference.via_binning,
            old_supplier_code=supplier_reference.old_supplier_code,
            business_group_id=supplier_reference.business_group_id,
            supplier_unique_code=supplier_reference.supplier_unique_code,
            company_id=supplier_reference.company_id,
            vat_npwp_no=supplier_reference.vat_npwp_no,
            vat_npwp_date = str(supplier_reference.vat_npwp_date),
            vat_name = supplier_reference.vat_name,
            vat_address_id = supplier_reference.vat_address_id,
            vat_pkp_type = supplier_reference.vat_pkp_type,
            vat_pkp_no = supplier_reference.vat_pkp_no,
            vat_tax_service_office_id = supplier_reference.vat_tax_service_office_id,
            vat_transaction_id=supplier_reference.vat_transaction_id,
            tax_npwp_no=supplier_reference.tax_npwp_no,
            tax_name = supplier_reference.tax_name,
            tax_address_id=supplier_reference.tax_address_id,
            tax_pkp_no = supplier_reference.tax_pkp_no,
            tax_pkp_date = str(supplier_reference.tax_pkp_date),
            tax_pkp_type = supplier_reference.tax_pkp_type,
            tax_tax_service_office_id = supplier_reference.tax_tax_service_office_id,
            vat_pkp_date = str(supplier_reference.vat_pkp_date),
            tax_npwp_date = str(supplier_reference.tax_npwp_date),
            supplier_referencce_pic = pic_reference,
            supplier_reference_bank_reference = bank_reference
       ))

@router.patch("/supplier_reference/{supplier_reference_id}",status_code=202)
async def patch_supplier_reference(supplier_reference_id:int):
    updated_data,err=SupplierReferenceService.patch_supplier_references(supplier_reference_id)
    if err == None:
        return payload_response(202,"Updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))

@router.post("/supplier_reference_bank_reference",status_code=201)
async def post_supplier_reference_bank_reference(req:MtrSupplierReferenceBankReference):
    created_data,err = SupplierReferenceService.post_supplier_reference_bank_reference(req)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))
    
@router.patch("/supplier_reference_bank_reference/{supplier_reference_bank_id}",status_code=202)
async def patch_supplier_reference_bank_reference(supplier_reference_bank_id:int):
    updated_data,err = SupplierReferenceService.patch_supplier_reference_bank_reference(supplier_reference_bank_id)
    if err == None:
        return payload_response(202,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    

@router.post("/supplier_reference_pic",status_code=201)
async def post_supplier_reference_pic(req:MtrSupplierReferencePic):
    created_data,err = SupplierReferenceService.post_supplier_reference_pic(req)
    if err == None:
        return payload_response(201,"created",created_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))
    
@router.patch("/supplier_reference_pic/{supplier_reference_pic_id}",status_code=202)
async def put_supplier_reference_pic(supplier_reference_pic_id:int):
    updated_data,err = SupplierReferenceService.patch_supplier_reference_pic(supplier_reference_pic_id)
    if err == None:
        return payload_response(202,"updated",updated_data)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(err))
