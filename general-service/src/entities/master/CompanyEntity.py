from sqlalchemy import (
    CHAR,
    String,
    Integer,
    Boolean,
    Column,
    ForeignKey,
    DateTime,
    Float,
)
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrCompany(Base):
    __tablename__ = "mtr_company"
    is_active = Column(Boolean, nullable=False, default="True")
    company_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    company_code = Column(String(10), nullable=False, unique=True, default="")
    company_type = Column(CHAR(1), nullable=False)
    company_name = Column(String(100), nullable=False)
    company_abbreviation = Column(String(15), nullable=False, default="")
    company_office_address_id = Column(Integer, ForeignKey("mtr_address.address_id"))
    company_phone_number = Column(String(30), nullable=True, default="")
    company_fax_number = Column(String(30), nullable=True, default="")
    company_email = Column(String(128), nullable=True, default="")
    vat_company_id = Column(Integer, ForeignKey("mtr_vat_company.vat_company_id"))
    tax_npwp_no = Column(String(30), nullable=False)
    tax_npwp_date = Column(DateTime, nullable=True, default="")
    tax_name = Column(String, nullable=True, default="")
    tax_address_id = Column(Integer, ForeignKey("mtr_address.address_id"))
    tax_pkp_type = Column(CHAR(1), nullable=True, default="")
    tax_pkp_no = Column(String(30), nullable=True, default="")
    tax_pkp_date = Column(DateTime, nullable=True, default="")
    tax_office_id = Column(Integer, ForeignKey("mtr_tax_office.tax_office_id"))
    region_id = Column(Integer, ForeignKey("mtr_region.region_id"))
    finance_area_id = Column(Integer, ForeignKey("mtr_finance_area.finance_area_id"))
    area_id = Column(Integer, ForeignKey("mtr_area.area_id"))
    incentive_group_id = Column(
        Integer, nullable=False
    )  # FK to mtr_incentive_group on aftersales service
    aftersales_area_id = Column(
        Integer, ForeignKey("mtr_aftersales_area.after_sales_area_id")
    )
    company_ownership_id = Column(
        Integer, ForeignKey("mtr_company_ownership.company_ownership_id")
    )
    business_category_id = Column(
        Integer, ForeignKey("mtr_business_category.business_category_id")
    )
    business_scope_id = Column(
        Integer, ForeignKey("mtr_business_scope.business_scope_id")
    )
    term_of_payment_id = Column(
        Integer, ForeignKey("mtr_term_of_payment.term_of_payment_id")
    )
    company_dealer_kia_code = Column(String(10), nullable=True, default="")
    company_no_of_stall = Column(Float, nullable=True, default=0)
    is_distributor = Column(Boolean, nullable=True, default=False)
    
    # # back populates
    address_company = relationship(
        "MtrAddress",
        back_populates="company_address",
        foreign_keys=[company_office_address_id],
    )
    vat_company = relationship(
        "MtrVatCompany", back_populates="company_vat", foreign_keys=[vat_company_id]
    )
    address_tax = relationship(
        "MtrAddress", back_populates="tax_address", foreign_keys=[tax_address_id]
    )
    taxoffice_company = relationship(
        "MtrTaxOffice", back_populates="company_taxoffice", foreign_keys=[tax_office_id]
    )
    # region_company = relationship(
    #     "MtrRegion", back_populates="company_region", foreign_keys=[region_id]
    # )
    finance_area_company = relationship(
        "MtrFinanceArea",
        back_populates="company_finance_area",
        foreign_keys=[finance_area_id],
    )
    area_company = relationship(
        "MtrArea", back_populates="company_area", foreign_keys=[area_id]
    )
    aftersales_area_company = relationship(
        "MtrAfterSalesArea",
        back_populates="company_aftersales_area",
        foreign_keys=[aftersales_area_id],
    )
    ownership_company = relationship(
        "MtrCompanyOwnership",
        back_populates="company_ownership",
        foreign_keys=[company_ownership_id],
    )
    business_category_company = relationship(
        "MtrBusinessCategory",
        back_populates="company_business_category",
        foreign_keys=[business_category_id],
    )
    business_scope_company = relationship(
        "MtrBusinessScope",
        back_populates="company_business_scope",
        foreign_keys=[business_scope_id],
    )
    term_of_payment_company = relationship(
        "MtrTermOfPayment",
        back_populates="company_term_of_payment",
        foreign_keys=[term_of_payment_id],
    )
    customer_company_id_bfk = relationship("MtrCustomer", back_populates="company_id_fk", foreign_keys="MtrCustomer.company_id")
    company_customer_va_bfk = relationship("MtrCustomerVirtualAccount", back_populates="company_customer_va_fk", foreign_keys="MtrCustomerVirtualAccount.company_id")
    company_source_document_detail = relationship("MtrDocumentDetail", back_populates="source_document_detail_company", foreign_keys="MtrDocumentDetail.company_id")
    customer_company_id_bfk = relationship("MtrCustomer", back_populates="company_id_fk", foreign_keys="MtrCustomer.company_id")
    company_cost_bfk = relationship("MtrCostProfitMap", back_populates="company_cost_fk", foreign_keys="MtrCostProfitMap.company_id")
    dealer_name_bfk = relationship("MtrCustomer", back_populates="dealer_name_fk", foreign_keys="MtrCustomer.dealer_name_id")
    company_bfk = relationship("MtrCustomerByDealer",back_populates="company_fk",foreign_keys="MtrCustomerByDealer.company_id")
    comref_company=relationship("MtrCompanyReference",back_populates="company_comref",foreign_keys="MtrCompanyReference.company_id")

    reference_company=relationship("MtrSupplierReferenceEntity",back_populates="company_reference",foreign_keys="MtrSupplierReferenceEntity.company_id")

    
    company_source_document_detail = relationship(
        "MtrDocumentDetail",
        back_populates="source_document_detail_company",
        foreign_keys="MtrDocumentDetail.company_id",
    )
    customer_company_id_bfk = relationship(
        "MtrCustomer",
        back_populates="company_id_fk",
        foreign_keys="MtrCustomer.company_id",
    )
    dealer_name_bfk = relationship(
        "MtrCustomer",
        back_populates="dealer_name_fk",
        foreign_keys="MtrCustomer.dealer_name_id",
    )
    # company_vatcompany = relationship(
    #     "MtrVatCompany",
    #     back_populates="vatcompany_company",
    #     foreign_keys="MtrVatCompany.company_id"
    # )
    company_company_id = relationship(
        "MtrVatCompany",
        back_populates="company_id_company",
        foreign_keys="MtrVatCompany.company_id",
    )
    company_bfk = relationship(
        "MtrCustomerByDealer",
        back_populates="company_fk",
        foreign_keys="MtrCustomerByDealer.company_id",
    )
    comref_company = relationship(
        "MtrCompanyReference",
        back_populates="company_comref",
        foreign_keys="MtrCompanyReference.company_id",
    )
