from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tournament import Tournament, Player

async def create_tournament(session: AsyncSession, data):
    tournament = Tournament(**data.dict())
    session.add(tournament)
    await session.commit()
    await session.refresh(tournament)
    return tournament

async def register_player(session: AsyncSession, tournament_id: int, data):
    tournament = await session.get(Tournament, tournament_id)
    if not tournament:
        return None, "Tournament not found"

    registered_count = await session.scalar(
        select(func.count()).select_from(Player).where(Player.tournament_id == tournament_id)
    )

    if registered_count >= tournament.max_players:
        return None, "Tournament is full"

    exists = await session.scalar(
        select(Player).where(Player.email == data.email, Player.tournament_id == tournament_id)
    )
    if exists:
        return None, "Player already registered"

    player = Player(**data.dict(), tournament_id=tournament_id)
    session.add(player)
    await session.commit()
    await session.refresh(player)
    return player, None

async def get_players(session: AsyncSession, tournament_id: int):
    result = await session.execute(
        select(Player).where(Player.tournament_id == tournament_id)
    )
    return result.scalars().all()

async def get_tournament_with_count(session: AsyncSession, tournament: Tournament):
    count = await session.scalar(
        select(func.count()).select_from(Player).where(Player.tournament_id == tournament.id)
    )
    return {
        "id": tournament.id,
        "name": tournament.name,
        "max_players": tournament.max_players,
        "start_at": tournament.start_at,
        "registered_players": count
    }
