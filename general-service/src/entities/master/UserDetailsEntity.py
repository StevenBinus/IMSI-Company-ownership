from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String, CHAR, DateTime, Float, ForeignKey, Boolean
from src.configs.database import Base,engine

class MtrUserDetails(Base):
    __tablename__ = 'mtr_user_details'
    is_active = Column(Boolean,nullable=False,default=True)
    user_employee_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, default=0)
    employee_name = Column(String(35), nullable=False, default="")
    employee_nickname = Column(String(30), nullable=True, default="")
    id_type_id = Column(Integer, ForeignKey("mtr_id_type.id_type_id"))
    id_number = Column(String(35), nullable=True, default="")
    company_id = Column(Integer, ForeignKey("mtr_company.company_id"), nullable=True)
    job_title_id = Column(Integer, ForeignKey("mtr_job_title.job_title_id"))
    job_position_id = Column(Integer, ForeignKey("mtr_job_position.job_position_id"))
    division_id = Column(Integer, ForeignKey("mtr_division.division_id"))
    cost_center_id = Column(Integer, ForeignKey("mtr_cost_center.cost_center_id"))
    profit_center_id = Column(Integer, ForeignKey("mtr_profit_center.profit_center_id"))
    address_id  = Column(Integer, ForeignKey("mtr_address.address_id"))
    office_phone_number = Column(String(30), nullable=True)
    home_phone_number = Column(String(30), nullable=True)
    mobile_phone = Column(String(30), nullable=True)
    email_address = Column(String(100), nullable=True)
    start_date = Column(DateTime, nullable=True)
    termination_date = Column(DateTime, nullable=True)
    gender = Column(CHAR(1), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    city_of_birth_id = Column(Integer, ForeignKey("mtr_city.city_id"))
    marital_status_id = Column(Integer, ForeignKey("mtr_marital_status.marital_status_id"))
    number_of_children = Column(Integer, nullable=True)
    citizenship = Column(String(35), nullable=True)
    last_education = Column(String(50), nullable=True)
    last_employment = Column(String(50), nullable=True)
    factor_x = Column(Float, nullable=True)
    skill_level_id = Column(Integer, ForeignKey("mtr_skill_level.skill_level_id"))

    employee_warranty = relationship("MtrCustomerWarranty", back_populates="warranty_employee", foreign_keys="MtrCustomerWarranty.employee_id")
    dealer_representative_customer = relationship("MtrCustomer", back_populates="customer_dealer_representative", foreign_keys="MtrCustomer.dealer_sales_representative")




    

    

