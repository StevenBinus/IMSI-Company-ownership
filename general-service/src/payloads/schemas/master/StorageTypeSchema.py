from pydantic import BaseModel

class MtrStorageTypeRequest(BaseModel):
    storage_type_code: str
    storage_type_name: str

class MtrStorageTypeUpdateRequest(BaseModel):
    storage_type_name: str

class MtrStorageTypeSchema(MtrStorageTypeRequest):
    is_active: bool
    storage_type_id: int

    class config:
        orm_mode = True