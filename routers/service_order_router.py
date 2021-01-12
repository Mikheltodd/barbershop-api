from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.service_orders_db import ServiceOrderInDB
from models.service_order_models import ServiceOrderIn, ServiceOrderOut

router = APIRouter()


@router.get("/service_order/{service_order_id}", response_model=ServiceOrderOut)
async def get_service_order(service_order_id: int, db: Session = Depends(get_db)):
    service_order_in_db = db.query(ServiceOrderInDB).get(service_order_id)
    if service_order_in_db == None:
        raise HTTPException(
            status_code=404, detail="La orden de servicio no existe")
    return service_order_in_db


@router.post("/service_order/create/")
async def new_service_order_detail(order_service_in: ServiceOrderIn, db: Session = Depends(get_db)):

    service_order_in_db = ServiceOrderInDB(
        **order_service_in.dict())

    db.add(service_order_in_db)
    db.commit()
    db.refresh(service_order_in_db)

    return {"Mensaje": "Orden de servicio creada correctamente."}
