"""add scores and start_message_id

Revision ID: 2a7b9a226610
Revises: 5d0415e3dc20
Create Date: 2026-10-17 23:10:45.970840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a7b9a226610'
down_revision: Union[str, Sequence[str], None] = '5d0415e3dc20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('first_questions', sa.Column('scores', sa.JSON(), nullable=True))
    op.add_column('users', sa.Column('start_message_id', sa.Integer(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'start_message_id')
    op.drop_column('first_questions', 'scores')
