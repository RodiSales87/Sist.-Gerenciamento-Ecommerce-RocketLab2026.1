from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.consumidor import ConsumidorCreate, ConsumidorUpdate
from app.repositories.consumidor import consumidor_repository

class ConsumidorService:
    def listar_consumidores(self, db: Session, skip: int = 0, limit: int = 100):
        return consumidor_repository.get_all(db, skip=skip, limit=limit)

    def buscar_consumidor(self, db: Session, id_consumidor: str):
        consumidor = consumidor_repository.get_by_id(db, id_consumidor)
        if not consumidor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Consumidor não encontrado"
            )
        return consumidor

    def criar_consumidor(self, db: Session, consumidor_create: ConsumidorCreate):
        consumidor_existente = consumidor_repository.get_by_id(db, consumidor_create.id_consumidor)
        if consumidor_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Este id_consumidor já está registrado"
            )
        return consumidor_repository.create(db, consumidor_create.model_dump())

    def atualizar_consumidor(self, db: Session, id_consumidor: str, consumidor_update: ConsumidorUpdate):
        db_consumidor = self.buscar_consumidor(db, id_consumidor)
        update_data = consumidor_update.model_dump(exclude_unset=True)
        return consumidor_repository.update(db, db_obj=db_consumidor, obj_in=update_data)

    def remover_consumidor(self, db: Session, id_consumidor: str):
        db_consumidor = self.buscar_consumidor(db, id_consumidor)
        consumidor_repository.delete(db, db_obj=db_consumidor)

consumidor_service = ConsumidorService()