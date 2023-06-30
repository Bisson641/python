from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import (
    relationship,
)

from models import Base
from .mixins import CreatedAtMixin
from .post_tags import post_tags_association


class Tag(Base, CreatedAtMixin):
    name = Column(String(30), nullable=False, unique=True, )
    posts = relationship("Post", secondary=post_tags_association, back_populates="tags")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
