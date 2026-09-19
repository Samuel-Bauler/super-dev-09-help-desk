from fastapi.routing import APIRouter

from app.dependencies.database import DbSession
from app.schemas.ticket_schema import TicketCriar, TicketDefinirPrioridade, TicketResposta
from app.services.ticket_service import TicketService


router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("", response_model=TicketResposta)
def criar(dado: TicketCriar, db: DbSession):
    return TicketService(db).criar(dado)


@router.post(
    "/{id}/definir-prioridade", response_model=TicketResposta
)
def definir_prioridade(id: int, dado: TicketDefinirPrioridade, db: DbSession):
    return TicketService(db).definir_prioridade(id, dado)