from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import asyncio
from app.models import tournament
from app.db import Base
from app.config import settings

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

config.set_main_option("sqlalchemy.url", settings.database_url.replace('+asyncpg', ''))

def run_migrations_offline():
    context.configure(url=settings.database_url.replace('+asyncpg', ''), target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()