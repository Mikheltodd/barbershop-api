# Paquetes Necesarios
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creación del Motor
db_url = "postgres://aahujhmcxynilb:1e3556f725e46ab9ed0bca3489009cd92acf4af5231dcda1566068ac2f05b1a5@ec2-75-101-212-64.compute-1.amazonaws.com:5432/da305b94k93938"
engine = create_engine(db_url)

# Creación de Sesión y Dependencias
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Base para las Entidades de Datos
Base = declarative_base()
Base.metadata.schema = "barbershop"
