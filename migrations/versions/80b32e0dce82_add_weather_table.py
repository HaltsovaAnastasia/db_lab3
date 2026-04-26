"""add weather table

Revision ID: 80b32e0dce82
Revises: 34fd02c067ba
Create Date: 2026-04-20 02:25:26.185135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80b32e0dce82'
down_revision: Union[str, Sequence[str], None] = '34fd02c067ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'weather',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('country', sa.String(length=100), nullable=True),
        sa.Column('wind_degree', sa.Integer(), nullable=True),
        sa.Column('wind_kph', sa.Float(), nullable=True),
        sa.Column('wind_direction', sa.String(length=20), nullable=True),
        sa.Column('last_updated', sa.DateTime(), nullable=True),
        sa.Column('sunrise', sa.Time(), nullable=True),
        sa.Column('humidity', sa.Integer(), nullable=True),
        sa.Column('visibility_km', sa.Float(), nullable=True),
        sa.Column('pressure_mb', sa.Float(), nullable=True),
        sa.Column('uv_index', sa.Float(), nullable=True),
        sa.Column('condition', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weather_id'), 'weather', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_weather_id'), table_name='weather')
    op.drop_table('weather')
