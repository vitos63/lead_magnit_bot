"""drop users name

Revision ID: e6edf0b866a2
Revises: 3a26941ddead
Create Date: 2026-10-17 12:05:43.723009

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6edf0b866a2'
down_revision: Union[str, Sequence[str], None] = '3a26941ddead'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column('users', 'name')


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
