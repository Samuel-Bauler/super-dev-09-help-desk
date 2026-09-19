from sqlalchemy.orm import Session

from app.core.enums import Papel, StatusChamado
from app.core.exceptions import PermissaoNegadaError, RegraNegocioError
from app.models.ticket import Ticket
from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket_schema import TicketCriar
from app.services.usuario_service import UsuarioService


class TicketService:
    def __init__(self, db: Session):
        self.db = db
        self.ticket_repository = TicketRepository(db)
        self.usuario_service = UsuarioService(db)

    def criar(self, dado: TicketCriar) -> Ticket:
        # Validar que o usuário existe efetivamente
        usuario = self.usuario_service.obter_por_id(dado.id_usuario)
        if usuario.papel != Papel.SOLICITANTE:
            raise PermissaoNegadaError("Tickets podem ser abertos somente por SOLICITANTE")

        ticket = Ticket(
            titulo=dado.titulo,
            descricao=dado.descricao,
            setor=dado.setor,
            solicitante_id=dado.id_usuario,
            status=StatusChamado.ABERTO,
            numero_protocolo="20260918-00001"
        )
        self.ticket_repository.adicionar(ticket)
        self.db.commit()
        return ticket
