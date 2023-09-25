from sqlalchemy import String,Column,Integer, Boolean, ForeignKey, DateTime, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrSupplier(Base):
    __tablename__ = "mtr_supplier"
    # company_id = Column(Integer, ForeignKey("mtr_company.company_id"), nullable=False)
    company_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    effective_date = Column(DateTime, nullable=True)
    supplier_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    supplier_code = Column(String(20), nullable=False, unique=True)
    supplier_title_prefix = Column(String(20), nullable=True)
    supplier_name = Column(String(100), nullable=False)
    supplier_title_suffix = Column(String(20), nullable=True)
    supplier_type_id = Column(Integer, nullable=False) #Fk dari table mtr_supplier_type
    term_of_payment_id = Column(Integer, ForeignKey("mtr_term_of_payment.term_of_payment_id"), nullable=False)
    default_currency_id = Column(Integer, nullable=True) #Fk dari table mtr_currency (ada di finance service)
    via_binning = Column(Boolean, nullable=True)
    is_import_supplier = Column(Boolean, nullable=True)
    supplier_invoice_type_id = Column(Integer, nullable=True) #Fk dari tabel comGenVariable where VARIABLE like 'SUP_INVOICE_TYPE_%'
    supplier_unique_id = Column(String(50), nullable=False)
    supplier_address_id = Column(Integer, ForeignKey("mtr_address.address_id"), nullable=False)
    supplier_phone_no = Column(String(30), nullable=True)
    supplier_fax_no = Column(String(30), nullable=True)
    supplier_mobile_phone = Column(String(30), nullable=False)
    supplier_email_address = Column(String(128), nullable=True)
    minimum_down_payment = Column(Integer, nullable=True)
    supplier_behaviour_id = Column(Integer, ForeignKey("mtr_supplier_behaviour.supplier_behaviour_id"), nullable=True)
    supplier_class_id = Column(Integer, ForeignKey("mtr_customer_class.customer_class_id"), nullable=True)
    vat_npwp_no = Column(String(30), nullable=False)
    vat_npwp_date = Column(DateTime, nullable=False)
    vat_pkp_type = Column(CHAR(1), nullable=False)
    vat_pkp_no = Column(String(30), nullable=True)
    vat_pkp_date = Column(DateTime, nullable=True)
    vat_transaction_id = Column(Integer, nullable=True) #Fk dari tabel mtr_vat_transacntion_code belum dibuat
    vat_name = Column(String(100), nullable=False)
    vat_address_id = Column(Integer, ForeignKey("mtr_address.address_id"), nullable=False)
    vat_tax_office = Column(Integer, nullable=True) #Fk dari tabel mtr_tax_office belum dibuat
    tax_npwp_no = Column(String(30), nullable=False)
    tax_npwp_date = Column(DateTime, nullable=False)
    tax_pkp_type = Column(CHAR, nullable=False)
    tax_pkp_no = Column(String(30), nullable=True)
    tax_pkp_date = Column(DateTime, nullable=True)
    tax_name = Column(String(100), nullable=False)
    tax_address_id = Column(Integer, ForeignKey("mtr_address.address_id"),nullable=False)
    tax_tax_office_id = Column(Integer, nullable=True) #Fk dari table mtr_tax_office

    # back populates
    # supplier_company = relationship("MtrCompany", back_populates="company_supplier", foreign_keys=[company_id])
    supplier_term_of_payment = relationship("MtrTermOfPayment", back_populates="term_of_payment_supplier", foreign_keys=[term_of_payment_id])
    supplier_address = relationship("MtrAddress", back_populates="address_supplier", foreign_keys=[supplier_address_id])
    supplier_behaviour = relationship("MtrSupplierBehaviour", back_populates="behaviour_supplier", foreign_keys=[supplier_behaviour_id])
    supplier_customer_class = relationship("MtrCustomerClass", back_populates="customer_class_supplier", foreign_keys=[supplier_class_id])
    supplier_vat_address = relationship("MtrAddress", back_populates="address_supplier_vat", foreign_keys=[vat_address_id])
    supplier_tax_address = relationship("MtrAddress", back_populates="address_supplier_tax", foreign_keys=[tax_address_id])
    supplier_pic = relationship("MtrSupplierPIC", back_populates="pic_supplier", foreign_keys="MtrSupplierPIC.supplier_id")
    supplier_bank_account = relationship("MtrSupplierBankAccount", back_populates="bank_account_supplier", foreign_keys="MtrSupplierBankAccount.supplier_id")