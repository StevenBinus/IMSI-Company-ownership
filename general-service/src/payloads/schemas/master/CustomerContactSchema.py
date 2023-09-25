from typing import List,Optional
from pydantic import BaseModel

class MtrCustomerContactSchema(BaseModel):
    contact_name:Optional[str]=None
    description:Optional[str]=None
    phone_number:Optional[str]=None