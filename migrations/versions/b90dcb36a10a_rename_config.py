"""Rename config

Revision ID: b90dcb36a10a
Revises: 7c6433145877
Create Date: 2017-08-21 14:16:40.991460

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b90dcb36a10a'
down_revision = '7c6433145877'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cfg_settings',
                    sa.Column('key', sa.String(length=128), nullable=False),
                    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('date_modified', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('public', sa.Boolean(), nullable=True),
                    sa.Column('value', sa.String(length=2048), nullable=True),
                    sa.PrimaryKeyConstraint('key')
                    )
    op.create_index(u'ix_cfg_settings_key', 'cfg_settings', ['key'], unique=False)
    op.create_index(u'ix_cfg_settings_public', 'cfg_settings', ['public'], unique=False)
    op.drop_table(u'config')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(u'config',
    sa.Column(u'date_created', sa.DATETIME(), nullable=True),
    sa.Column(u'date_modified', sa.DATETIME(), nullable=True),
    sa.Column(u'key', mysql.VARCHAR(length=256), nullable=True),
    sa.Column(u'public', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column(u'value', mysql.VARCHAR(length=2048), nullable=True),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_index(u'ix_cfg_settings_public', table_name='cfg_settings')
    op.drop_index(u'ix_cfg_settings_key', table_name='cfg_settings')
    op.drop_table('cfg_settings')
    # ### end Alembic commands ###
