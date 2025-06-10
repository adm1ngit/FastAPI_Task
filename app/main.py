from fastapi import FastAPI
from app.api import tournament

app = FastAPI()
app.include_router(tournament.router)