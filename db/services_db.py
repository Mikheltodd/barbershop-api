from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db.db_connection import Base, engine


class ServiceInDB(Base):
    __tablename__ = "services"
    service_id = Column(Integer, primary_key=True, autoincrement=True)
    service_category_id = Column(Integer, ForeignKey("categories.category_id"))
    service_name = Column(String)
    service_description = Column(String)
    service_price = Column(Float)
    service_duration = Column(Integer)


Base.metadata.create_all(bind=engine)
