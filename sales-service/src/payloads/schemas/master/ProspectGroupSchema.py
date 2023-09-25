from pydantic import BaseModel


class ProspectGroupRequest(BaseModel):
    prospect_group_code: str
    prospect_group_name: str


class ProspectGroupSchema(ProspectGroupRequest):
    is_active: bool
    prospect_group_id: int

    class Config:
        orm_mode = True
