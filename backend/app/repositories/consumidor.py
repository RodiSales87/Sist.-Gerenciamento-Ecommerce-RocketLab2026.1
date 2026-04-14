from sqlalchemy.orm import Session
from app.models.consumidor import Consumidor

class ConsumidorRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Consumidor).offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, id_consumidor: str):
        return db.query(Consumidor).filter(Consumidor.id_consumidor == id_consumidor).first()

    def create(self, db: Session, obj_in: dict):
        db_consumidor = Consumidor(**obj_in)
        db.add(db_consumidor)
        db.commit()
        db.refresh(db_consumidor)
        return db_consumidor

    def update(self, db: Session, db_obj: Consumidor, obj_in: dict):
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Consumidor):
        db.delete(db_obj)
        db.commit()

consumidor_repository = ConsumidorRepository()