from pydantic import BaseModel


class AppointmentIn(BaseModel):
    appointment_date: str
    appointment_time: str
    appointment_status: str
    appointment_customer_id: int


class AppointmentOut(BaseModel):
    appointment_id: int
    appointment_date: str
    appointment_time: str
    appointment_status: str
    appointment_customer_id: int

    class Config:
        orm_mode = True
