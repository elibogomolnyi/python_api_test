"""Add column to Posts

Revision ID: 69b88b2c3ef8
Revises: cb0fe03d97b0
Create Date: 2023-06-10 20:18:50.029494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69b88b2c3ef8'
down_revision = 'cb0fe03d97b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable = False))


def downgrade() -> None:
    op.drop_column("posts", 'content')
