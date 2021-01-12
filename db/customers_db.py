from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine


class CustomerInDB(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True,
                         autoincrement=True, unique=True)
    customer_name = Column(String)
    customer_status = Column(String)
    customer_address = Column(String)
    customer_phone = Column(String)
    customer_email = Column(String)
    customer_birthday = Column(String)
    customer_gender = Column(String)
    customer_occupation = Column(String)


Base.metadata.create_all(bind=engine)
