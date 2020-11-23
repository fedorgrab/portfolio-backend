"""empty message

Revision ID: ce5546901c49
Revises: 8cfc85e5f0d6
Create Date: 2020-11-12 16:40:27.365156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce5546901c49'
down_revision = '8cfc85e5f0d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('portfolio_project', sa.Column('image_source_link_inner', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('portfolio_project', 'image_source_link_inner')
    # ### end Alembic commands ###
