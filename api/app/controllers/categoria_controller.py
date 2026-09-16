from fastapi.routing import APIRouter

from app.schemas.categoria_schema import CategoriaResposta, CategoriaCriar, CategoriaEditar 
from app.services.categoria_service import CategoriaService
from app.dependencies.database import DbSession


router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get(
    "",
    summary="Lista de categorias",
    response_model=list[CategoriaResposta]
)
def listar(db: DbSession):
    return CategoriaService(db).listar()

@router.get(
    "/{id}",
    summary="Obtem uma categoria pelo id",
    response_model=CategoriaResposta
)
def consultar_por_id(id: int, db: DbSession):
    return CategoriaService(db).obter_por_id(id)


@router.post(
    "",
    summary="Cadastrar uma categoria",
    response_model=CategoriaResposta
)
def criar(dado: CategoriaCriar, db: DbSession):
    return CategoriaService(db).criar(dado)


@router.put(
    "/{id}",
    summary="Editar uma categoria por id",
    response_model=CategoriaResposta
)
def editar(id: int, dado: CategoriaEditar, db: DbSession):
    return CategoriaService(db).editar(id, dado)


@router.delete(
    "/{id}",
    summary="Apagar uma categoria por id"
)
def apagar(id: int, db: DbSession):
    return CategoriaService(db).apagar(id)