from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBodyType(Base):
    __tablename__ = 'mtr_body_type'
    is_active = Column(Boolean, default=True, nullable=False)
    body_type_id = Column(Integer, autoincrement=True, primary_key=True)
    body_type_code = Column(String(10), nullable=False, unique=True)
    body_type_description = Column(String(50), nullable=False)
