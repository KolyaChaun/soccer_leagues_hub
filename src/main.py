from fastapi import FastAPI
from src import models
from src.database import engine
from src.routers import players

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(players.router)


@app.get("/")
def root():
    return {"message": "Soccer Leagues Hub API is running!"}
