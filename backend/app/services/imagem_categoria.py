from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.imagem_categoria import CategoriaImagemCreate, CategoriaImagemUpdate
from app.repositories.imagem_categoria import categoria_imagem_repository

class CategoriaImagemService:
    def listar_categorias(self, db: Session, skip: int = 0, limit: int = 100):
        return categoria_imagem_repository.get_all(db, skip=skip, limit=limit)

    def buscar_categoria(self, db: Session, categoria_produto: str):
        categoria = categoria_imagem_repository.get_by_categoria(db, categoria_produto)
        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Categoria de imagem não encontrada"
            )
        return categoria

    def criar_categoria(self, db: Session, categoria_create: CategoriaImagemCreate):
        categoria_existente = categoria_imagem_repository.get_by_categoria(db, categoria_create.categoria_produto)
        if categoria_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Esta categoria já possui uma imagem registrada"
            )
        return categoria_imagem_repository.create(db, categoria_create.model_dump())

    def atualizar_categoria(self, db: Session, categoria_produto: str, categoria_update: CategoriaImagemUpdate):
        db_categoria = self.buscar_categoria(db, categoria_produto)
        update_data = categoria_update.model_dump(exclude_unset=True)
        return categoria_imagem_repository.update(db, db_obj=db_categoria, obj_in=update_data)

    def remover_categoria(self, db: Session, categoria_produto: str):
        db_categoria = self.buscar_categoria(db, categoria_produto)
        categoria_imagem_repository.delete(db, db_obj=db_categoria)

categoria_imagem_service = CategoriaImagemService()
