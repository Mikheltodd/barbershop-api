from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine


class CategoryInDB(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String)
    category_description = Column(String)


Base.metadata.create_all(bind=engine)
