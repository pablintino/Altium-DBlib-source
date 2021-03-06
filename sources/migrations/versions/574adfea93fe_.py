"""empty message

Revision ID: 574adfea93fe
Revises: f58558097ac2
Create Date: 2020-06-23 19:02:09.387426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '574adfea93fe'
down_revision = 'f58558097ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inductor_choke',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_lines', sa.String(length=30), nullable=True),
    sa.Column('dc_resistance', sa.String(length=30), nullable=True),
    sa.Column('impedance_freq', sa.String(length=30), nullable=True),
    sa.Column('current_rating', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inductor_choke')
    # ### end Alembic commands ###
