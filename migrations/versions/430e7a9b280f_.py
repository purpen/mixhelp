"""empty message

Revision ID: 430e7a9b280f
Revises: 0e7330f23578
Create Date: 2018-04-24 11:23:02.624157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '430e7a9b280f'
down_revision = '0e7330f23578'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problem_sku', sa.Column('spu_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'problem_sku', 'problem_spu', ['spu_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'problem_sku', type_='foreignkey')
    op.drop_column('problem_sku', 'spu_id')
    # ### end Alembic commands ###
