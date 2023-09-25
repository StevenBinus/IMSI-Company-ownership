from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrGRPOReturnReferenceType(Base):
    __tablename__ = 'mtr_grpo_return_reference_type'
    is_active = Column(Boolean, default=True, nullable=False)
    grpo_return_reference_type_id = Column(Integer, autoincrement=True, primary_key=True)
    grpo_return_reference_type_code = Column(String(10), nullable=False, unique=True)
    grpo_return_reference_type_description = Column(String(50), nullable=False)