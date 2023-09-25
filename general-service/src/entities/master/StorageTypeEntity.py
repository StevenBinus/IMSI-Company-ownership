from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrStorageType(Base):
    __tablename__ = "mtr_storage_type"
    is_active = Column(Boolean, default=True, nullable=False)
    storage_type_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    storage_type_code = Column(String(20), nullable=False)
    storage_type_name = Column(String(50), nullable=False)