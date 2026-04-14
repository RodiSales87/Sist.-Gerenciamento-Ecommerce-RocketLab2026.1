from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class AvaliacaoPedidoBase(BaseModel):
    id_pedido: str
    avaliacao: int
    titulo_comentario: Optional[str] = None
    comentario: Optional[str] = None
    data_comentario: Optional[datetime] = None
    data_resposta: Optional[datetime] = None

class AvaliacaoPedidoCreate(AvaliacaoPedidoBase):
    id_avaliacao: str

class AvaliacaoPedidoUpdate(BaseModel):
    id_pedido: Optional[str] = None
    avaliacao: Optional[int] = None
    titulo_comentario: Optional[str] = None
    comentario: Optional[str] = None
    data_comentario: Optional[datetime] = None
    data_resposta: Optional[datetime] = None

class AvaliacaoPedidoResponse(AvaliacaoPedidoBase):
    id_avaliacao: str

    class Config:
        from_attributes = True
