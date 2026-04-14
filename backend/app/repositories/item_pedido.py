from sqlalchemy.orm import Session
from app.models.item_pedido import ItemPedido

class ItemPedidoRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(ItemPedido).offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id_pedido: str, id_item: int):
        return db.query(ItemPedido).filter(
            ItemPedido.id_pedido == id_pedido,
            ItemPedido.id_item == id_item
        ).first()

    def create(self, db: Session, obj_in: dict):
        db_item = ItemPedido(**obj_in)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def update(self, db: Session, db_obj: ItemPedido, obj_in: dict):
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: ItemPedido):
        db.delete(db_obj)
        db.commit()

item_pedido_repository = ItemPedidoRepository()
