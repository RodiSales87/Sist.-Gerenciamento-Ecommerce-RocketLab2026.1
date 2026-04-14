from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.imagem_categoria import CategoriaImagemResponse, CategoriaImagemCreate, CategoriaImagemUpdate
from app.services.imagem_categoria import categoria_imagem_service

router = APIRouter(prefix="/categorias-imagens", tags=["Categorias de Imagens"])

@router.get("/", response_model=List[CategoriaImagemResponse])
def listar_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return categoria_imagem_service.listar_categorias(db, skip=skip, limit=limit)

@router.get("/{categoria_produto}", response_model=CategoriaImagemResponse)
def buscar_categoria(categoria_produto: str, db: Session = Depends(get_db)):
    return categoria_imagem_service.buscar_categoria(db, categoria_produto)

@router.post("/", response_model=CategoriaImagemResponse, status_code=status.HTTP_201_CREATED)
def criar_categoria(categoria: CategoriaImagemCreate, db: Session = Depends(get_db)):
    return categoria_imagem_service.criar_categoria(db, categoria)

@router.patch("/{categoria_produto}", response_model=CategoriaImagemResponse)
def atualizar_categoria(categoria_produto: str, categoria: CategoriaImagemUpdate, db: Session = Depends(get_db)):
    return categoria_imagem_service.atualizar_categoria(db, categoria_produto, categoria)

@router.delete("/{categoria_produto}", status_code=status.HTTP_200_OK)
def remover_categoria(categoria_produto: str, db: Session = Depends(get_db)):
    categoria_imagem_service.remover_categoria(db, categoria_produto)
    return {"mensagem": "Categoria de imagem removida com sucesso"}
