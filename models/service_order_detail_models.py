from pydantic import BaseModel


class ServiceOrderDetailIn(BaseModel):
    service_order_detail_service_id : int
    service_order_detail_quantity : int
    service_order_detail_amount : int
    service_order_detail_service_order_id : int
    service_order_detail_employee_id : int


class ServiceOrderDetailOut(BaseModel):
    service_order_detail_id : int
    service_order_detail_service_id : int
    service_order_detail_quantity : int
    service_order_detail_amount : int
    service_order_detail_service_order_id : int
    service_order_detail_employee_id : int

    class Config:
        orm_mode = True
