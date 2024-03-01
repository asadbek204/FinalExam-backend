from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import Mapped
from .field_types import *
from .database import Base
from settings import settings


class BaseModel(AbstractConcreteBase, Base):
    """
    - id : primary key for all nested models
    - __repr__ : base implementation for describing models
    """
    __abstract__ = True

    id: Mapped[int_pk]

    def __repr__(self) -> str:
        return f"<{self.__tablename__} (id={self.id})>"


class FileABC(AbstractConcreteBase, Base):
    """
    Base class for all documents:
    - name : name of the file
    - path : path to the file
    - caption : message to attach to the file
    """
    __abstract__ = True

    id: Mapped[int_pk]
    name: Mapped[str_64]
    path: Mapped[str]
    caption: Mapped[str] = mapped_column(String(2048))
    size: Mapped[float]

    @property
    def url(self) -> str:
        """
        :return: url of file for frontend
        """
        return f"{settings.server.url}/{self.path}/{self.name}"

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", name: {self.name})>"


class Document(FileABC):
    """
    - Represents a single document in the database
    - type : document type
    - size : document size in bytes
    - caption : caption of the document
    - type : type of the file
    """
    __tablename__ = "documents"

    type: Mapped[str] = mapped_column(String(10))


class MediaTypes(Enum):
    """
    Enumeration of available media types
    """
    jpeg = "image/jpeg"
    jpg = "image/jpg"
    png = "image/png"
    gif = "image/gif"
    tiff = "image/tiff"
    webp = "image/webp"
    mp3 = "audio/mp3"
    mp4 = "video/mp4"
    webm = "video/webm"
    ogg = "video/ogg"
    mpeg = "video/mpeg"
    mov = "video/mov"


class Media(FileABC):
    """
    Represents a single media file in the database
    """
    __tablename__ = "medias"

    type: Mapped[MediaTypes]


class AvatarBaseABS(AbstractConcreteBase, Base):
    """
    Base abstract class for all avatar files
    """
    __abstract__ = True

    id: Mapped[int_pk]
    image_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="CASCADE"))

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", image_id: {self.image_id})>"


class MediaGroup(BaseModel):
    """
    Represents a group of medias in the database
    """
    __tablename__ = "media_groups"

    created_at: Mapped[auto_utcnow]
    edited_at: Mapped[updated_at]


class MediaGroupMedia(BaseModel):
    """
    Represents a single media from a group of medias
    """
    __tablename__ = "media_group_medias"

    group_id: Mapped[int] = mapped_column(ForeignKey(MediaGroup.id, ondelete="CASCADE"))
    media_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="CASCADE"))


class MessageBase(BaseModel):
    """
    - Base abstract class for all messages:
    - child classes must implement the chat_id property
    - media_id property is for make a caption for sent media
    """
    __abstract__ = True

    text: Mapped[str_512]
    media_group_id: Mapped[int] = mapped_column(ForeignKey(MediaGroup.id, ondelete="CASCADE"), nullable=True, default=None)
    created_at: Mapped[auto_utcnow]
    edited_at: Mapped[updated_at]
    forward_from: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True, default=None)


class ChatABS(BaseModel):
    """
    Base abstract class for all chats
    """
    __abstract__ = True

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[name]
    short_description: Mapped[str_256]
    description: Mapped[str_512]
    username: Mapped[username]
    created_at: Mapped[auto_utcnow]
    password: Mapped[str_256]
    price: Mapped[int]

    def __repr__(self) -> str:
        return f"<Chat (id: {self.id}, name: {self.name})>"
