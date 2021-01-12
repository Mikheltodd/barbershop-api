from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.services_db import ServiceInDB
from models.service_models import ServiceIn, ServiceOut
from db.categories_db import CategoryInDB
from models.category_models import CategoryIn, CategoryOut


router = APIRouter()


@router.get("/service/{service_id}", response_model=ServiceOut)
async def get_service(service_id: int, db: Session = Depends(get_db)):
    service_in_db = db.query(ServiceInDB).get(service_id)
    if service_in_db == None:
        raise HTTPException(
            status_code=404, detail="El servicio solicitado no existe.")
    return service_in_db


@router.post("/service/create/")
async def new_service(service_in: ServiceIn, db: Session = Depends(get_db)):

    service_in_db = ServiceInDB(**service_in.dict())

    db.add(service_in_db)
    db.commit()
    db.refresh(service_in_db)

    return {"Mensaje": "El servicio fue creado correctamente."}
