"""Added libraries for languages

Revision ID: 36123a921490
Revises: 0107ac835c3f
Create Date: 2024-12-10 16:21:28.119310

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "36123a921490"
down_revision = "0107ac835c3f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "libraries",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("language_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["language_id"], ["languages.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("libraries")
    # ### end Alembic commands ###