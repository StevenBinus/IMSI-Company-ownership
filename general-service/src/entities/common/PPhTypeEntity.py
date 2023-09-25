from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrPPhType(Base):
    __tablename__ = 'mtr_pph_type'
    is_active = Column(Boolean, default=True, nullable=False)
    pph_type_id = Column(Integer, autoincrement=True, primary_key=True)
    pph_type_code = Column(String(20),nullable=False, unique=True)
    pph_type_description = Column(String(256), nullable=False)