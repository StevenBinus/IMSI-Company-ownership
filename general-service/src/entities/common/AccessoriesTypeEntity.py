from sqlalchemy import Column, Integer,Boolean,String
from src.configs.database import Base

class MtrAccessoriesType(Base):
    __tablename__ = 'mtr_accessories_type'
    is_active = Column(Boolean, default=True, nullable=False)
    accessories_type_id = Column(Integer, autoincrement=True, primary_key=True)
    accessories_type_code = Column(String(25),nullable=False, unique=True)
    accessories_type_description = Column(String(50), nullable=False)