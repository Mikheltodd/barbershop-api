from sqlalchemy import Column, Integer, String, DateTime
import datetime
from db.db_connection import Base, engine


class ServiceOrderInDB(Base):
    __tablename__ = "service_orders"
    service_order_id = Column(Integer, primary_key=True, autoincrement=True)
    service_order_datetime = Column(DateTime, default=datetime.datetime.utcnow)


Base.metadata.create_all(bind=engine)
