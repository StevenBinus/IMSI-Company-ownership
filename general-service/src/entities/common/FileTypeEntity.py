from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFileType(Base):
    __tablename__ = 'mtr_file_type'
    is_active = Column(Boolean, default=True, nullable=False)
    file_type_id = Column(Integer, autoincrement=True, primary_key=True)
    file_type_code = Column(String(10), nullable=False, unique=True)
    file_type_description = Column(String(50), nullable=False)