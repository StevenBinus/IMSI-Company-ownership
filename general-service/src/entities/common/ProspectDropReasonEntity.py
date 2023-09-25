from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrProspectDropReason(Base):
    __tablename__ = 'mtr_prospect_drop_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    prospect_drop_reason_id = Column(Integer, autoincrement=True, primary_key=True)
    prospect_drop_reason_code = Column(String(20),nullable=False, unique=True)
    prospect_drop_reason_description = Column(String(256), nullable=False)