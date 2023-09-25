from pydantic import BaseModel

class PaginationSchema(BaseModel):
    rows:list = []

    class Config:
        orm_mode = True