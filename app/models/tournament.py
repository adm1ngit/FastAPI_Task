from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base
import datetime

class Tournament(Base):
    __tablename__ = "tournaments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    max_players: Mapped[int] = mapped_column(Integer, nullable=False)
    start_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)

    players: Mapped[list["Player"]] = relationship(back_populates="tournament", cascade="all, delete-orphan")


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"))

    tournament: Mapped["Tournament"] = relationship(back_populates="players")