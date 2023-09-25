from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrModule(Base):
    __tablename__ = 'mtr_module'
    is_active = Column(Boolean, default=True, nullable=False)
    module_id = Column(Integer, autoincrement=True, primary_key=True)
    module_code = Column(String(5), nullable=False, unique=True)
    module_name = Column(String(100), nullable=False)