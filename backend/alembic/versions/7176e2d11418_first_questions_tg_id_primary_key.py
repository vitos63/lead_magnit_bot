"""first_questions tg_id primary key

Revision ID: 7176e2d11418
Revises: 31e0a8254ab4
Create Date: 2026-10-17 16:05:25.963650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7176e2d11418'
down_revision: Union[str, Sequence[str], None] = '31e0a8254ab4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column('first_questions', 'id')
    op.drop_constraint('first_questions_tg_id_key', 'first_questions', type_='unique')
    op.create_primary_key('first_questions_pkey', 'first_questions', ['tg_id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('first_questions_pkey', 'first_questions', type_='primary')
    op.create_unique_constraint('first_questions_tg_id_key', 'first_questions', ['tg_id'])
    op.add_column('first_questions', sa.Column('id', sa.Integer(), sa.Identity(), nullable=False))
    op.create_primary_key('first_questions_pkey', 'first_questions', ['id'])
