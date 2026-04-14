"""add media_avaliacao in product table again

Revision ID: eac77fd1577a
Revises: a805177d5c83
Create Date: 2026-04-13 16:43:54.180200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'eac77fd1577a'
down_revision: Union[str, None] = 'a805177d5c83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "categorias_imagens",
        sa.Column("categoria_produto", sa.String(100), primary_key=True),
        sa.Column("link_imagem", sa.String(500), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("categorias_imagens")
