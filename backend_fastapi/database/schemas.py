import typing
from datetime import datetime
from pydantic import BaseModel
from .models import MediaTypes
from backend_fastapi.auth.schemas import User


class File(BaseModel):
    id: int
    name: str
    path: str
    caption: str
    size: str


class Document(File):
    type: str


class Media(File):
    type: MediaTypes


class Avatar(BaseModel):
    id: int
    image: Media


class MediaList(BaseModel):
    prev: typing.Optional["MediaList"]
    current: Media
    next: typing.Optional["MediaList"]


class MediaGroup(BaseModel):
    media_list: MediaList
    created_at: datetime
    edited_at: datetime


class Message(BaseModel):
    text: str
    media_group: MediaGroup
    created_at: datetime
    edited_at: datetime
    forward_from: User


class ChatBase(BaseModel):
    user: User
    name: str
    short_description: str
    description: str
    username: str
    created_at: datetime
    password: str
