from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db
from db.customers_db import CustomerInDB
# from db.appointments_db import AppointmentInDB

from models.customer_models import CustomerIn, CustomerOut
# from models.appointment_models import AppointmentIn, AppointmentOut

router = APIRouter()


@router.get("/customer/{customer_id}", response_model=CustomerOut)
async def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer_in_db = db.query(CustomerInDB).get(customer_id)
    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    return customer_in_db


@router.post("/customer/register/")
async def new_customer(customer_in: CustomerIn, db: Session = Depends(get_db)):

    customer_in_db = CustomerInDB(**customer_in.dict())

    db.add(customer_in_db)
    db.commit()
    db.refresh(customer_in_db)

    return {"Mensaje": "El cliente fue creado correctamente"}
