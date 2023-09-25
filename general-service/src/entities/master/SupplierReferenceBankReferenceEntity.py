from sqlalchemy import String,Column,Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrSupplierReferenceBankReference(Base):
    __tablename__ = "mtr_supplier_reference_bank_reference"
    supplier_reference_bank_account_id=Column(Integer,primary_key=True,nullable=False)
    bank_id = Column(Integer,nullable=False)#FK ke mtr_bank dari finance
    account_type=Column(String(4),nullable=False)
    account_name = Column(String(60),nullable=False)
    account_number = Column(String(20),nullable=False)
    currency_id = Column(Integer,nullable=False)#FK dari mtr_currency fi finance
    is_active = Column(Boolean,nullable=False,default=True)
    supplier_reference_id=Column(Integer,ForeignKey("mtr_supplier_reference.supplier_reference_id"),nullable=False)

    #back populates
    supplier_reference_bank_reference=relationship("MtrSupplierReferenceEntity",back_populates="bank_reference_supplier_reference",foreign_keys=[supplier_reference_id])
