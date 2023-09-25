from pydantic import BaseModel
from typing import List, Optional

class MtrSupplierReferencePic(BaseModel):
    pic_code :str
    pic_name :str
    pic_division_id :int
    pic_position_id :int
    pic_mobile_phone:str
    supplier_reference_id:int