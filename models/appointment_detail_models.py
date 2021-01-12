from pydantic import BaseModel


class AppointmentDetailIn(BaseModel):
    appointment_detail_employee_id: int
    appointment_detail_service_id: int
    appointment_detail_appointment_id: int


class AppointmentDetailOut(BaseModel):
    appointment_detail_id: int
    appointment_detail_employee_id: int
    appointment_detail_service_id: int
    appointment_detail_appointment_id: int

    class Config:
        orm_mode = True
