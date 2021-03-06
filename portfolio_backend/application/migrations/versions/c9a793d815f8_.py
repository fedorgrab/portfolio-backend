"""empty message

Revision ID: c9a793d815f8
Revises: 644f8e836f31
Create Date: 2020-10-31 21:56:49.235284

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c9a793d815f8"
down_revision = "644f8e836f31"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "portfolio_project", sa.Column("short_description", sa.Text(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("portfolio_project", "short_description")
    # ### end Alembic commands ###
