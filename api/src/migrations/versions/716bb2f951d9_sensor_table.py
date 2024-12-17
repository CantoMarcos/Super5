"""sensor_table

Revision ID: 716bb2f951d9
Revises: 
Create Date: 2024-11-27 16:10:37.768669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '716bb2f951d9'
down_revision = None
branch_labels = None
depends_on = None


table_name = "sensor_data"

def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),  # ID do sensor
        sa.Column('sensor1', sa.Float(), nullable=False),  # Nome do sensor
        sa.Column('sensor2', sa.Float(), nullable=False),  # Valor do sensor
        sa.Column('sensor3', sa.Float(), nullable=False),  # Data e hora
        sa.Column('sensor4', sa.Float(), nullable=False),  # Data e hora
        sa.Column('sensor5', sa.Float(), nullable=False),  # Data e hora
        sa.Column('date', sa.DateTime(), nullable=False, index=True)  # Data e hora

    )


def downgrade() -> None:
    op.drop_table(table_name)
