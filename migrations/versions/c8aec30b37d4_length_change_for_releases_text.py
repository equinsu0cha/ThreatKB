"""Length change for releases text

Revision ID: c8aec30b37d4
Revises: ee0d67b4e552
Create Date: 2018-02-24 13:01:41.987860

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c8aec30b37d4'
down_revision = 'ee0d67b4e552'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('releases', 'release_data',
               existing_type=mysql.TEXT(),
               type_=sa.Text(length=4294967295),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('releases', 'release_data',
               existing_type=sa.Text(length=4294967295),
               type_=mysql.TEXT(),
               existing_nullable=False)
    # ### end Alembic commands ###