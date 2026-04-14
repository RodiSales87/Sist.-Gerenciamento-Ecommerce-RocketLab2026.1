from sqlalchemy.orm import Session
from app.models.imagem_categoria import CategoriaImagem

class CategoriaImagemRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(CategoriaImagem).offset(skip).limit(limit).all()

    def get_by_categoria(self, db: Session, categoria_produto: str):
        return db.query(CategoriaImagem).filter(CategoriaImagem.categoria_produto == categoria_produto).first()

    def create(self, db: Session, obj_in: dict):
        db_categoria_imagem = CategoriaImagem(**obj_in)
        db.add(db_categoria_imagem)
        db.commit()
        db.refresh(db_categoria_imagem)
        return db_categoria_imagem

    def update(self, db: Session, db_obj: CategoriaImagem, obj_in: dict):
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: CategoriaImagem):
        db.delete(db_obj)
        db.commit()

categoria_imagem_repository = CategoriaImagemRepository()
