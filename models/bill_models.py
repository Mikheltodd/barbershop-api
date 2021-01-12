from pydantic import BaseModel
from datetime import datetime


class BillIn(BaseModel):
    bill_datetime: datetime
    bill_total: float
    bill_discount: float
    bill_discount_id: int
    bill_customer_id: int
    bill_service_order_id: int


class BillOut(BaseModel):
    bill_id: int
    bill_datetime: datetime
    bill_total: float
    bill_discount: float
    bill_discount_id: int
    bill_customer_id: int
    bill_service_order_id: int

    class Config:
        orm_mode = True
