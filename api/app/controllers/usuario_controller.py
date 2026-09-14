from fastapi import APIRouter, Depends

from app.core.database import SessionLocal
from app.schemas.usuario_schema import UsuarioCriar
from app.services.usuario_service import UsuarioService


router = APIRouter(prefix="/usuarios", tags=["Usuários"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def criar(dado: UsuarioCriar, db=Depends(get_db)):
    return UsuarioService(db).criar(dado)