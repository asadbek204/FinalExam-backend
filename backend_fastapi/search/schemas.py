from datetime import datetime
from pydantic import BaseModel
from backend_fastapi.auth.schemas import User
from backend_fastapi.channel.schemas import Post


class SearchHistory(BaseModel):
    user: User
    created_at: datetime
    updated_at: datetime
    query: str


class History(BaseModel):
    user: User
    post: Post
    created_at: datetime
    last_seen_at: datetime
