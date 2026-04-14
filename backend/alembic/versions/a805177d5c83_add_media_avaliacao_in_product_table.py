"""add media_avaliacao in product table

Revision ID: a805177d5c83
Revises: 001
Create Date: 2026-04-13 14:02:20.783976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a805177d5c83'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('produtos', sa.Column('media_avaliacao', sa.Float(), nullable=True, server_default='0.0'))
    pass


def downgrade() -> None:
    op.drop_column('produtos', 'media_avaliacao')
    pass
