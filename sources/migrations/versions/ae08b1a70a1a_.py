"""empty message

Revision ID: ae08b1a70a1a
Revises: 7e6770997013
Create Date: 2020-08-06 22:48:36.390804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae08b1a70a1a'
down_revision = '7e6770997013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fuse_pptc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('current_hold', sa.String(length=30), nullable=True),
    sa.Column('current_trip', sa.String(length=30), nullable=True),
    sa.Column('voltage_rating', sa.String(length=30), nullable=True),
    sa.Column('resistance_maximum', sa.String(length=30), nullable=True),
    sa.Column('resistance_minimum', sa.String(length=30), nullable=True),
    sa.Column('power_rating', sa.String(length=30), nullable=True),
    sa.Column('current_rating', sa.String(length=30), nullable=True),
    sa.Column('temperature_min', sa.String(length=30), nullable=True),
    sa.Column('temperature_max', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fuse_pptc')
    # ### end Alembic commands ###
