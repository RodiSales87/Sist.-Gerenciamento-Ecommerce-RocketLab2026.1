from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.produto import ProdutoCreate, ProdutoUpdate
from app.repositories.produto import produto_repository

class ProdutoService:
    def listar_produtos(self, db: Session, skip: int = 0, limit: int = 100):
        return produto_repository.get_all(db, skip=skip, limit=limit)

    def buscar_produto(self, db: Session, id_produto: str):
        produto = produto_repository.get_by_id(db, id_produto)
        if not produto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
        return produto

    def criar_produto(self, db: Session, produto_create: ProdutoCreate):
        produto_existente = produto_repository.get_by_id(db, produto_create.id_produto)
        if produto_existente:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este id_produto já está registrado")
        
        return produto_repository.create(db, produto_create.model_dump())

    def atualizar_produto(self, db: Session, id_produto: str, produto_update: ProdutoUpdate):
        db_produto = self.buscar_produto(db, id_produto) # Reaproveita a validação de buscar
        
        update_data = produto_update.model_dump(exclude_unset=True)
        return produto_repository.update(db, db_obj=db_produto, obj_in=update_data)

    def remover_produto(self, db: Session, id_produto: str):
        db_produto = self.buscar_produto(db, id_produto)
        produto_repository.delete(db, db_obj=db_produto)

# Instância global do serviço
produto_service = ProdutoService()