from sqlalchemy import String, Column, Integer, Boolean, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrDocumentDetail(Base):
    __tablename__ = "mtr_document_detail"
    is_active = Column(Boolean, nullable=False, default=True)
    document_detail_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )
    document_type_id = Column(
        Integer, ForeignKey("mtr_document_type.document_type_id"), nullable=False
    )
    company_id = Column(Integer, ForeignKey("mtr_company.company_id"), nullable=False)
    brand_id = Column(Integer, nullable=False)  # FK to mtr_brand from sales service
    profit_center_id = Column(
        Integer, ForeignKey("mtr_profit_center.profit_center_id"), nullable=False
    )
    transaction_type_id = Column(
        Integer, ForeignKey("mtr_transaction_type.transaction_type_id"), nullable=False
    )
    period_year = Column(String(4), nullable=False)
    period_month = Column(CHAR(2), nullable=False)
    bank_company_id = Column(
        Integer, nullable=False
    )  # FK with mtr_bank_company finance service
    last_document_number = Column(Integer, nullable=False)

    # back populates
    source_document_detail_type = relationship(
        "MtrDocumentType",
        back_populates="type_source_document_detail",
        foreign_keys=[document_type_id],
    )
    source_document_detail_company = relationship("MtrCompany", back_populates="company_source_document_detail", foreign_keys=[company_id])
    source_document_detail_profit_center = relationship(
        "MtrProfitCenter",
        back_populates="profit_center_source_document_detail",
        foreign_keys=[profit_center_id],
    )
    source_document_detail_transaction_type = relationship(
        "MtrTransactionType",
        back_populates="transaction_type_source_document_detail",
        foreign_keys=[transaction_type_id],
    )
