from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MtrCustomerSchema(BaseModel):
    company_id: int
    customer_type_id: Optional[int] = None
    id_type: Optional[int] = None
    id_number: Optional[str] = None
    customer_title_prefix: Optional[str] = None
    customer_name: str
    customer_title_suffix: Optional[str] = None
    keyword: Optional[str] = None
    id_address_id: Optional[int] = None
    customer_email_address: Optional[str] = None
    id_phone_no: Optional[str] = None
    customer_mobile_phone: Optional[str] = None
    customer_mobile_phone2: Optional[str] = None
    driver_mobile_phone: Optional[str] = None 
    term_of_payment_id: Optional[int] = None
    tax_invoice_type_id: Optional[int] = None
    home_address_id: Optional[int] = None
    home_phone_no: Optional[str] = None
    home_fax_no: Optional[str] = None
    office_address_id: Optional[int] = None
    office_phone_no: Optional[str] = None
    office_fax_no: Optional[str] = None
    reference_name: Optional[str] = None
    reference_address_id: Optional[int] = None
    reference_phone_number: Optional[str] = None
    vat_registration_number: Optional[str] = None
    vat_registration_date: Optional[datetime] = None
    vat_pkp_type: Optional[str] = None
    vat_pkp_number: Optional[str] = None
    vat_pkp_date: Optional[datetime] = None
    vat_transaction_id: Optional[int] = None
    vat_name: Optional[str] = None
    vat_address_id: Optional[int] = None
    vat_tax_office_id: Optional[int] = None
    tax_registration_number: Optional[str] = None
    tax_registration_date: Optional[datetime] = None
    pkp_type: Optional[str] = None
    pkp_number: Optional[str] = None
    pkp_date: Optional[datetime] = None
    tax_name: Optional[str] = None
    tax_address_id: Optional[int] = None
    tax_office_id: Optional[int] = None
    business_type_id: Optional[int] = None
    business_group_id: Optional[int] = None
    business_website: Optional[str] = None
    customer_class_id:Optional[int] = None
    customer_behavior_id: Optional[int] = None
    customer_gender_id: Optional[int] = None
    customer_birthday: Optional[datetime] = None
    customer_birth_place: Optional[str] = None
    customer_religion_id: Optional[int] = None
    customer_marital_status_id: Optional[int] = None
    customer_marriage_date: Optional[datetime] = None
    customer_job_title_id: Optional[int] = None
    customer_hobby: Optional[str] = None
    reference_note: Optional[str] = None
    correspondence_equal_to: Optional[str] = None
    bill_equal_to: Optional[str] = None
    print_state: Optional[bool] = None
    dealer_name_id: Optional[int] = None
    collector_id: Optional[int] = None
    dealer_sales_representative: Optional[int] = None
    dealer_contact_date: Optional[datetime] = None
    customer_price_code:Optional[int] = None
    

class MtrGetCustomerSchema(BaseModel):
    company_id: int
    dealer_sales_representative: Optional[int] = None
    customer_code: str
    customer_title_prefix: Optional[str] = None
    customer_name: str
    customer_title_suffix: Optional[str] = None
    customer_type_id: Optional[int] = None
    keyword: Optional[str] = None
    customer_gender_id: Optional[int] = None
    customer_birthday: Optional[datetime] = None
    customer_birth_place: Optional[str] = None
    customer_religion_id: Optional[int] = None
    customer_marital_status_id: Optional[int] = None
    customer_marriage_date: Optional[datetime] = None
    customer_hobby: Optional[str] = None
    customer_mobile_phone: Optional[str] = None
    customer_mobile_phone2: Optional[str] = None
    driver_mobile_phone: Optional[str] = None 
    customer_email_address: Optional[str] = None
    customer_job_title_id: Optional[int] = None
    id_type: Optional[int] = None
    id_number: Optional[str] = None
    id_address_id: Optional[int] = None
    id_phone_no: Optional[str] = None
    id_fax_no: Optional[str] = None
    home_address_id: Optional[int] = None
    home_phone_no: Optional[str] = None
    home_fax_no: Optional[str] = None
    office_address_id: Optional[int] = None
    office_phone_no: Optional[str] = None
    office_fax_no: Optional[str] = None
    reference_name: Optional[str] = None
    reference_address_id: Optional[int] = None
    reference_phone_number: Optional[str] = None
    reference_note: Optional[str] = None
    tax_invoice_type_id: Optional[int] = None
    tax_registration_number: Optional[str] = None
    tax_registration_date: Optional[datetime] = None
    tax_name: Optional[str] = None
    tax_address_id: Optional[int] = None
    pkp_number: Optional[str] = None
    pkp_type: Optional[str] = None
    vat_registration_number: Optional[str] = None
    vat_registration_date: Optional[datetime] = None
    vat_name: Optional[str] = None
    vat_address_id: Optional[int] = None
    vat_pkp_type: Optional[str] = None
    vat_pkp_date: Optional[datetime] = None
    vat_pkp_number: Optional[str] = None
    vat_tax_office_id: Optional[int] = None
    bill_equal_to: Optional[str] = None
    correspondence_equal_to: Optional[str] = None
    business_type_id: Optional[int] = None
    business_group_id: Optional[int] = None
    business_website: Optional[str] = None
    dealer_name_id: Optional[int] = None
    dealer_contact_date: Optional[datetime] = None
    customer_class_id:Optional[int] = None
    customer_behavior_id: Optional[int] = None
    print_state: Optional[bool] = None
    collector_id: Optional[int] = None
    term_of_payment_id: Optional[int] = None
    tax_office_id: Optional[int] = None
    vat_transaction_id: Optional[int] = None
    customer_price_code:Optional[int] = None
    customer_delivery_address:list
    customer_contact:list
    customer_bank_account:list
    customer_by_dealer:list

    class Config:
        orm_mode = True
