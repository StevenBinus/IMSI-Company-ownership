from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSubstituteType(Base):
    __tablename__ = 'mtr_substitute_type'
    is_active = Column(Boolean, default=True, nullable=False)
    substitute_type_id = Column(Integer, autoincrement=True, primary_key=True)
    substitute_type_code = Column(String(1), primary_key=True)
    substitute_type_name = Column(String(50), nullable=False)