from pydantic import BaseModel


class EmployeeIn(BaseModel):
    employee_name : str
    employee_position_id : str
    employee_address : str
    employee_phone : str
    employee_email : str
    employee_status : str


class EmployeeOut(BaseModel):
    employee_id : int
    employee_name : str
    employee_position_id : str
    employee_address : str
    employee_phone : str
    employee_email : str
    employee_status : str

    class Config:
        orm_mode = True
