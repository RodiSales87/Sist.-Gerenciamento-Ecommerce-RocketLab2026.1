from sqlalchemy.orm import Session
from app.models.produto import Produto

class ProdutoRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Produto).offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id_produto: str):
        return db.query(Produto).filter(Produto.id_produto == id_produto).first()

    def create(self, db: Session, obj_in: dict):
        db_produto = Produto(**obj_in)
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto

    def update(self, db: Session, db_obj: Produto, obj_in: dict):
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Produto):
        db.delete(db_obj)
        db.commit()

# Instância global reutilizável do repositório
produto_repository = ProdutoRepository()