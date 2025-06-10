from pydantic import BaseModel, EmailStr
from datetime import datetime

class TournamentCreate(BaseModel):
    name: str
    max_players: int
    start_at: datetime

class TournamentOut(BaseModel):
    id: int
    name: str
    max_players: int
    start_at: datetime
    registered_players: int

    class Config:
        orm_mode = True

class PlayerCreate(BaseModel):
    name: str
    email: EmailStr

class PlayerOut(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True