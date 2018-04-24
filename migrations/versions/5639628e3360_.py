"""empty message

Revision ID: 5639628e3360
Revises: b5255484a954
Create Date: 2018-04-24 14:29:13.407021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5639628e3360'
down_revision = 'b5255484a954'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problem_sku', sa.Column('file_url', sa.String(length=50), nullable=True))
    op.add_column('problem_sku', sa.Column('problem_cause', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('problem_sku', 'problem_cause')
    op.drop_column('problem_sku', 'file_url')
    # ### end Alembic commands ###