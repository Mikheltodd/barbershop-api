from pydantic import BaseModel


class ServiceIn(BaseModel):
    service_category_id: int
    service_name: str
    service_description: str
    service_price: float
    service_duration: int


class ServiceOut(BaseModel):
    service_id: int
    service_category_id: int
    service_name: str
    service_description: str
    service_price: float
    service_duration: int

    class Config:
        orm_mode = True
