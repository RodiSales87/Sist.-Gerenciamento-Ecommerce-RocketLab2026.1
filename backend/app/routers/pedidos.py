from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.pedido import PedidoCreate, PedidoUpdate, PedidoResponse
from app.services.pedido import pedido_service

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.get("/", response_model=List[PedidoResponse])
def get_pedidos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return pedido_service.listar_pedidos(db, skip, limit)

@router.get("/{id_pedido}", response_model=PedidoResponse)
def get_pedido(id_pedido: str, db: Session = Depends(get_db)):
    return pedido_service.buscar_pedido(db, id_pedido)

@router.post("/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def create_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return pedido_service.criar_pedido(db, pedido)

@router.patch("/{id_pedido}", response_model=PedidoResponse)
def update_pedido(id_pedido: str, pedido_atualizado: PedidoUpdate, db: Session = Depends(get_db)):
    return pedido_service.atualizar_pedido(db, id_pedido, pedido_atualizado)

@router.delete("/{id_pedido}", status_code=status.HTTP_200_OK)
def delete_pedido(id_pedido: str, db: Session = Depends(get_db)):
    pedido_service.remover_pedido(db, id_pedido)
    return {"mensagem": "Pedido removido com sucesso"}
