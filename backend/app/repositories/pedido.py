from sqlalchemy.orm import Session
from app.models.pedido import Pedido

class PedidoRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Pedido).offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id_pedido: str):
        return db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()

    def create(self, db: Session, obj_in: dict):
        db_pedido = Pedido(**obj_in)
        db.add(db_pedido)
        db.commit()
        db.refresh(db_pedido)
        return db_pedido

    def update(self, db: Session, db_obj: Pedido, obj_in: dict):
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Pedido):
        db.delete(db_obj)
        db.commit()

pedido_repository = PedidoRepository()
