from sqlalchemy import Column, Boolean, Integer, String
from src.configs.database import Base


class MtrProspectGroup(Base):
    __tablename__ = "mtr_prospect_group"
    is_active = Column(Boolean, nullable=False, default=True)
    prospect_group_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True
    )
    prospect_group_code = Column(String(5), nullable=False, default="")
    prospect_group_name = Column(String(50), nullable=True, default="")
