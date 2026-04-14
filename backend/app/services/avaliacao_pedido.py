from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.avaliacao_pedido import AvaliacaoPedidoCreate, AvaliacaoPedidoUpdate
from app.repositories.avaliacao_pedido import avaliacao_pedido_repository

class AvaliacaoPedidoService:
    def listar_avaliacoes(self, db: Session, skip: int = 0, limit: int = 100):
        return avaliacao_pedido_repository.get_all(db, skip=skip, limit=limit)

    def buscar_avaliacao(self, db: Session, id_avaliacao: str):
        avaliacao = avaliacao_pedido_repository.get_by_id(db, id_avaliacao)
        if not avaliacao:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Avaliação não encontrada"
            )
        return avaliacao

    def criar_avaliacao(self, db: Session, avaliacao_create: AvaliacaoPedidoCreate):
        avaliacao_existente = avaliacao_pedido_repository.get_by_id(db, avaliacao_create.id_avaliacao)
        if avaliacao_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Esta avaliação já está registrada"
            )
        return avaliacao_pedido_repository.create(db, avaliacao_create.model_dump())

    def atualizar_avaliacao(self, db: Session, id_avaliacao: str, avaliacao_update: AvaliacaoPedidoUpdate):
        db_avaliacao = self.buscar_avaliacao(db, id_avaliacao)
        update_data = avaliacao_update.model_dump(exclude_unset=True)
        return avaliacao_pedido_repository.update(db, db_obj=db_avaliacao, obj_in=update_data)

    def remover_avaliacao(self, db: Session, id_avaliacao: str):
        db_avaliacao = self.buscar_avaliacao(db, id_avaliacao)
        avaliacao_pedido_repository.delete(db, db_obj=db_avaliacao)

avaliacao_pedido_service = AvaliacaoPedidoService()
