from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import Mapped, mapped_column
from .field_types import int_pk, str_64
from .database import Base
from settings import settings


class Image(Base):
    __tablename__ = "images"

    id: Mapped[int_pk]
    filename: Mapped[str_64]
    file_path: Mapped[str]

    @property
    def url(self) -> str:
        return f"{settings.server.url}/{self.file_path}/{self.filename}"

    def __repr__(self) -> str:
        return f"<Avatar (id: {self.id}, name: {self.filename})>"


class AvatarBase(AbstractConcreteBase, Base):
    __abstract__ = True

    id: Mapped[int_pk]
    image_id: Mapped[int] = mapped_column(ForeignKey("images.id", ondelete="CASCADE"))

    def __repr__(self) -> str:
        return f"<Avatar (id: {self.id}, image_id: {self.image_id})>"
