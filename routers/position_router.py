from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.positions_db import PositionInDB
from db.employees_db import EmployeeInDB

from models.position_models import PositionIn, PositionOut
from models.employee_models import EmployeeIn, EmployeeOut

router = APIRouter()


@router.get("/position/{position_id}", response_model=PositionOut)
async def get_position(position_id: int, db: Session = Depends(get_db)):
    position_in_db = db.query(PositionInDB).get(position_id)
    if position_in_db == None:
        raise HTTPException(status_code=404, detail="El cargo solicitado no existe.")
    return position_in_db


@router.post("/position/create/")
async def new_position(position_in: PositionIn, db: Session = Depends(get_db)):

    position_in_db = PositionInDB(**position_in.dict())

    db.add(position_in_db)
    db.commit()
    db.refresh(position_in_db)

    return {"Mensaje": "El cargo fue creado correctamente"}
