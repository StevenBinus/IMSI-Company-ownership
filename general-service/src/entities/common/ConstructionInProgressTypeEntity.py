from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrConstructionInProgressType(Base):
    __tablename__ = 'mtr_construction_in_progress_type'
    is_active = Column(Boolean, default=True, nullable=False)
    construction_in_progress_type_id = Column(Integer, autoincrement=True, primary_key=True)
    construction_in_progress_type_code = Column(String(10), nullable=False, unique=True)
    construction_in_progress_type_description = Column(String(50), nullable=False)