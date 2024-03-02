from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.database.models import BaseModel, Avatar, ChatABS, Message
from backend_fastapi.database.field_types import auto_utcnow
from backend_fastapi.auth.models import User


class Group(ChatABS):
    __tablename__ = "groups"


class GroupAvatar(BaseModel):
    __tablename__ = "group_avatars"

    author_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="SET NULL"), nullable=True)
    group_id: Mapped[int] = mapped_column(ForeignKey(Group.id, ondelete="CASCADE"))
    avatar_id: Mapped[int] = mapped_column(ForeignKey(Avatar.id, ondelete="CASCADE"))


class GroupMember(BaseModel):
    __tablename__ = "group_members"

    group_id: Mapped[int] = mapped_column(ForeignKey(Group.id, ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    joined_by: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="SET NULL"), nullable=True, default=None)
    joined_at: Mapped[auto_utcnow]


class GroupMessage(BaseModel):
    __tablename__ = "group_messages"

    group_id: Mapped[int] = mapped_column(ForeignKey(Group.id, ondelete="CASCADE"))
    message_id: Mapped[int] = mapped_column(ForeignKey(Message.id, ondelete="CASCADE"))
