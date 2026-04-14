from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.item_pedido import ItemPedidoCreate, ItemPedidoUpdate, ItemPedidoResponse
from app.services.item_pedido import item_pedido_service

router = APIRouter(
    prefix="/itens-pedidos",
    tags=["Itens dos Pedidos"]
)

@router.get("/", response_model=List[ItemPedidoResponse])
def get_itens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return item_pedido_service.listar_itens(db, skip, limit)

@router.get("/{id_pedido}/{id_item}", response_model=ItemPedidoResponse)
def get_item(id_pedido: str, id_item: int, db: Session = Depends(get_db)):
    return item_pedido_service.buscar_item(db, id_pedido, id_item)

@router.post("/", response_model=ItemPedidoResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemPedidoCreate, db: Session = Depends(get_db)):
    return item_pedido_service.criar_item(db, item)

@router.patch("/{id_pedido}/{id_item}", response_model=ItemPedidoResponse)
def update_item(id_pedido: str, id_item: int, item_atualizado: ItemPedidoUpdate, db: Session = Depends(get_db)):
    return item_pedido_service.atualizar_item(db, id_pedido, id_item, item_atualizado)

@router.delete("/{id_pedido}/{id_item}", status_code=status.HTTP_200_OK)
def delete_item(id_pedido: str, id_item: int, db: Session = Depends(get_db)):
    item_pedido_service.remover_item(db, id_pedido, id_item)
    return {"mensagem": "Item do pedido removido com sucesso"}