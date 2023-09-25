from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrTransactionType(Base):
    __tablename__ = 'mtr_transaction_type'
    is_active = Column(Boolean, default=True, nullable=False)
    transaction_type_id = Column(Integer, autoincrement=True, primary_key=True)
    transaction_type_code = Column(String(20), nullable=False, unique=True)
    transaction_type_name = Column(String(256), nullable=False,)

    #back populates
    transaction_type_source_document = relationship("MtrDocument", back_populates="source_document_transaction_type", foreign_keys="MtrDocument.transaction_type_id")
    transaction_type_source_document_detail = relationship("MtrDocumentDetail", back_populates="source_document_detail_transaction_type", foreign_keys="MtrDocumentDetail.transaction_type_id")