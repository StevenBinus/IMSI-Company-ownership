from typing import List, Optional
from pydantic import BaseModel

class MtrRequestForPaymentReferenceTypeGetSchema(BaseModel):
    request_for_payment_reference_type_code:Optional[str] = None
    request_for_payment_reference_type_description:Optional[str] = None
    
    class Config:
        orm_mode = True