from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCompanyReference(Base):
    __tablename__ = "mtr_company_reference"
    is_active = Column(Boolean, nullable=False, default=True)
    company_id=Column(Integer,ForeignKey("mtr_company"),primary_key=True)
    # Currency_id, mtr_currency FK ke finance-service
    currency_id=Column(Integer,nullable=False)
    margin_outer_kpp=Column(Integer,nullable=True)
    adjustment_reason_id=Column(Integer,ForeignKey("mtr_adjustment_reason.adjustment_reason_id"))
    lead_time_unit_etd=Column(Integer,nullable=True)
    # bank_acc_receive_company_id FK dari mtr_bank_company di finance-service
    bank_acc_receive_company_id=Column(Integer,nullable=False)
    vat_code=Column(String(50),nullable=False)
    # kedua warehouse id dari mtr_warehouse di aftersales-service
    item_broken_warehouse_id=Column(Integer,nullable=False)
    unit_warehouse_id=Column(Integer,nullable=False)
    use_dms=Column(Boolean,nullable=False,default=False)
    time_difference=Column(Integer,nullable=True)
    operation_discount_outer_kpp=Column(Integer,nullable=True)
    check_month_end=Column(Boolean,nullable=True,default=False)
    # COA ,mtr_coa_group fk ke finance-service
    coa_group_id=Column(Integer,nullable=False)
    with_vat=Column(Boolean,nullable=True,default=False)
    approval_spm_id=Column(Integer,ForeignKey("mtr_approval_spm.approval_spm_id"))
    is_use_tax_industry=Column(Boolean,nullable=True,default=False)
    markup_percentage=Column(Integer,nullable=True,default=False)
    is_external_pdi=Column(Boolean,nullable=True,default=False)
    hide_cost=Column(Boolean,nullable=True,default=False)
    use_price_code=Column(Boolean,nullable=True,default=False)
    disable_edit_draft_soinvoice=Column(Boolean,nullable=False,default=False)

    #back populates
    company_comref=relationship("MtrCompany",back_populates="comref_company",foreign_keys=[company_id])
    adjustment_comref=relationship("MtrAdjustmentReason",back_populates="comref_adjustment",foreign_keys=[adjustment_reason_id])
    appspm_comref=relationship("MtrApprovalSpm",back_populates="comref_appspm",foreign_keys=[approval_spm_id] )
   

   