from app.repositories import tournament as repo
from app.schemas.tournament import TournamentCreate, PlayerCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_tournament(session: AsyncSession, data: TournamentCreate):
    return await repo.create_tournament(session, data)

async def register_player(session: AsyncSession, tournament_id: int, data: PlayerCreate):
    return await repo.register_player(session, tournament_id, data)

async def list_players(session: AsyncSession, tournament_id: int):
    return await repo.get_players(session, tournament_id)

async def tournament_with_players_count(session: AsyncSession, tournament):
    return await repo.get_tournament_with_count(session, tournament)