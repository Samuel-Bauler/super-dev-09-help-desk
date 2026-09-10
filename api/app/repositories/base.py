from typing import Generic, TypeVar
from sqlalchemy.orm import Session

from sqlalchemy import select

from app.core.database import Base


T = TypeVar("T", bound=Base)


class RepositorioBase(Generic[T]):
    def __init__(self, db: Session, model: type[T]):
        self.db = db
        self.model = model

    def adicionar(self, objeto: T) -> T:
        """Adicionar à sessão e faz flush para o dado gerar o id(sem fazer commit)"""
        self.db.add(object)
        self.db.flush()
        self.db.refresh(object)
        return objeto

    def obter_por_id(self, id: int) -> T | None:
        return self.db.get(self.model, id)

    def remover(self, objeto: T) -> None:
        self.db.delete(objeto)
        self.db.flush()

    def listar_todos(self) -> list[T]:
        return list(self.db.scalars(select(self.model)).unique().all())