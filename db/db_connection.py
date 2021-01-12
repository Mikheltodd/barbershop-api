# Paquetes Necesarios
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creación del Motor
db_url = "postgresql://postgres:root@localhost:5432/BarberShop"
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
