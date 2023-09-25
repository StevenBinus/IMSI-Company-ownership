from src.configs.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class TrxVehicleSalesOrderTakeDetail(Base):
    __tablename__ = "trx_vehicle_sales_order_take_detail"
    taken_detail_system_number = Column(Integer,primary_key=True,autoincrement=True)
    taken_detail_system_number_old = Column(Integer,nullable=True)
    taken_system_number = Column(Integer,ForeignKey("trx_vehicle_sales_order_take.taken_system_number"))
    vehicle_sales_order_document_number = Column(String(25),unique=True,nullable=False)
    vehicle_sales_order_system_number = Column(Integer,ForeignKey("trx_vehicle_sales_order_form_registration.register_system_number"))

    #back populates
    takensysnodetail_header = relationship("TrxVehicleSalesOrderTake",back_populates="takensysnoheader_detail",
                                           foreign_keys=[taken_system_number])
    takedetail_spmreg = relationship("TrxVehicleSalesOrderFormRegistration",back_populates="spmreg_takedetail",
                                     foreign_keys=[vehicle_sales_order_system_number])