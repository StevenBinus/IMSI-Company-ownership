from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrClaimType(Base):
    __tablename__ = 'mtr_claim_type'
    is_active = Column(Boolean, default=True, nullable=False)
    claim_type_id = Column(Integer, autoincrement=True, primary_key=True)
    claim_type_code = Column(String(10), nullable=False, unique=True)
    claim_type_description = Column(String(50), nullable=False)
