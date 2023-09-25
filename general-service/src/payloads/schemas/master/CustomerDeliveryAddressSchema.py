from typing import List,Optional
from pydantic import BaseModel

class MtrCustomerDeliveryAddressSchema(BaseModel):
    ship_to_name:str
    address_id:Optional[int]=None
    phone_number:Optional[str]=None
    fax_number:Optional[str]=None
    lead_times:Optional[int]=None
    contact_person:Optional[str]=None
    job_title_id:Optional[int]=None