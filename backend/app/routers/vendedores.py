from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.vendedor import VendedorCreate, VendedorUpdate, VendedorResponse
from app.services.vendedor import vendedor_service

router = APIRouter(
    prefix="/vendedores",
    tags=["Vendedores"]
)

@router.get("/", response_model=List[VendedorResponse])
def get_vendedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return vendedor_service.listar_vendedores(db, skip, limit)

@router.get("/{id_vendedor}", response_model=VendedorResponse)
def get_vendedor(id_vendedor: str, db: Session = Depends(get_db)):
    return vendedor_service.buscar_vendedor(db, id_vendedor)

@router.post("/", response_model=VendedorResponse, status_code=status.HTTP_201_CREATED)
def create_vendedor(vendedor: VendedorCreate, db: Session = Depends(get_db)):
    return vendedor_service.criar_vendedor(db, vendedor)

@router.patch("/{id_vendedor}", response_model=VendedorResponse)
def update_vendedor(id_vendedor: str, vendedor_atualizado: VendedorUpdate, db: Session = Depends(get_db)):
    return vendedor_service.atualizar_vendedor(db, id_vendedor, vendedor_atualizado)

@router.delete("/{id_vendedor}", status_code=status.HTTP_200_OK)
def delete_vendedor(id_vendedor: str, db: Session = Depends(get_db)):
    vendedor_service.remover_vendedor(db, id_vendedor)
    return {"mensagem": "Vendedor removido com sucesso"}