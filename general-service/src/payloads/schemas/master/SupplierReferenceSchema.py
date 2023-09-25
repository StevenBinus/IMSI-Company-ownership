from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class MtrSupplierReferenceSchema(BaseModel):
    supplier_name:str
    supplier_type_id:int
    supplier_class:str
    supplier_title_prefix :Optional[str]
    supplier_title_suffix:Optional[str]
    supplier_address_id:int
    supplier_phone_number:str
    supplier_fax_number:str
    supplier_mobile_phone:str
    supplier_email_address:str
    supplier_behaviour_id:int
    term_of_payment_id:int
    minimum_down_payment:float
    via_binning:bool
    old_supplier_code:Optional[str]
    business_group_id:int
    supplier_unique_code:str
    company_id:int
    vat_npwp_no:str
    vat_npwp_date:datetime
    vat_name :str
    vat_address_id:int
    vat_pkp_type :str
    vat_pkp_no:str
    vat_tax_service_office_id:int
    vat_transaction_id:int
    tax_npwp_no:str
    tax_name :str
    tax_address_id:int
    tax_pkp_no:str
    tax_pkp_date:datetime
    tax_pkp_type:bool
    tax_tax_service_office_id:int
    vat_pkp_date:datetime
    tax_npwp_date:datetime

class MtrSupplierReferenceSchemaGetAll(BaseModel):
    supplier_status :str
    supplier_code :Optional[str]
    supplier_name:str
    supplier_type_id:int
    supplier_class:str
    supplier_title_prefix :Optional[str]
    supplier_title_suffix:Optional[str]
    supplier_address_id:int
    supplier_phone_number:str
    supplier_fax_number:str
    supplier_mobile_phone:str
    supplier_email_address:str
    supplier_behaviour_id:int
    term_of_payment_id:int
    minimum_down_payment:float
    via_binning:bool
    old_supplier_code:Optional[str]
    business_group_id:int
    supplier_unique_code:str
    company_id:int
    vat_npwp_no:str
    vat_npwp_date:datetime
    vat_name :str
    vat_address_id:int
    vat_pkp_type :str
    vat_pkp_no:str
    vat_tax_service_office_id:int
    vat_transaction_id:int
    tax_npwp_no:str
    tax_name :str
    tax_address_id:int
    tax_pkp_no:str
    tax_pkp_date:datetime
    tax_pkp_type:bool
    tax_tax_service_office_id:int
    vat_pkp_date:datetime
    tax_npwp_date:datetime
    supplier_referencce_pic:list
    supplier_reference_bank_reference:list
