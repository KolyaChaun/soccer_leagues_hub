from sqlalchemy.orm import Session
from src.teams import models, schemas


def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def get_teams(db: Session):
    return db.query(models.Team).all()


def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


def update_team(db: Session, team_id: int, team_data: schemas.TeamCreate):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        return None

    for key, value in team_data.dict().items():
        setattr(team, key, value)

    db.commit()
    db.refresh(team)
    return team


def delete_team(db: Session, team_id: int):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        return False

    db.delete(team)
    db.commit()
    return True