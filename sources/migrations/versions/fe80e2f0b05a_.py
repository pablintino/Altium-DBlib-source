"""empty message

Revision ID: fe80e2f0b05a
Revises: ae00fefcfa94
Create Date: 2020-05-15 12:14:15.935951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe80e2f0b05a'
down_revision = 'ae00fefcfa94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('connector_pcb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orientation', sa.String(length=50), nullable=True),
    sa.Column('pitch', sa.String(length=30), nullable=True),
    sa.Column('voltage_rating', sa.String(length=30), nullable=True),
    sa.Column('current_rating', sa.String(length=30), nullable=True),
    sa.Column('number_of_rows', sa.String(length=30), nullable=True),
    sa.Column('number_of_contacts', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dcdc_voltage_regulator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voltage_input_min', sa.String(length=30), nullable=True),
    sa.Column('voltage_output_min_fixed', sa.String(length=30), nullable=True),
    sa.Column('voltage_output_max', sa.String(length=30), nullable=True),
    sa.Column('current_output', sa.String(length=30), nullable=True),
    sa.Column('frequency_switching', sa.String(length=30), nullable=True),
    sa.Column('topology', sa.String(length=50), nullable=True),
    sa.Column('output_type', sa.String(length=50), nullable=True),
    sa.Column('number_of_outputs', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('led_indicator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('forward_voltage', sa.String(length=30), nullable=True),
    sa.Column('color', sa.String(length=30), nullable=True),
    sa.Column('lens_style', sa.String(length=50), nullable=True),
    sa.Column('lens_transparency', sa.String(length=30), nullable=True),
    sa.Column('dominant_wavelength', sa.String(length=30), nullable=True),
    sa.Column('test_current', sa.String(length=30), nullable=True),
    sa.Column('lens_size', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('linear_voltage_regulator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gain_bandwith', sa.String(length=50), nullable=True),
    sa.Column('output_type', sa.String(length=50), nullable=True),
    sa.Column('voltage_output_min_fixed', sa.String(length=30), nullable=True),
    sa.Column('voltage_output_max', sa.String(length=30), nullable=True),
    sa.Column('voltage_dropout_max', sa.String(length=30), nullable=True),
    sa.Column('current_supply_max', sa.String(length=30), nullable=True),
    sa.Column('current_output', sa.String(length=30), nullable=True),
    sa.Column('pssr', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('memory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('technology', sa.String(length=50), nullable=True),
    sa.Column('memory_type', sa.String(length=50), nullable=True),
    sa.Column('size', sa.String(length=30), nullable=True),
    sa.Column('interface', sa.String(length=50), nullable=True),
    sa.Column('clock_frequency', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('microcontroller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('core', sa.String(length=50), nullable=True),
    sa.Column('core_size', sa.String(length=30), nullable=True),
    sa.Column('speed', sa.String(length=30), nullable=True),
    sa.Column('flash_size', sa.String(length=30), nullable=True),
    sa.Column('ram_size', sa.String(length=30), nullable=True),
    sa.Column('peripherals', sa.String(length=250), nullable=True),
    sa.Column('connectivity', sa.String(length=250), nullable=True),
    sa.Column('voltage_supply', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opamp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gain_bandwith', sa.String(length=30), nullable=True),
    sa.Column('output_type', sa.String(length=50), nullable=True),
    sa.Column('input_type', sa.String(length=50), nullable=True),
    sa.Column('amplifier_type', sa.String(length=50), nullable=True),
    sa.Column('slew_rate', sa.String(length=30), nullable=True),
    sa.Column('voltage_supplies', sa.String(length=30), nullable=True),
    sa.Column('voltage_input_offset', sa.String(length=30), nullable=True),
    sa.Column('current_output', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('optocoupler_digital',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voltage_isolation', sa.String(length=30), nullable=True),
    sa.Column('voltage_saturation_max', sa.String(length=30), nullable=True),
    sa.Column('current_transfer_ratio_max', sa.String(length=30), nullable=True),
    sa.Column('current_transfer_ratio_min', sa.String(length=30), nullable=True),
    sa.Column('voltage_forward_typical', sa.String(length=30), nullable=True),
    sa.Column('voltage_output_max', sa.String(length=30), nullable=True),
    sa.Column('number_of_channels', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('optocoupler_linear',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voltage_isolation', sa.String(length=30), nullable=True),
    sa.Column('transfer_gain', sa.String(length=30), nullable=True),
    sa.Column('input_forward_voltage', sa.String(length=30), nullable=True),
    sa.Column('servo_gain', sa.String(length=30), nullable=True),
    sa.Column('forward_gain', sa.String(length=30), nullable=True),
    sa.Column('non_linearity', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('potentiometer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('power_max', sa.String(length=30), nullable=True),
    sa.Column('tolerance', sa.String(length=30), nullable=True),
    sa.Column('resistance_min', sa.String(length=30), nullable=True),
    sa.Column('resistance_max', sa.String(length=30), nullable=True),
    sa.Column('number_of_turns', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('switch_push_button',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('function', sa.String(length=50), nullable=True),
    sa.Column('dc_voltage_rating', sa.String(length=30), nullable=True),
    sa.Column('ac_voltage_rating', sa.String(length=30), nullable=True),
    sa.Column('current_rating', sa.String(length=30), nullable=True),
    sa.Column('circuit_type', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('switch_switch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voltage_rating', sa.String(length=30), nullable=True),
    sa.Column('current_rating', sa.String(length=30), nullable=True),
    sa.Column('number_of_positions', sa.String(length=30), nullable=True),
    sa.Column('circuit_type', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transceiver',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('duplex', sa.String(length=30), nullable=True),
    sa.Column('data_rate', sa.String(length=30), nullable=True),
    sa.Column('protocol', sa.String(length=30), nullable=True),
    sa.Column('voltage_supply', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['component.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transceiver')
    op.drop_table('switch_switch')
    op.drop_table('switch_push_button')
    op.drop_table('potentiometer')
    op.drop_table('optocoupler_linear')
    op.drop_table('optocoupler_digital')
    op.drop_table('opamp')
    op.drop_table('microcontroller')
    op.drop_table('memory')
    op.drop_table('linear_voltage_regulator')
    op.drop_table('led_indicator')
    op.drop_table('dcdc_voltage_regulator')
    op.drop_table('connector_pcb')
    # ### end Alembic commands ###