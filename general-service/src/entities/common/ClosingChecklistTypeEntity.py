from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrClosingChecklistType(Base):
    __tablename__ = 'mtr_closing_checklist_type'
    is_active = Column(Boolean, default=True, nullable=False)
    closing_checklist_type_id = Column(Integer, autoincrement=True, primary_key=True)
    closing_checklist_type_code = Column(String(25), nullable=False, unique=True)
    closing_checklist_type_description = Column(String(50), nullable=False)
