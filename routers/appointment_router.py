from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db
from db.customers_db import CustomerInDB
from db.appointments_db import AppointmentInDB

from models.customer_models import CustomerIn, CustomerOut
from models.appointment_models import AppointmentIn, AppointmentOut

router = APIRouter()


@router.get("/appointment/{appointment_id}", response_model=AppointmentOut)
async def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment_in_db = db.query(AppointmentInDB).get(appointment_id)
    if appointment_in_db == None:
        raise HTTPException(status_code=404, detail="La cita no existe")
    return appointment_in_db


@router.post("/appointment/create/")
async def new_appointment(appointment_in: AppointmentIn, db: Session = Depends(get_db)):

    appointment_in_db = AppointmentInDB(**appointment_in.dict())

    db.add(appointment_in_db)
    db.commit()
    db.refresh(appointment_in_db)

    return {"Mensaje": "La cita fue creada correctamente"}
