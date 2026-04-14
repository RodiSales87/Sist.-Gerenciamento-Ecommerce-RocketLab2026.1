from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.produto import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from app.services.produto import produto_service

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.get("/", response_model=List[ProdutoResponse])
def get_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db, skip, limit)

@router.get("/{id_produto}", response_model=ProdutoResponse)
def get_produto(id_produto: str, db: Session = Depends(get_db)):
    return produto_service.buscar_produto(db, id_produto)

@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def create_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return produto_service.criar_produto(db, produto)

@router.patch("/{id_produto}", response_model=ProdutoResponse)
def update_produto(id_produto: str, produto_atualizado: ProdutoUpdate, db: Session = Depends(get_db)):
    return produto_service.atualizar_produto(db, id_produto, produto_atualizado)

@router.delete("/{id_produto}", status_code=status.HTTP_200_OK)
def delete_produto(id_produto: str, db: Session = Depends(get_db)):
    produto_service.remover_produto(db, id_produto)
    return {"mensagem": "Produto removido com sucesso"}
    return {"mensagem": "Produto removido com sucesso"}