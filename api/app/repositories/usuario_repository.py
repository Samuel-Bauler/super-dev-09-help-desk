from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.repositories.base import RepositorioBase


class UsuarioRepository(RepositorioBase[Usuario]):
    def __init__(self, db: Session):
        super().__init__(db, Usuario)