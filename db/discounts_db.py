from sqlalchemy import Column, Integer, String, Float
from db.db_connection import Base, engine


class DiscountInDB(Base):
    __tablename__ = "discounts"
    discount_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    discount_name = Column(String)
    discount_value = Column(Integer)


Base.metadata.create_all(bind=engine)
