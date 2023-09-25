from pydantic import BaseModel


class ProspectSourceCreateRequest(BaseModel):
    prospect_group_id: int
    company_id: int
    prospect_source_code: str
    prospect_source_name: str


class ProspectSourceUpdateRequest(BaseModel):
    prospect_source_name: str
    prospect_group_id: int


class ProspectSourceSchema(ProspectSourceCreateRequest, ProspectSourceUpdateRequest):
    is_active: bool
    prospect_source_id: int

    class Config:
        orm_mode = True
