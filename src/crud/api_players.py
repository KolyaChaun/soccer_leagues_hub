from sqlalchemy.orm import Session
from src.schemas import schema_players
from src.models import model_players


def create_player(db: Session, player: schema_players.PlayerCreate):
    db_player = model_players.Player(**player.model_dump())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_players(db: Session):
    return db.query(model_players.Player).all()


def get_player(db: Session, player_id: int):
    return (
        db.query(model_players.Player)
        .filter(model_players.Player.id == player_id)
        .first()
    )


def update_player(
    db: Session, player_id: int, player_data: schema_players.PlayerCreate
):
    player = (
        db.query(model_players.Player)
        .filter(model_players.Player.id == player_id)
        .first()
    )
    if not player:
        return None

    for key, value in player_data.dict().items():
        setattr(player, key, value)

    db.commit()
    db.refresh(player)
    return player


def delete_player(db: Session, player_id: int):
    player = (
        db.query(model_players.Player)
        .filter(model_players.Player.id == player_id)
        .first()
    )
    if not player:
        return False

    db.delete(player)
    db.commit()
    return True
