from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
import datetime
from db.db_connection import Base, engine


class BillInDB(Base):
    __tablename__ = "bills"
    bill_id = Column(
        Integer, primary_key=True, autoincrement=True)
    bill_datetime = Column(DateTime, default=datetime.datetime.utcnow)
    bill_total = Column(
        Float)
    bill_discount = Column(
        Float)
    bill_discount_id = Column(Integer, ForeignKey("discounts.discount_id"))
    bill_customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    bill_service_order_id = Column(
        Integer, ForeignKey("service_orders.service_order_id"))


Base.metadata.create_all(bind=engine)
