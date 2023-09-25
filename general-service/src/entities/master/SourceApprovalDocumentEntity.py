from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSourceApprovalDocument(Base):
    __tablename__ = 'mtr_source_approval_document'
    is_active = Column(Boolean, default=True, nullable=False)
    source_approval_document_id = Column(Integer, autoincrement=True, primary_key=True)
    source_approval_document_code = Column(String(20), nullable=False, unique=True)
    source_approval_document_name = Column(String(256), nullable=False,)