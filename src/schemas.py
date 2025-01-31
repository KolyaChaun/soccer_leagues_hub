from pydantic import BaseModel
from typing import Optional


class PlayerCreate(BaseModel):
    name: str
    surname: str
    age: int
    club: Optional[str] = None


class PlayerResponse(PlayerCreate):
    id: int

    class Config:
        from_attributes = True
