"""add users skipped_review

Revision ID: b4f1c9e27d3a
Revises: 2a7b9a226610
Create Date: 2026-10-18 14:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4f1c9e27d3a'
down_revision: Union[str, Sequence[str], None] = '2a7b9a226610'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('skipped_review', sa.Boolean(), server_default=sa.false(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'skipped_review')
