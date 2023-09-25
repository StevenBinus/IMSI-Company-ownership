from typing import List,Optional
from pydantic import BaseModel

class MtrCustomerByDealerSchema(BaseModel):
    company_id:int     