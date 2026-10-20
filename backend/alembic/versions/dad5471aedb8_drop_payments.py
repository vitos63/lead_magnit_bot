"""drop payments

Revision ID: dad5471aedb8
Revises: b4f1c9e27d3a
Create Date: 2026-10-20 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dad5471aedb8'
down_revision: Union[str, Sequence[str], None] = 'b4f1c9e27d3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Postgres can't drop a value from an enum, so BUY_PRODUCT stays in the type unused
    op.execute(
        "UPDATE users SET stage = CASE WHEN consent THEN 'SEND_PRE_QUESTIONNAIRE' ELSE 'GET_RESULT' END::stage "
        "WHERE stage = 'BUY_PRODUCT'"
    )
    op.drop_table('payments')
    op.drop_column('users', 'skipped_review')


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column('users', sa.Column('skipped_review', sa.Boolean(), server_default=sa.false(), nullable=False))
    op.create_table('payments',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('product', sa.String(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),
    sa.ForeignKeyConstraint(['tg_id'], ['users.tg_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
