from pydantic import BaseModel

class PositionIn(BaseModel):
    position_title : str

class PositionOut(BaseModel):
    position_id : int
    position_title : str

    class Config:
        orm_mode = True