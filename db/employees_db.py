from sqlalchemy import Column, Integer, String, ForeignKey
from db.db_connection import Base, engine


class EmployeeInDB(Base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True,
                        autoincrement=True, unique=True)
    employee_name = Column(String)
    employee_position_id = Column(Integer, ForeignKey("positions.position_id"))
    employee_address = Column(String)
    employee_phone = Column(String)
    employee_email = Column(String)
    employee_status = Column(String)


Base.metadata.create_all(bind=engine)
