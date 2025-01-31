from sqlalchemy.orm import Session
from src import models, schemas


def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_players(db: Session):
    return db.query(models.Player).all()


def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def update_player(db: Session, player_id: int, player_data: schemas.PlayerCreate):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        return None

    for key, value in player_data.dict().items():
        setattr(player, key, value)

    db.commit()
    db.refresh(player)
    return player


def delete_player(db: Session, player_id: int):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        return False

    db.delete(player)
    db.commit()
    return True
