from enum import Enum


class Papel(str, Enum):
    ADMIN = "ADMIN"
    ATENDENTE = "ATENDENTE"
    SOLICITANTE = "SOLICITANTE"

