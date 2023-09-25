from datetime import datetime
from pydantic import BaseModel
from typing import Optional
    
class TrxProspectVehicleDetailRequest(BaseModel):
    prospect_system_number:int
    prospect_brand_id:int
    prospect_model_id:int
    prospect_variant_id:int
    accessories_option_id:int
    prospect_colour_id:int
    prospect_quantity:int
    expected_delivery_date:datetime
    
class TrxProspectFolloWUpRequest(BaseModel):
    prospect_system_number:int
    prospect_follow_up_date:datetime
    follow_up_id:int
    prospect_follow_up_note:str
    result_date:datetime    
    result_note:str
    
class TrxProspectRequest(BaseModel):
    prospect_date: datetime
    prospect_customer_system_number:int = None  # field SPM No default FK's null
    vehicle_sales_order_system_number:int = None # field SPM No default FK's null
    prospect_stage_id:int = None  # field SPM No default FK's null
    customer_id:Optional[int] = None # get from mtr_customer from general-common service
    # insert to trx_prospect_customer produce prospect_customer id
    title_prefix:Optional[str] = None
    prospect_name:str
    title_suffix:Optional[str] = None
    prospect_gender:Optional[int] = None # get from general-common service 
    prospect_type:Optional[int] = None # get from general-common service
    prospect_source:int # get from general-common service
    search_keyword:Optional[str] = None
    customer_address_line1:Optional[str] = None
    customer_address_line2:Optional[str] = None
    customer_address_line3:Optional[str] = None
    customer_area:Optional[int] = None #get from address from general-common service
    customer_phone_no:Optional[str] = None 
    customer_fax_no:Optional[str] = None
    customer_mobile_phone:Optional[str] = None
    customer_mobile_emailaddr:Optional[str] = None
    contact_person_name:Optional[str] = None
    contact_person_gender:Optional[int] = None # get from general-common service
    contact_person_job_title:Optional[int] = None # get from general-common service
    contact_person_mobile_phone:Optional[str] = None 
    contact_person_email_addr:Optional[str] = None
    customer_group_business_category:Optional[int] = None # get from general-common service
    customer_group_sub_category:Optional[int] = None  # get from general-common service
    customer_group_website:Optional[str] = None
    # end of trx_prospect_customer
    buying_plan_date:Optional[datetime] = None
    conduct_test_drive:Optional[bool] = None
    test_drive_date_schedule:Optional[datetime] = None
    test_drive_date_actual:Optional[datetime] = None
    competitor_model:Optional[str] = None
    fund_type_id:Optional[int] = None  # get from general-common service
    retail_price_unit:Optional[float] = None
    request_discount:Optional[float] = None
    down_payment_budget:Optional[float] = None
    change_sales_rep_to:Optional[int] = None  # get from general-common service
    prospect_reference:Optional[str] = None
    prospect_note:Optional[str] = None
    prospect_drop_date:Optional[datetime] = None
    prospect_drop_reason_id:Optional[int] = None  # get from general-common service
    prospect_drop_remark:Optional[str] = None

class MtrProspectCustomerSchema(BaseModel):
    company_id:int
    prospect_customer_system_number:int
    prospect_code:str
    customer_type_id:int
    prospect_customer_title_prefix:str
    prospect_customer_name:str
    prospect_customer_title_suffix:str
    business_type_id:int
    business_group_id:int
    sales_representative_id:int
    prospect_address_id:int
    prospect_customer_mobile_phone:str
    prospect_customer_email_address:str
    prospect_customer_website:str
    prospect_customer_phone_number:str
    prospect_customer_fax_number:str
    gender_id:int
    contact_person:str
    job_title_id:int
    contact_mobile_phone:str
    contact_email_address:str
    keyword:str
    
    class Config:
        orm_mode = True

class TrxProspectHeaderwithDetail(BaseModel):
    prospect_date: datetime
    prospect_customer_system_number:int=None
    vehicle_sales_order_system_number:int=None
    prospect_stage_id:int=None
    customer_id:int
    buying_plan_date:datetime
    conduct_test_drive:bool
    test_drive_date_schedule:datetime
    test_drive_date_actual:datetime
    competitor_model:str
    fund_type_id:int
    retail_price_unit:float
    request_discount:float
    down_payment_budget:float
    change_sales_rep_to:int
    prospect_reference:str
    prospect_note:str
    prospect_drop_date:datetime
    prospect_drop_reason_id:int
    prospect_drop_remark:str
    prospectdetail:MtrProspectCustomerSchema