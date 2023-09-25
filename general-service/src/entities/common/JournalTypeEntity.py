from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrJournalType(Base):
    __tablename__ = 'mtr_journal_type'
    is_active = Column(Boolean, default=True, nullable=False)
    journal_type_id = Column(Integer, autoincrement=True, primary_key=True)
    journal_type_code = Column(String(5), nullable=False, unique=True)
    journal_type_name = Column(String(100), nullable=False)