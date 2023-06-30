from sqlalchemy import (
    Column,
    String,
    Boolean,
    false,
)
from sqlalchemy.orm import (
    relationship,
)
from models.base import Base
from .mixins import CreatedAtMixin


class User(CreatedAtMixin, Base):
    username = Column(String(30), unique=True, nullable=False,)
    email = Column(String(150), unique=True, nullable=True,)
    archived = Column(Boolean, default=False, server_default=false(), nullable=False,)
    # bio = Column(String, default="", server_default="", nullable=False,)
    author = relationship("Author", back_populates="user", uselist=False, )


    def __str__(self):
        return f"User(id={self.id}, username={self.username}, created_at={self.created_at})"

    def __repr__(self):
        return str(self)
