"""Create START_FILTER_REQUESTS_LENGTH

Revision ID: 808f4e517394
Revises: af2de80654b6
Create Date: 2018-11-29 10:58:02.103458

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from app.models import cfg_settings
import datetime

# revision identifiers, used by Alembic.
revision = '808f4e517394'
down_revision = 'af2de80654b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    date_created = datetime.datetime.now().isoformat()
    date_modified = datetime.datetime.now().isoformat()

    op.bulk_insert(
        cfg_settings.Cfg_settings.__table__,
        [
            {"key": "START_FILTER_REQUESTS_LENGTH", "value": "3", "public": True, "date_created": date_created,
             "date_modified": date_modified,
             "description": "The number characters to wait to start filtering table content"},
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    keys = ["START_FILTER_REQUESTS_LENGTH"]
    for key in keys:
        op.execute("""DELETE from cfg_settings where `key`='%s';""" % (key))
        # ### end Alembic commands ###