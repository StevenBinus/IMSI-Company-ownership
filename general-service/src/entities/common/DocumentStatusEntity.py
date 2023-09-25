from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrDocumentStatus(Base):
    __tablename__ = 'mtr_document_status'
    is_active = Column(Boolean, default=True, nullable=False)
    document_status_id = Column(Integer, autoincrement=True, primary_key=True)
    document_status_code = Column(String(10), nullable=False, unique=True)
    document_status_description = Column(String(50), nullable=False)