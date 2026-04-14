from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.pedido import PedidoCreate, PedidoUpdate
from app.repositories.pedido import pedido_repository

class PedidoService:
    def listar_pedidos(self, db: Session, skip: int = 0, limit: int = 100):
        return pedido_repository.get_all(db, skip=skip, limit=limit)

    def buscar_pedido(self, db: Session, id_pedido: str):
        pedido = pedido_repository.get_by_id(db, id_pedido)
        if not pedido:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Pedido não encontrado"
            )
        return pedido

    def criar_pedido(self, db: Session, pedido_create: PedidoCreate):
        pedido_existente = pedido_repository.get_by_id(db, pedido_create.id_pedido)
        if pedido_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Este id_pedido já está registrado"
            )
        return pedido_repository.create(db, pedido_create.model_dump())

    def atualizar_pedido(self, db: Session, id_pedido: str, pedido_update: PedidoUpdate):
        db_pedido = self.buscar_pedido(db, id_pedido)
        update_data = pedido_update.model_dump(exclude_unset=True)
        return pedido_repository.update(db, db_obj=db_pedido, obj_in=update_data)

    def remover_pedido(self, db: Session, id_pedido: str):
        db_pedido = self.buscar_pedido(db, id_pedido)
        pedido_repository.delete(db, db_obj=db_pedido)

pedido_service = PedidoService()
