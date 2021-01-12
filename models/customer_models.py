from pydantic import BaseModel


class CustomerIn(BaseModel):
    customer_name: str
    customer_status: str
    customer_address: str
    customer_phone: str
    customer_email: str
    customer_birthday: str
    customer_gender: str
    customer_occupation: str


class CustomerOut(BaseModel):
    customer_id: int
    customer_name: str
    customer_status: str
    customer_address: str
    customer_phone: str
    customer_email: str
    customer_birthday: str
    customer_gender: str
    customer_occupation: str

    class Config:
        orm_mode = True
