from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrItemClaimType(Base):
    __tablename__ = 'mtr_item_claim_type'
    is_active = Column(Boolean, default=True, nullable=False)
    item_claim_type_id = Column(Integer, autoincrement=True, primary_key=True)
    item_claim_type_code = Column(String(10), nullable=False, unique=True)
    item_claim_type_description = Column(String(50), nullable=False)