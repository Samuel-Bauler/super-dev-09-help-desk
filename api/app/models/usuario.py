from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum, String

from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column

from app.core.enums import Papel
from app.core.tempo import agora


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(160), nullable=False, unique=True, index=True)
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    papel: Mapped[Papel] = mapped_column(Enum(Papel, native_enum=False, length=20), nullable=False,)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=agora, nullable=False)