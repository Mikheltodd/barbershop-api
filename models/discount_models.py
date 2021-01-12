from pydantic import BaseModel


class DiscountIn(BaseModel):
    discount_name: str
    discount_value: int


class DiscountOut(BaseModel):
    discount_id: int
    discount_name: str
    discount_value: int

    class Config:
        orm_mode = True
