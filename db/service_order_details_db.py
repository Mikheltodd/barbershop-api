from sqlalchemy import Column, Integer, String, ForeignKey, Float
from db.db_connection import Base, engine


class ServiceOrderDetailInDB(Base):
    __tablename__ = "service_order_details"
    service_order_detail_id = Column(
        Integer, primary_key=True, autoincrement=True)
    service_order_detail_service_id = Column(
        Integer, ForeignKey("services.service_id"))
    service_order_detail_quantity = Column(Integer)
    service_order_detail_amount = Column(Float)
    service_order_detail_service_order_id = Column(
        Integer, ForeignKey("service_orders.service_order_id"))
    service_order_detail_employee_id = Column(
        Integer, ForeignKey("employees.employee_id"))


Base.metadata.create_all(bind=engine)
