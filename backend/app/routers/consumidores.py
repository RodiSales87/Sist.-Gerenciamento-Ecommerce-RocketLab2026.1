from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.consumidor import ConsumidorCreate, ConsumidorUpdate, ConsumidorResponse
from app.services.consumidor import consumidor_service

router = APIRouter(
    prefix="/consumidores",
    tags=["Consumidores"]
)

@router.get("/", response_model=List[ConsumidorResponse])
def get_consumidores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return consumidor_service.listar_consumidores(db, skip, limit)

@router.get("/{id_consumidor}", response_model=ConsumidorResponse)
def get_consumidor(id_consumidor: str, db: Session = Depends(get_db)):
    return consumidor_service.buscar_consumidor(db, id_consumidor)

@router.post("/", response_model=ConsumidorResponse, status_code=status.HTTP_201_CREATED)
def create_consumidor(consumidor: ConsumidorCreate, db: Session = Depends(get_db)):
    return consumidor_service.criar_consumidor(db, consumidor)

@router.patch("/{id_consumidor}", response_model=ConsumidorResponse)
def update_consumidor(id_consumidor: str, consumidor_atualizado: ConsumidorUpdate, db: Session = Depends(get_db)):
    return consumidor_service.atualizar_consumidor(db, id_consumidor, consumidor_atualizado)

@router.delete("/{id_consumidor}", status_code=status.HTTP_200_OK)
def delete_consumidor(id_consumidor: str, db: Session = Depends(get_db)):
    consumidor_service.remover_consumidor(db, id_consumidor)
    return {"mensagem": "Consumidor removido com sucesso"}