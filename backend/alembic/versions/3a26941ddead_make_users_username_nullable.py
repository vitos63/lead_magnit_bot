"""make users username nullable

Revision ID: 3a26941ddead
Revises: 3de16a801c93
Create Date: 2026-10-17 12:02:17.589667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a26941ddead'
down_revision: Union[str, Sequence[str], None] = '3de16a801c93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('users', 'username', existing_type=sa.String(), nullable=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('users', 'username', existing_type=sa.String(), nullable=False)
