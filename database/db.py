import urllib

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import settings

connection_string = (
    f"DRIVER={{{settings.DB_DRIVER}}};"
    f"SERVER={settings.DB_SERVER};"
    f"DATABASE={settings.DB_DATABASE};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

params = urllib.parse.quote_plus(connection_string)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}",
    echo=False,
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()