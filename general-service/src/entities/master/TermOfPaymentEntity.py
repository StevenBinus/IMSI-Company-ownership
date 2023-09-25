from sqlalchemy import Column, Boolean, String, Integer, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base, engine


class MtrTermOfPayment(Base):
    __tablename__ = "mtr_term_of_payment"
    is_active = Column(Boolean, nullable=False, default=True)
    term_of_payment_id = Column(Integer, primary_key=True)
    term_of_payment_code = Column(String(5), nullable=False, unique=True)
    term_of_payment_installment = Column(Integer, nullable=True, default=0)
    term_of_payment_interval = Column(Integer, nullable=True, default=0)
    term_of_payment_name = Column(String(100), nullable=True, default="")
    term_of_payment_policy = Column(CHAR(1), nullable=True, default="")

    #back populates
    reference_term_of_payment = relationship("MtrSupplierReferenceEntity",
                                             back_populates="term_of_payment_reference",
                                             foreign_keys="MtrSupplierReferenceEntity.term_of_payment_id")
    # back populates
    company_term_of_payment = relationship(
        "MtrCompany",
        back_populates="term_of_payment_company",
        foreign_keys="MtrCompany.term_of_payment_id",
    )
    term_of_payment_supplier = relationship(
        "MtrSupplier",
        back_populates="supplier_term_of_payment",
        foreign_keys="MtrSupplier.term_of_payment_id",
    )
    customer_term_of_payment_id_bfk = relationship(
        "MtrCustomer",
        back_populates="term_of_payment_id_fk",
        foreign_keys="MtrCustomer.term_of_payment_id",
    )
