from fastapi import FastAPI
from src.players import models
from src.database import engine
from src.routers import players, teams

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(players.router)
app.include_router(teams.router)


@app.get("/")
def root():
    return {"message": "Soccer Leagues Hub API is running!"}
