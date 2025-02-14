from datetime import date

from pydantic import BaseModel


class PlayerCreate(BaseModel):
    name: str
    surname: str
    photo_url: str | None = None
    date_of_birth: date
    team_id: int


class PlayerResponse(PlayerCreate):
    id: int

    class Config:
        from_attributes = True
