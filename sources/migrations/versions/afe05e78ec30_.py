"""empty message

Revision ID: afe05e78ec30
Revises: a8376736e696
Create Date: 2020-07-07 21:58:31.816407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afe05e78ec30'
down_revision = 'a8376736e696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('capacitor', 'capacitor_ceramic')
    op.add_column('capacitor_ceramic', sa.Column('temperature_min', sa.String(length=30), nullable=True))
    op.add_column('capacitor_ceramic', sa.Column('temperature_max', sa.String(length=30), nullable=True))

    op.create_table('capacitor_electrolytic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tolerance', sa.String(length=30), nullable=True),
    sa.Column('voltage', sa.String(length=30), nullable=True),
    sa.Column('material', sa.String(length=30), nullable=True),
    sa.Column('polarised', sa.Boolean(), nullable=True),
    sa.Column('esr', sa.String(length=30), nullable=True),
    sa.Column('lifetime_temperature', sa.String(length=30), nullable=True),
    sa.Column('temperature_min', sa.String(length=30), nullable=True),
    sa.Column('temperature_max', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('capacitor_tantalum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tolerance', sa.String(length=30), nullable=True),
    sa.Column('voltage', sa.String(length=30), nullable=True),
    sa.Column('lifetime_temperature', sa.String(length=30), nullable=True),
    sa.Column('esr', sa.String(length=30), nullable=True),
    sa.Column('temperature_min', sa.String(length=30), nullable=True),
    sa.Column('temperature_max', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_table('capacitor_tantalum')
    op.drop_table('capacitor_electrolytic')
    op.rename_table('capacitor_ceramic', 'capacitor')
    op.drop_column('capacitor', 'temperature_min')
    op.drop_column('capacitor', 'temperature_max')
    # ### end Alembic commands ###
