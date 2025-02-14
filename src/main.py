from fastapi import FastAPI
from src.routers import players, teams

app = FastAPI()

app.include_router(players.router)
app.include_router(teams.router)


@app.get("/")
def root():
    return {"message": "Soccer Leagues Hub API is running!"}
