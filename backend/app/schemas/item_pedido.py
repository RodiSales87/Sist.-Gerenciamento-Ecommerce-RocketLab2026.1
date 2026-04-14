from typing import Optional
from pydantic import BaseModel

class ItemPedidoBase(BaseModel):
    id_produto: str
    id_vendedor: str
    preco_BRL: float
    preco_frete: float

class ItemPedidoCreate(ItemPedidoBase):
    id_pedido: str
    id_item: int

class ItemPedidoUpdate(BaseModel):
    id_produto: Optional[str] = None
    id_vendedor: Optional[str] = None
    preco_BRL: Optional[float] = None
    preco_frete: Optional[float] = None

class ItemPedidoResponse(ItemPedidoBase):
    id_pedido: str
    id_item: int

    class Config:
        from_attributes = True