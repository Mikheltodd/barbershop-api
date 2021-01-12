from pydantic import BaseModel
from datetime import datetime


class ServiceOrderIn(BaseModel):
    service_order_datetime: datetime


class ServiceOrderOut(BaseModel):
    service_order_id: int
    service_order_datetime: datetime

    class Config:
        orm_mode = True
