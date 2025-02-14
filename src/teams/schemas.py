from pydantic import BaseModel


class TeamCreate(BaseModel):
    team_name: str
    emblem_url: str | None = None
    form_color: str
    avg_age: int | None = None



class TeamResponse(TeamCreate):
    id: int

    class Config:
        from_attributes = True