import sys
from pathlib import Path

# add /app to PYTHONPATH so "import app" works
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool
import os

from app.db.base import Base
from app import models  # noqa

config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

#fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
