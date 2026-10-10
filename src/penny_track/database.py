import os

from sqlalchemy import create_engine

from penny_track.config.settings import settings


database_url = settings.database_url
if not database_url:
    raise RuntimeError(
        "DATABASE_URL is not configured. "
        "Set it to a PostgreSQL URL such as "
        "'postgresql+psycopg://postgres:password@localhost:5432/penny_track'."
    )

engine = create_engine(database_url, pool_pre_ping=True, echo=True)