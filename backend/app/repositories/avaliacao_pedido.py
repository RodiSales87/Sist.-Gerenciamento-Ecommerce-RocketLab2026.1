from sqlalchemy.orm import Session
from app.models.avaliacao_pedido import AvaliacaoPedido

class AvaliacaoPedidoRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(AvaliacaoPedido).offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id_avaliacao: str):
        return db.query(AvaliacaoPedido).filter(AvaliacaoPedido.id_avaliacao == id_avaliacao).first()

    def create(self, db: Session, obj_in: dict):
        db_avaliacao = AvaliacaoPedido(**obj_in)
        db.add(db_avaliacao)
        db.commit()
        db.refresh(db_avaliacao)
        return db_avaliacao

    def update(self, db: Session, db_obj: AvaliacaoPedido, obj_in: dict):
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: AvaliacaoPedido):
        db.delete(db_obj)
        db.commit()

avaliacao_pedido_repository = AvaliacaoPedidoRepository()
