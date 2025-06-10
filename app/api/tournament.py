from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.tournament import TournamentCreate, PlayerCreate, TournamentOut, PlayerOut
from app.services import tournament as service
from app.db import get_session

router = APIRouter(prefix="/tournaments")

@router.post("", response_model=TournamentOut)
async def create(data: TournamentCreate, session: AsyncSession = Depends(get_session())):
    tournament = await service.create_tournament(session, data)
    return await service.tournament_with_players_count(session, tournament)

@router.post("/{tournament_id}/register", response_model=PlayerOut)
async def register(tournament_id: int, data: PlayerCreate, session: AsyncSession = Depends(get_session())):
    player, error = await service.register_player(session, tournament_id, data)
    if error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return player

@router.get("/{tournament_id}/players", response_model=list[PlayerOut])
async def list_players(tournament_id: int, session: AsyncSession = Depends(get_session())):
    return await service.list_players(session, tournament_id)