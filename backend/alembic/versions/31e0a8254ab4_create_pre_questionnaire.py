"""create pre_questionnaire

Revision ID: 31e0a8254ab4
Revises: e6edf0b866a2
Create Date: 2026-10-17 16:03:08.233105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31e0a8254ab4'
down_revision: Union[str, Sequence[str], None] = 'e6edf0b866a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('pre_questionnaire',
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('what_result_you_want_to_get', sa.String(), nullable=True),
    sa.Column('what_mostly_hinder', sa.String(), nullable=True),
    sa.Column('are_you_ready', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['tg_id'], ['users.tg_id'], ),
    sa.PrimaryKeyConstraint('tg_id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('pre_questionnaire')
