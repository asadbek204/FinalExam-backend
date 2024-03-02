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
    caption: Mapped[str] = mapped_column(String(2048))


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


class Avatar(BaseModel):
    """
    Base abstract class for all avatar files
    """
    __tablename__ = "avatars"

    image_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="CASCADE"))

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", image_id: {self.image_id})>"


def node(model_name: str) -> type:
    return typing.Annotated[
        int,
        mapped_column(
            ForeignKey(
                f"{model_name}.id",
                ondelete="RESTRICT"
            ),
            default=None,
            nullable=True
        )
    ]


class NodeListModel(BaseModel):
    __abstract__ = True

    prev_id: Mapped[int | None]
    current_id: Mapped[int]
    next_id: Mapped[int | None]


class MediaList(NodeListModel):
    __tablename__ = "media_list"
    __type_of_node__ = Media

    prev_id: Mapped[node("media_list")]
    current_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="RESTRICT"))
    next_id: Mapped[node("media_list")]


class MediaGroup(BaseModel):
    """
    Represents a group of medias in the database
    """
    __tablename__ = "media_groups"

    media_list: Mapped[int] = mapped_column(ForeignKey(MediaList.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
    edited_at: Mapped[updated_at]


class Message(BaseModel):
    """
    - media_group_id property is for make a caption for sent media(s)
    """
    __tablename__ = "messages"

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

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[name]
    short_description: Mapped[str_256]
    description: Mapped[str_512]
    username: Mapped[username]
    created_at: Mapped[auto_utcnow]
    password: Mapped[str_256]

    def __repr__(self) -> str:
        return f"<Chat (id: {self.id}, name: {self.name})>"
