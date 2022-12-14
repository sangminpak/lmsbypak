"""empty message

Revision ID: b8e69c0aa947
Revises: e14e7f994aa6
Create Date: 2022-07-29 10:21:31.334545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8e69c0aa947'
down_revision = 'e14e7f994aa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses', 'teacher_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses', 'teacher_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
