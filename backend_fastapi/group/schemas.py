from datetime import datetime
from pydantic import BaseModel
from backend_fastapi.auth.schemas import User
from backend_fastapi.database.schemas import ChatBase, AvatarBase


class Group(ChatBase):
    ...


class GroupAvatar(AvatarBase):
    author: User
    group: Group


class GroupMember(BaseModel):
    group: Group
    user: User
    joined_at: datetime
    joined_by: User
