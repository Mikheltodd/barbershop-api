from sqlalchemy import Column, Integer, String, ForeignKey
from db.db_connection import Base, engine


class AppointmentDetailInDB(Base):
    __tablename__ = "appointment_details"
    appointment_detail_id = Column(
        Integer, primary_key=True, autoincrement=True)
    appointment_detail_employee_id = Column(
        Integer, ForeignKey("employees.employee_id"))
    appointment_detail_service_id = Column(
        Integer, ForeignKey("services.service_id"))
    appointment_detail_appointment_id = Column(
        Integer, ForeignKey("appointments.appointment_id"))


Base.metadata.create_all(bind=engine)
