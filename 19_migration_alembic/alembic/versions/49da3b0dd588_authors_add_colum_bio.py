"""Authors add colum bio

Revision ID: 49da3b0dd588
Revises: 313eebfbbd74
Create Date: 2023-06-23 23:04:01.923366

"""
from alembic import op
import sqlalchemy as sa

from models import Author, User


# revision identifiers, used by Alembic.
revision = "49da3b0dd588"
down_revision = "313eebfbbd74"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("blog_authors", sa.Column("bio", sa.String(), server_default="", nullable=False))
    bind = op.get_bind()
    bind.execute(
        sa.update(Author)
        .where(Author.user_id == User.id)
        .values({Author.bio: User.bio})
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("blog_authors", "bio")
    # ### end Alembic commands ###