from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.discounts_db import DiscountInDB
from models.discount_models import DiscountIn, DiscountOut

router = APIRouter()


@router.get("/discount/{discount_id}", response_model=DiscountOut)
async def get_discount(discount_id: int, db: Session = Depends(get_db)):
    discount_in_db = db.query(DiscountInDB).get(discount_id)
    if discount_in_db == None:
        raise HTTPException(
            status_code=404, detail="El descuento solicitado no existe.")
    return discount_in_db


@router.post("/discount/create/")
async def new_discount(discount_in: DiscountIn, db: Session = Depends(get_db)):

    discount_in_db = DiscountInDB(
        **discount_in.dict())

    db.add(discount_in_db)
    db.commit()
    db.refresh(discount_in_db)

    return {"Mensaje": "El descuento fue creado correctamente."}
