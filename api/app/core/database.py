from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings


# engine: pool de conexões
engine = create_engine(settings.database_url, pool_pre_ping=True)

# SessionLocal é a fábrica de sessões (uma por requisição)
SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, 
    autocommit=False, 
    expire_on_commit=False
)


# Base é a classe mãe de todos os models SQLAlchemy
class Base(DeclarativeBase):
    pass
