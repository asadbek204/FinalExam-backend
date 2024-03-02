import typing
from datetime import datetime
from pydantic import BaseModel
from backend_fastapi.auth.schemas import User
from backend_fastapi.channel.schemas import Post
from backend_fastapi.database.schemas import Media


class SearchHistory(BaseModel):
    user: User
    created_at: datetime
    updated_at: datetime
    query: str


class History(BaseModel):
    user: User
    search_history: SearchHistory
    created_at: datetime
    last_seen_at: datetime


class SeenPostsList(BaseModel):
    prev: typing.Optional["SeenPostsList"]
    current: Post
    next: typing.Optional["SeenPostsList"]


class SeenMediasList(BaseModel):
    prev: typing.Optional["SeenMediasList"]
    current: Media
    next: typing.Optional["SeenMediasList"]
