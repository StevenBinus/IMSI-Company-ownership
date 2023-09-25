from typing import List, Optional
from pydantic import BaseModel

class MtrCustomerVirtualAccountSchema(BaseModel):
    customer_id :int
    company_id :int
    profit_center_id :int
    account_bank_company :int