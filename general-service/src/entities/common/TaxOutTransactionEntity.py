from sqlalchemy import Column,Boolean,String,Integer
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrVATTransactionCode(Base):
    __tablename__ = "mtr_vat_transaction_code"
    is_active = Column(Boolean,nullable=False,default=True)
    vat_transaction_code_id = Column(Integer,autoincrement=True,primary_key=True)
    vat_transaction_code = Column(String(20),nullable=False)
    vat_transaction_name = Column(String(256),nullable=True,default="")

    #back populates
    vat_company_taxouttrans = relationship("MtrVatCompany", back_populates="taxouttrans_vat_company", foreign_keys="MtrVatCompany.vat_tax_out_transaction_id")
    customer_vat_transaction_id_bfk = relationship("MtrCustomer", back_populates="vat_transaction_id_fk", foreign_keys="MtrCustomer.vat_transaction_id")
    vat_supply_reference=relationship("MtrSupplierReferenceEntity",back_populates="supplier_reference_vat",foreign_keys="MtrSupplierReferenceEntity.vat_transaction_id")