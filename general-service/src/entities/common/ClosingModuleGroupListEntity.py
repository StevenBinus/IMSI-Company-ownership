from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrClosingModuleGrouplist(Base):
    __tablename__ = 'mtr_closing_module_grouplist'
    is_active = Column(Boolean, default=True, nullable=False)
    closing_module_grouplist_id = Column(Integer, autoincrement=True, primary_key=True)
    closing_module_grouplist_code = Column(String(25), nullable=False, unique=True)
    closing_module_grouplist_description = Column(String(50), nullable=False)