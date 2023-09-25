from sqlalchemy import String,Column,Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrDocument(Base):
    __tablename__ = "mtr_document"
    is_active = Column(Boolean,default=True,nullable=False)
    document_id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    document_type_id = Column(Integer, ForeignKey("mtr_document_type.document_type_id"), nullable=False)
    brand_id = Column(Integer, nullable=False) #FK with mtr_brand in sales service
    profit_center_id = Column(Integer, ForeignKey("mtr_profit_center.profit_center_id"), nullable=False)
    transaction_type_id = Column(Integer,ForeignKey("mtr_transaction_type.transaction_type_id") , nullable=False)
    bank_company_id = Column(Integer, nullable=False) # FK with mtr_bank_company finance service
    reset_frequency_id = Column(Integer, ForeignKey("mtr_reset_frequency.reset_frequency_id"), nullable=False)
    document_name = Column(String(128), nullable=False)
    document_format = Column(String(50), nullable=False)
    document_reference = Column(Boolean, nullable=False)
    signature_employee_1 = Column(Integer, nullable=False) #FK with mtr_user_details user service
    signature_title_1 = Column(String(50), nullable=False)
    signature_employee_2 = Column(Integer, nullable=False) #FK with mtr_user_details user service
    signature_title_2 = Column(String(50), nullable=False)
    signature_employee_3 = Column(Integer, nullable=False) #FK with mtr_user_details user service
    signature_title_3 = Column(String(50), nullable=False)
    signature_employee_4 = Column(Integer, nullable=False) #FK with mtr_user_details user service
    signature_title_4 = Column(String(50), nullable=False)
    document_source_doc_prefix = Column(String(128), nullable=True)
    document_brand_prefix = Column(String(128), nullable=True)
    document_profit_cost_center_prefix = Column(String(128), nullable=True)
    document_transaction_type_prefix = Column(String(128), nullable=True)
    document_bank_acc_prefix = Column(String(128), nullable=True)
    document_auto_number = Column(Boolean, nullable=False)

    #back populates
    source_document_type = relationship("MtrDocumentType", back_populates="type_source_document", foreign_keys=[document_type_id])
    source_document_profit_center = relationship("MtrProfitCenter", back_populates="profit_center_source_document", foreign_keys=[profit_center_id])
    source_document_transaction_type = relationship("MtrTransactionType", back_populates="transaction_type_source_document", foreign_keys=[transaction_type_id])
    source_document_reset_frequency = relationship("MtrResetFrequency", back_populates="reset_frequency_source_document", foreign_keys=[reset_frequency_id])