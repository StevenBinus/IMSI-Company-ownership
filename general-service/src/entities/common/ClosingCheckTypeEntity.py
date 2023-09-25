from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrClosingCheckType(Base):
    __tablename__ = 'mtr_closing_check_type'
    is_active = Column(Boolean, default=True, nullable=False)
    closing_check_type_id = Column(Integer, autoincrement=True, primary_key=True)
    closing_check_type_code = Column(String(5), nullable=False, unique=True)
    closing_check_type_description = Column(String(50), nullable=False)