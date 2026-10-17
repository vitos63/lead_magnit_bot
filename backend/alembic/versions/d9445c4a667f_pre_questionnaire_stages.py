"""pre_questionnaire stages

Revision ID: d9445c4a667f
Revises: 7176e2d11418
Create Date: 2026-10-17 16:12:29.714449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9445c4a667f'
down_revision: Union[str, Sequence[str], None] = '7176e2d11418'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TYPE stage RENAME VALUE 'OPEN_questionnaire' TO 'OPEN_PRE_QUESTIONNAIRE'")
    with op.get_context().autocommit_block():
        op.execute("ALTER TYPE stage ADD VALUE IF NOT EXISTS 'SEND_PRE_QUESTIONNAIRE' AFTER 'OPEN_PRE_QUESTIONNAIRE'")


def downgrade() -> None:
    """Downgrade schema."""
    # Postgres can't drop a value from an enum, so SEND_PRE_QUESTIONNAIRE stays in the type
    op.execute("UPDATE users SET stage = 'OPEN_PRE_QUESTIONNAIRE' WHERE stage = 'SEND_PRE_QUESTIONNAIRE'")
    op.execute("ALTER TYPE stage RENAME VALUE 'OPEN_PRE_QUESTIONNAIRE' TO 'OPEN_questionnaire'")
