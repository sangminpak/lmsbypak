"""empty message

Revision ID: 1cbaee6cbaa6
Revises: 13b1faa45693
Create Date: 2022-07-29 07:50:14.669366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cbaee6cbaa6'
down_revision = '13b1faa45693'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignments', sa.Column('received_grade', sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assignments', 'received_grade')
    # ### end Alembic commands ###
