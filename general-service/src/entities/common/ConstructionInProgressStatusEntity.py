from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrConstructionInProgressStatus(Base):
    __tablename__ = 'mtr_construction_in_progress_status'
    is_active = Column(Boolean, default=True, nullable=False)
    construction_in_progress_status_id = Column(Integer, autoincrement=True, primary_key=True)
    construction_in_progress_status_code = Column(String(10), nullable=False, unique=True)
    construction_in_progress_status_description = Column(String(50), nullable=False)