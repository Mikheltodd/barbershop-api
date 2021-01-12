from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.customers_db import CustomerInDB
from db.bills_db import BillInDB
from db.discounts_db import DiscountInDB
from db.service_orders_db import ServiceOrderInDB
from models.customer_models import CustomerIn, CustomerOut
from models.bill_models import BillIn, BillOut
from models.discount_models import DiscountIn, DiscountOut
from models.service_order_models import ServiceOrderIn, ServiceOrderOut

router = APIRouter()


@router.get("/bill/{bill_id}", response_model=BillOut)
async def get_bill(bill_id: int, db: Session = Depends(get_db)):
    bill_in_db = db.query(
        BillInDB).get(bill_id)
    if bill_in_db == None:
        raise HTTPException(
            status_code=404, detail="La factura solicitada no existe.")
    return bill_in_db


@router.post("/bill/create/")
async def new_bill(bill_in: BillIn, db: Session = Depends(get_db)):

    bill_in_db = BillInDB(
        **bill_in.dict())

    db.add(bill_in_db)
    db.commit()
    db.refresh(bill_in_db)

    return {"Mensaje": "La factura fue creada correctamente."}
