"""create user db

Revision ID: 2b6c740223bf
Revises: 
Create Date: 2024-04-23 23:22:17.060853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func,text

# revision identifiers, used by Alembic.
revision: str = '2b6c740223bf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.UUID, primary_key=True,nullable=False,server_default=text("uuid_generate_v4()")),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('image_url', sa.String(500), nullable=True),
        sa.Column('content', sa.Unicode(200)),
        sa.Column('lat', sa.DECIMAL(8,6)),
        sa.Column('long', sa.DECIMAL(9,6)),
        sa.Column('created_at', sa.DateTime(TIMESTAMP =True),server_default=func.now()),
        sa.Column('updated_at',sa.DateTime(TIMESTAMP =True),server_default=func.now(), onupdate=func.now()),



    )


def downgrade() -> None:
    pass
