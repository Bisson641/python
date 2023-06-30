from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)
from models import Base

post_tags_association = Table(
    "blog_post_tags_association",
    Base.metadata,
    Column("post_id", ForeignKey("blog_posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("blog_tags.id"), primary_key=True),
)
