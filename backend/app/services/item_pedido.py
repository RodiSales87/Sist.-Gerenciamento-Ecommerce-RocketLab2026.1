from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.item_pedido import ItemPedidoCreate, ItemPedidoUpdate
from app.repositories.item_pedido import item_pedido_repository

class ItemPedidoService:
    def listar_itens(self, db: Session, skip: int = 0, limit: int = 100):
        return item_pedido_repository.get_all(db, skip=skip, limit=limit)

    def buscar_item(self, db: Session, id_pedido: str, id_item: int):
        item = item_pedido_repository.get_by_id(db, id_pedido, id_item)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Item do pedido não encontrado"
            )
        return item

    def criar_item(self, db: Session, item_create: ItemPedidoCreate):
        item_existente = item_pedido_repository.get_by_id(db, item_create.id_pedido, item_create.id_item)
        if item_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Este item já está registrado para este pedido"
            )
        return item_pedido_repository.create(db, item_create.model_dump())

    def atualizar_item(self, db: Session, id_pedido: str, id_item: int, item_update: ItemPedidoUpdate):
        db_item = self.buscar_item(db, id_pedido, id_item)
        update_data = item_update.model_dump(exclude_unset=True)
        return item_pedido_repository.update(db, db_obj=db_item, obj_in=update_data)

    def remover_item(self, db: Session, id_pedido: str, id_item: int):
        db_item = self.buscar_item(db, id_pedido, id_item)
        item_pedido_repository.delete(db, db_obj=db_item)

item_pedido_service = ItemPedidoService()
