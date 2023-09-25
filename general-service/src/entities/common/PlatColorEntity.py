from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrPlatColor(Base):
    __tablename__ = 'mtr_plat_color'
    is_active = Column(Boolean, default=True, nullable=False)
    plat_color_id = Column(Integer, autoincrement=True, primary_key=True)
    plat_color_code = Column(String(20),nullable=False, unique=True)
    plat_color_description = Column(String(256), nullable=False)