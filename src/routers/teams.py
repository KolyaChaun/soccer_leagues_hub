from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import schema_teams
from src.crud import api_teams
from src.database import SessionLocal

router = APIRouter(prefix="/teams", tags=["Teams"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schema_teams.TeamResponse)
def create_team(team: schema_teams.TeamCreate, db: Session = Depends(get_db)):
    return api_teams.create_team(db, team)


@router.get("/", response_model=list[schema_teams.TeamResponse])
def get_teams(db: Session = Depends(get_db)):
    return api_teams.get_teams(db)


@router.get("/{team_id}", response_model=schema_teams.TeamResponse)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = api_teams.get_team(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.put("/{team_id}", response_model=schema_teams.TeamResponse)
def update_team(
    team_id: int, team_data: schema_teams.TeamCreate, db: Session = Depends(get_db)
):
    team = api_teams.update_team(db, team_id, team_data)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    success = api_teams.delete_team(db, team_id)
    if not success:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team removed"}
