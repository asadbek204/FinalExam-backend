from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import Mapped
from .field_types import *
from .database import Base
from settings import settings


class BaseModel(AbstractConcreteBase, Base):
    __abstract__ = True

    id: Mapped[int_pk]

    def __repr__(self) -> str:
        return f"<{self.__tablename__} (id={self.id})>"


class DocumentBase(AbstractConcreteBase, Base):
    """
    Base class for all documents:
    - name : name of the file
    - path : path to the file
    """
    __abstract__ = True

    id: Mapped[int_pk]
    name: Mapped[str_64]
    path: Mapped[str]

    @property
    def url(self) -> str:
        return f"{settings.server.url}/{self.path}/{self.name}"

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", name: {self.name})>"


class Document(DocumentBase):
    """
    Represents a single document in the database
    - type : document type
    - size : document size in bytes
    - caption : caption of the document
    """
    __tablename__ = "documents"

    type: Mapped[str] = mapped_column(String(10))
    size: Mapped[float]
    caption: Mapped[str] = mapped_column(String(2048))


class MediaType(Enum):
    png: str = 'png'
    jpg: str = 'jpg'
    jpeg: str = 'jpeg'
    svg: str = 'svg'
    gif: str = 'gif'


class Media(DocumentBase):
    __tablename__ = "medias"

    type: Mapped[MediaType]
    caption: Mapped[str] = mapped_column(String(2048))


class AvatarBase(AbstractConcreteBase, Base):
    __abstract__ = True

    id: Mapped[int_pk]
    image_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="CASCADE"))

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", image_id: {self.image_id})>"


class MediaGroup(BaseModel):
    __tablename__ = "media_groups"

    created_at: Mapped[auto_utcnow]
    edited_at: Mapped[updated_at]


class MediaGroupMedia(BaseModel):
    __tablename__ = "media_group_medias"

    group_id: Mapped[int] = mapped_column(ForeignKey(MediaGroup.id, ondelete="CASCADE"))
    media_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="CASCADE"))


class MessageBase(BaseModel):
    """
    Base class for all messages:
    - child classes must implement the chat_id property
    - media_id property is for make a caption for sent media
    """
    __abstract__ = True

    text: Mapped[str_512]
    media_group_id: Mapped[int] = mapped_column(ForeignKey(MediaGroup.id, ondelete="CASCADE"), nullable=True, default=None)
    created_at: Mapped[auto_utcnow]
    edited_at: Mapped[updated_at]
    forward_from: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True, default=None)


class Chat(AbstractConcreteBase, Base):
    __abstract__ = True

    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[name]
    short_description: Mapped[str_256]
    description: Mapped[str_512]
    username: Mapped[username]
    created_at: Mapped[auto_utcnow]
    password: Mapped[str_256]

    def __repr__(self) -> str:
        return f"<Chat (id: {self.id}, name: {self.name})>"
