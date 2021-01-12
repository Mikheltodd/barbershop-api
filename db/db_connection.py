# Paquetes Necesarios
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creación del Motor
db_url = "postgres://jomlyhfohmirsf:d6b3cca5255c9dbd1fc549cc7ee8183da74ee40818576ea5d315b3d70053587f@ec2-35-168-77-215.compute-1.amazonaws.com:5432/dclfag75opedrp"
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
