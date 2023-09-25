from sqlalchemy import String,Column,Integer, Boolean
from sqlalchemy.orm import relationship 
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrBankAccountType(Base):
    __tablename__ = 'mtr_bank_account_type'
    is_active = Column(Boolean, default=True, nullable=False)
    bank_account_type_id = Column(Integer, autoincrement=True, primary_key=True)
    bank_account_type_code = Column(String(20), nullable=False, unique=True)
    bank_account_type_name = Column(String(256), nullable=False)

    #back populates
    bank_account_type_bfk = relationship("MtrCustomerBankAccount", back_populates="bank_account_type_fk", foreign_keys="MtrCustomerBankAccount.bank_account_type_id")
    bank_account_type_supplier = relationship("MtrSupplierBankAccount", back_populates="supplier_bank_account_type", foreign_keys="MtrSupplierBankAccount.account_type_id")