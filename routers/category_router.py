from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.categories_db import CategoryInDB
from models.category_models import CategoryIn, CategoryOut


router = APIRouter()


@router.get("/category/{category_id}", response_model=CategoryOut)
async def get_categories(category_id: int, db: Session = Depends(get_db)):
    category_in_db = db.query(CategoryInDB).get(category_id)
    if category_in_db == None:
        raise HTTPException(
            status_code=404, detail="La categoría solicitada no existe.")
    return category_in_db


@router.post("/category/create/")
async def new_category(category_in: CategoryIn, db: Session = Depends(get_db)):

    category_in_db = CategoryInDB(**category_in.dict())

    db.add(category_in_db)
    db.commit()
    db.refresh(category_in_db)

    return {"Mensaje": "La categoría fue creada correctamente."}
