from sqlalchemy.orm import Session
from src.schemas import schema_teams
from src.models import model_teams


def create_team(db: Session, team: schema_teams.TeamCreate):
    db_team = model_teams.Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def get_teams(db: Session):
    return db.query(model_teams.Team).all()


def get_team(db: Session, team_id: int):
    return db.query(model_teams.Team).filter(model_teams.Team.id == team_id).first()


def update_team(db: Session, team_id: int, team_data: schema_teams.TeamCreate):
    team = db.query(model_teams.Team).filter(model_teams.Team.id == team_id).first()
    if not team:
        return None

    for key, value in team_data.dict().items():
        setattr(team, key, value)

    db.commit()
    db.refresh(team)
    return team


def delete_team(db: Session, team_id: int):
    team = db.query(model_teams.Team).filter(model_teams.Team.id == team_id).first()
    if not team:
        return False

    db.delete(team)
    db.commit()
    return True
