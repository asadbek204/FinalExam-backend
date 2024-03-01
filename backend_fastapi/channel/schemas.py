from datetime import datetime
from pydantic import BaseModel
from backend_fastapi.auth.schemas import User
from backend_fastapi.group.schemas import Group
from backend_fastapi.database.schemas import ChatBase, AvatarBase


class Channel(ChatBase):
    chat_group: Group


class ChannelAvatar(AvatarBase):
    channel: Channel


class Subscriber(BaseModel):
    user: User
    channel: Channel
    subscribed_at: datetime


class Post(BaseModel):
    author: User
    channel: Channel
    created_at: datetime
    edited_at: datetime
    title: str
    description: str


class Tag(BaseModel):
    id: int
    author: User
    post: Post
    name: str
    created_at: datetime


class TaggedUser(Tag):
    tagged_user: User


class TaggedPost(Tag):
    tagged_post: Post


class TaggedChannel(Tag):
    tagged_channel: Channel


class TaggedGroup(Tag):
    tagged_group: Group
