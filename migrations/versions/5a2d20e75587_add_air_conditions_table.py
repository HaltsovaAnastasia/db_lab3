"""add air_conditions table

Revision ID: 5a2d20e75587
Revises: 80b32e0dce82
Create Date: 2026-04-21 03:55:39.284469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a2d20e75587'
down_revision: Union[str, Sequence[str], None] = '80b32e0dce82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'air_conditions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('weather_id', sa.Integer(), nullable=False),
        sa.Column('humidity', sa.Integer(), nullable=True),
        sa.Column('visibility_km', sa.Float(), nullable=True),
        sa.Column('pressure_mb', sa.Float(), nullable=True),
        sa.Column('uv_index', sa.Float(), nullable=True),
        sa.Column('condition', sa.String(length=100), nullable=True),
        sa.Column('should_go_outside', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['weather_id'], ['weather.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('weather_id')
    )
    op.create_index(op.f('ix_air_conditions_id'), 'air_conditions', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_air_conditions_id'), table_name='air_conditions')
    op.drop_table('air_conditions')
