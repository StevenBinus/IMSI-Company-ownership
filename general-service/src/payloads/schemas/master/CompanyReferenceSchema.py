from typing import List, Optional
from pydantic import BaseModel

class MtrCompanyreferenceGet(BaseModel):
    company_id:int
    # Currency_id, mtr_currency FK ke finance-service
    currency_id:str
    margin_outer_kpp:int
    adjustment_reason_id:str
    lead_time_unit_etd:int
    # bank_acc_receive_company_id FK dari mtr_bank_company di finance-service
    bank_acc_receive_company_id:int
    vat_code:int
    # kedua warehouse id dari mtr_warehouse di aftersales-service
    item_broken_warehouse_id:int
    unit_warehouse_id:int
    use_dm_new_datas:bool
    time_difference:int
    operation_discount_outer_kpp:int
    check_month_end:bool
    # COA ,mtr_coa_group fk ke finance-service
    coa_group_id:int
    with_vat:bool
    
    class Config:
        orm_mode = True
