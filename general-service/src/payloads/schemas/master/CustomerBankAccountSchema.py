from typing import List,Optional
from pydantic import BaseModel

class MtrCustomerBankAccountSchema(BaseModel):
    bank_id:int
    bank_account_type_id:Optional[int]=None    
    bank_account_name:Optional[str]=None
    bank_account_number:str
    currency_id:Optional[int]=None

class MtrCustomerBankAccountUpdateSchema(BaseModel):
    bank_account_name:Optional[str]=None
    currency_id:Optional[int]=None
