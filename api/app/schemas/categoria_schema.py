

from pydantic import BaseModel, Field, ConfigDict


class CategoriaCriar(BaseModel):
    nome: str = Field(min_length=2, max_length=60, description="Nome unico da categoria")
    descricao: str | None = Field(default=None,max_length=255, description="Descrição opcional")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nome": "Rede",
                "descricao": "Problemas de conexão, Wi-Fi, VPN e cabeamento"
            }
        }
    )


class CategoriaEditar(BaseModel):
    nome: str = Field(min_length=2, max_length=60, description="Nome unico da categoria")
    descricao: str | None = Field(default=None,max_length=255, description="Descrição opcional")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nome": "Rede",
                "descricao": "Problemas de conexão, Wi-Fi, VPN e cabeamento"
            }
        }
    )


class CategoriaResposta(BaseModel):
    id: int
    nome: str
    descricao: str | None

    model_config = ConfigDict(from_attributes=True)