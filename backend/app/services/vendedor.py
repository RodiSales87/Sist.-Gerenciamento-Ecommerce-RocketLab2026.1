from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.vendedor import VendedorCreate, VendedorUpdate
from app.repositories.vendedor import vendedor_repository

class VendedorService:
    def listar_vendedores(self, db: Session, skip: int = 0, limit: int = 100):
        return vendedor_repository.get_all(db, skip=skip, limit=limit)

    def buscar_vendedor(self, db: Session, id_vendedor: str):
        vendedor = vendedor_repository.get_by_id(db, id_vendedor)
        if not vendedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Vendedor não encontrado"
            )
        return vendedor

    def criar_vendedor(self, db: Session, vendedor_create: VendedorCreate):
        vendedor_existente = vendedor_repository.get_by_id(db, vendedor_create.id_vendedor)
        if vendedor_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Este id_vendedor já está registrado"
            )
        return vendedor_repository.create(db, vendedor_create.model_dump())

    def atualizar_vendedor(self, db: Session, id_vendedor: str, vendedor_update: VendedorUpdate):
        db_vendedor = self.buscar_vendedor(db, id_vendedor)
        update_data = vendedor_update.model_dump(exclude_unset=True)
        return vendedor_repository.update(db, db_obj=db_vendedor, obj_in=update_data)

    def remover_vendedor(self, db: Session, id_vendedor: str):
        db_vendedor = self.buscar_vendedor(db, id_vendedor)
        vendedor_repository.delete(db, db_obj=db_vendedor)

vendedor_service = VendedorService()