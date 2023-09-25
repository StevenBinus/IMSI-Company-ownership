from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MtrSupplierReferenceBankReference(BaseModel):
    bank_id :int
    account_type:str
    account_name :str
    account_number :str
    currency_id :int
    supplier_reference_id:int