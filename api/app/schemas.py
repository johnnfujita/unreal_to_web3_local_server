from typing import Optional

from pydantic import BaseModel


class NFTEntry(BaseModel):
    token_id: int
    owner_account: str
    read_available: bool
    car_model: str

    class Config:
        orm_mode = True