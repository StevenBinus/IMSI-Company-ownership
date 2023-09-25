from pydantic import BaseModel

class MtrDivisionRequest(BaseModel):
    division_code: str
    division_name: str

class MtrDivisionUpdateRequest(BaseModel):
    division_name: str

class MtrStorageTypeSchema(MtrDivisionRequest):
    is_active: bool
    division_id: int

    class config:
        orm_mode = True