from sqlalchemy.orm import Session
from app.models.vendedor import Vendedor

class VendedorRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Vendedor).offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id_vendedor: str):
        return db.query(Vendedor).filter(Vendedor.id_vendedor == id_vendedor).first()

    def create(self, db: Session, obj_in: dict):
        db_vendedor = Vendedor(**obj_in)
        db.add(db_vendedor)
        db.commit()
        db.refresh(db_vendedor)
        return db_vendedor

    def update(self, db: Session, db_obj: Vendedor, obj_in: dict):
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Vendedor):
        db.delete(db_obj)
        db.commit()

vendedor_repository = VendedorRepository()