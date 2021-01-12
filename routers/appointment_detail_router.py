from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.employees_db import EmployeeInDB
from models.employee_models import EmployeeIn, EmployeeOut
from db.services_db import ServiceInDB
from models.service_models import ServiceIn, ServiceOut
from db.appointments_db import AppointmentInDB
from models.appointment_models import AppointmentIn, AppointmentOut
from db.appointment_details_db import AppointmentDetailInDB
from models.appointment_detail_models import AppointmentDetailIn, AppointmentDetailOut


router = APIRouter()


@router.get("/appointment_detail/{appointment_detail_id}", response_model=AppointmentDetailOut)
async def get_appointment_detail(appointment_detail_id: int, db: Session = Depends(get_db)):
    appointment_detail_in_db = db.query(
        AppointmentDetailInDB).get(appointment_detail_id)
    if appointment_detail_in_db == None:
        raise HTTPException(
            status_code=404, detail="El detalle de cita solicitado no existe.")
    return appointment_detail_in_db


@router.post("/appointment_detail/create/")
async def new_appointment_detail(appointment_detail_in: AppointmentDetailIn, db: Session = Depends(get_db)):

    appointment_detail_in_db = AppointmentDetailInDB(
        **appointment_detail_in.dict())

    db.add(appointment_detail_in_db)
    db.commit()
    db.refresh(appointment_detail_in_db)

    return {"Mensaje": "El detalle de cita fue creado correctamente."}
