"""add categorias_imagens table

Revision ID: e2d73f66ecfb
Revises: eac77fd1577a
Create Date: 2026-04-13 16:47:03.561517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e2d73f66ecfb'
down_revision: Union[str, None] = 'eac77fd1577a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
