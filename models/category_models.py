from pydantic import BaseModel


class CategoryIn(BaseModel):
    category_name: str
    category_description: str


class CategoryOut(BaseModel):
    category_id: int
    category_name: str
    category_description: str

    class Config:
        orm_mode = True
