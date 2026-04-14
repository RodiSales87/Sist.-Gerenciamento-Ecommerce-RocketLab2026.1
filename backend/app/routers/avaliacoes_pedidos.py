from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.avaliacao_pedido import AvaliacaoPedidoResponse, AvaliacaoPedidoCreate, AvaliacaoPedidoUpdate
from app.services.avaliacao_pedido import avaliacao_pedido_service

router = APIRouter(prefix="/avaliacoes-pedidos", tags=["Avaliações de Pedidos"])

@router.get("/", response_model=List[AvaliacaoPedidoResponse])
def listar_avaliacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return avaliacao_pedido_service.listar_avaliacoes(db, skip=skip, limit=limit)

@router.get("/{id_avaliacao}", response_model=AvaliacaoPedidoResponse)
def buscar_avaliacao(id_avaliacao: str, db: Session = Depends(get_db)):
    return avaliacao_pedido_service.buscar_avaliacao(db, id_avaliacao)

@router.post("/", response_model=AvaliacaoPedidoResponse, status_code=status.HTTP_201_CREATED)
def criar_avaliacao(avaliacao: AvaliacaoPedidoCreate, db: Session = Depends(get_db)):
    return avaliacao_pedido_service.criar_avaliacao(db, avaliacao)

@router.patch("/{id_avaliacao}", response_model=AvaliacaoPedidoResponse)
def atualizar_avaliacao(id_avaliacao: str, avaliacao: AvaliacaoPedidoUpdate, db: Session = Depends(get_db)):
    return avaliacao_pedido_service.atualizar_avaliacao(db, id_avaliacao, avaliacao)

@router.delete("/{id_avaliacao}", status_code=status.HTTP_200_OK)
def remover_avaliacao(id_avaliacao: str, db: Session = Depends(get_db)):
    avaliacao_pedido_service.remover_avaliacao(db, id_avaliacao)
    return {"mensagem": "Avaliação removida com sucesso"}
