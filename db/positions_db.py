from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine


class PositionInDB(Base):
     __tablename__ = "positions"
     position_id = Column(Integer, primary_key=True,
                          autoincrement=True, unique=True)
     position_title = Column(String)


Base.metadata.create_all(bind=engine)