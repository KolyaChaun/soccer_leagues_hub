from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import schema_players
from src.crud import api_players
from src.database import SessionLocal

router = APIRouter(prefix="/players", tags=["Players"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schema_players.PlayerResponse)
def create_player(player: schema_players.PlayerCreate, db: Session = Depends(get_db)):
    return api_players.create_player(db, player)


@router.get("/", response_model=list[schema_players.PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    return api_players.get_players(db)


@router.get("/{player_id}", response_model=schema_players.PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = api_players.get_player(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.put("/{player_id}", response_model=schema_players.PlayerResponse)
def update_player(
    player_id: int,
    player_data: schema_players.PlayerCreate,
    db: Session = Depends(get_db),
):
    player = api_players.update_player(db, player_id, player_data)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.delete("/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    success = api_players.delete_player(db, player_id)
    if not success:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"message": "Player removed"}
