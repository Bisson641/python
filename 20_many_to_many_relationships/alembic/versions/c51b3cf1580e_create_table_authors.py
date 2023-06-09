"""Create table authors

Revision ID: c51b3cf1580e
Revises: 4905973d6330
Create Date: 2023-06-23 22:23:22.044794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c51b3cf1580e"
down_revision = "4905973d6330"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "blog_authors",
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["blog_users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("blog_authors")
    # ### end Alembic commands ###
