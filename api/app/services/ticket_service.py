from sqlalchemy.orm import Session

from app.core.enums import Papel, StatusChamado
from app.core.exceptions import NaoEncontradoError, PermissaoNegadaError, RegraNegocioError
from app.core.tempo import agora
from app.models.ticket import Ticket
from app.repositories.ticket_repository import TicketRepository
from app.schemas.ticket_schema import TicketCriar, TicketDefinirPrioridade
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
    
    def obter_por_id(self, id: int) -> Ticket:
        ticket = self.ticket_repository.obter_por_id(id)
        if ticket is None:
            raise NaoEncontradoError("Ticket não encontrado")
        return ticket

    def definir_prioridade(self, id: int, dado: TicketDefinirPrioridade) -> Ticket:
        # buscar o ticket do banco de dados, validando q o mesmo existe
        ticket = self.obter_por_id(id)

        # buscar o usuario do banco de dados, validando que o mesmo existe
        usuario = self.usuario_service.obter_por_id(dado.id_usuario)

        # verificar que o usuario tem o papel de atendente, pois o ticket pode ser
        # resolvido somente por um ATENDENTE
        if usuario.papel != Papel.ATENDENTE:
            raise PermissaoNegadaError("Ticket pode ser definido prioridade somente por ATENDENTE")

        ticket.prioridade = dado.prioridade
        # definir quem será o atendente do chamado
        ticket.atendente_id = dado.id_usuario
        ticket.data_atualizacao = agora()
        # Salvar as modificações do ticket
        self.db.commit()
        return ticket

