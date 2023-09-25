from pydantic import BaseModel
from typing import Optional

class MtrDealerRepresentativeSchema(BaseModel):
    dealer_representative_code:float
    dealer_representative_name:Optional[str] = None
    dealer_representative_cost_center_sequence:Optional[float] = None

    class Config:
        orm_mode = True

