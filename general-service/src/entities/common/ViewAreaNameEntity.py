from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrViewAreaName(Base):
    __tablename__ = 'mtr_view_area_name'
    is_active = Column(Boolean, default=True, nullable=False)
    view_area_name_id = Column(Integer, autoincrement=True, primary_key=True)
    view_area_name_code = Column(String(20),nullable=False, unique=True)
    view_area_name_description = Column(String(256), nullable=False)