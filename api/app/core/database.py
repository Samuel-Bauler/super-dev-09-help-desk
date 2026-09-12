from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


engine = create_engine(settings.database_url, pool_pre_ping=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


# Base é a classe mae de todos os models SQLAlchemy
class Base(DeclarativeBase):
    pass

# python -c "import app.models as m; print(sorted(m.Base.metadata.tables))"

# Criar migration
# alembic revision --autogenerate -m "mensagem"

# Aplicar as migrations (criar tabela, modificar tabelas, apagar tabelas)
# alembic upgrade head