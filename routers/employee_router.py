from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.employees_db import EmployeeInDB
from db.positions_db import PositionInDB

from models.employee_models import EmployeeIn, EmployeeOut
from models.position_models import PositionIn, PositionOut

router = APIRouter()


@router.get("/employee/{employee_id}", response_model=EmployeeOut)
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee_in_db = db.query(EmployeeInDB).get(employee_id)
    if employee_in_db == None:
        raise HTTPException(
            status_code=404, detail="El empleado solicitado no existe")
    return employee_in_db


@router.post("/employee/register/")
async def new_employee(employee_in: EmployeeIn, db: Session = Depends(get_db)):

    employee_in_db = EmployeeInDB(**employee_in.dict())

    db.add(employee_in_db)
    db.commit()
    db.refresh(employee_in_db)

    return {"Mensaje": "El empleado fue creado correctamente"}