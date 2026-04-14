"""add imagem_produto column

Revision ID: 6bf80ab6b2d1
Revises: e2d73f66ecfb
Create Date: 2026-04-14 13:56:44.716395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '6bf80ab6b2d1'
down_revision: Union[str, None] = 'e2d73f66ecfb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('produtos', sa.Column('imagem_produto', sa.String(length=500), nullable=True))


def downgrade() -> None:
    op.execute("""
        UPDATE produtos
        SET imagem_produto = (
            SELECT link_imagem 
            FROM categorias_imagens 
            WHERE categorias_imagens.categoria_produto = produtos.categoria_produto
        )
    """)
