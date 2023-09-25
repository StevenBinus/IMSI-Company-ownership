from sqlalchemy import String,Column,Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrSupplierBankAccount(Base):
    __tablename__ = "mtr_supplier_bank_account"
    supplier_bank_account_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    is_active = Column(Boolean, default=True, nullable=False)
    bank_id = Column(Integer, nullable=False) #Fk dari tabel mtr_bank (dari finance service)
    account_type_id = Column(Integer, ForeignKey("mtr_bank_account_type.bank_account_type_id"), nullable=False)
    account_name = Column(String(60), nullable=False)
    account_no = Column(String(20), nullable=False)
    currency_id = Column(Integer, nullable=False) #Fk dari tabel mtr_currency (dari finance service)
    supplier_id = Column(Integer, ForeignKey("mtr_supplier.supplier_id"), nullable=False)

    #back populates
    supplier_bank_account_type = relationship("MtrBankAccountType", back_populates="bank_account_type_supplier", foreign_keys=[account_type_id])
    bank_account_supplier = relationship("MtrSupplier", back_populates="supplier_bank_account", foreign_keys=[supplier_id])