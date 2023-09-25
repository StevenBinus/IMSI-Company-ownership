from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrUniqueSpecificationType(Base):
    __tablename__ = 'mtr_unique_specification_type'
    is_active = Column(Boolean, default=True, nullable=False)
    unique_specification_type_id = Column(Integer, autoincrement=True, primary_key=True)
    unique_specification_type_code = Column(String(20),nullable=False, unique=True)
    unique_specification_type_description = Column(String(256), nullable=False)