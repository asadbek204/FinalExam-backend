import uuid
from datetime import datetime
from pydantic import BaseModel
from backend_fastapi.auth.schemas import User


class LiveStream(BaseModel):
    id: uuid.UUID
    user: User
    title: str
    description: str
    created_at: datetime
    starting_at: datetime


class Viewer(BaseModel):
    user: User
    stream: LiveStream
    joined_by: User
    created_at: datetime


class Donate(BaseModel):
    viewer: Viewer
    description: str
    amount: int
    created_at: datetime
