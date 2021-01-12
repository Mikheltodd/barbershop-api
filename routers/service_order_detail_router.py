from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.service_order_details_db import ServiceOrderDetailInDB
from db.employees_db import EmployeeInDB
from db.service_orders_db import ServiceOrderInDB
from db.services_db import ServiceInDB

from models.service_order_detail_models import ServiceOrderDetailIn, ServiceOrderDetailOut
from models.employee_models import EmployeeIn, EmployeeOut
from models.service_order_models import ServiceOrderIn, ServiceOrderOut
from models.service_models import ServiceIn, ServiceOut

router = APIRouter()


@router.get("/service_order_detail/{service_order_detail_id}", response_model=ServiceOrderDetailOut)
async def get_detail(service_order_detail_id: int, db: Session = Depends(get_db)):
    service_order_detail_in_db = db.query(ServiceOrderDetailInDB).get(
        service_order_detail_id)
    if service_order_detail_in_db == None:
        raise HTTPException(
            status_code=404, detail="Detalle de orden de servicio no encontrado")
    return service_order_detail_in_db


@router.post("/service_order_detail/create/")
async def new_service_order_detail(order_service_detail_in: ServiceOrderDetailIn, db: Session = Depends(get_db)):

    service_order_detail_in_db = ServiceOrderDetailInDB(
        **order_service_detail_in.dict())

    db.add(service_order_detail_in_db)
    db.commit()
    db.refresh(service_order_detail_in_db)

    return {"Mensaje": "Detalle de orden de servicio creado correctamente."}