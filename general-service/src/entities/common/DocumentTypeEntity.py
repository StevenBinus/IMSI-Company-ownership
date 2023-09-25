from sqlalchemy import String,Column,Integer,Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrDocumentType(Base):
    __tablename__ = "mtr_document_type"
    is_active = Column(Boolean, default=True, nullable=False)
    document_type_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    document_type_code = Column(String(15), unique=True, nullable=False)
    document_type_description = Column(String(100), nullable=False)

    #back populates
    type_source_document = relationship("MtrDocument", back_populates="source_document_type", foreign_keys="MtrDocument.document_type_id")
    type_source_document_detail = relationship("MtrDocumentDetail", back_populates="source_document_detail_type", foreign_keys="MtrDocumentDetail.document_type_id")