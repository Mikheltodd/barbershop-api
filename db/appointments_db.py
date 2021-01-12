from sqlalchemy import Column, ForeignKey, Integer, String
from db.db_connection import Base, engine


class AppointmentInDB(Base):
    __tablename__ = "appointments"
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_date = Column(String)
    appointment_time = Column(String)
    appointment_status = Column(String)
    appointment_customer_id = Column(
        Integer, ForeignKey("customers.customer_id"))


Base.metadata.create_all(bind=engine)
