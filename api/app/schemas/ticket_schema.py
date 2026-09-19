from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from app.core.enums import PrioridadeChamado, SetorChamado, StatusChamado


class TicketCriar(BaseModel):
    id_usuario:int = Field(alias="idUsuario")
    titulo:str = Field(min_length=3, max_length=120)
    descricao:str = Field(min_length=10)
    setor:SetorChamado

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "idUsuario": 1,
                "titulo": "PC com problema",
                "descricao": "Placa de vídeo não tem internet",
                "setor": "ADMINISTRATIVO"
            }
        }
    )



class TicketDefinirPrioridade(BaseModel):
    pass


class TicketAssociar(BaseModel):
    pass


class TicketResolver(BaseModel):
    pass


class TicketCancelar(BaseModel):
    pass


class TicketResposta(BaseModel):
    id: int
    numero_protocolo: str
    titulo: str
    descricao: str
    status: StatusChamado
    prioridade: PrioridadeChamado | None
    setor: SetorChamado
    descricao_solucao: str | None
    motivo_cancelamento: str | None
    data_criacao: datetime
    data_atualizacao: datetime | None
    solicitante_id: int
    atendente_id: int | None
