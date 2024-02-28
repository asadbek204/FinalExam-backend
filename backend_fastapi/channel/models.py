from sqlalchemy import String, ForeignKey
from backend_fastapi.database.database import Base
from backend_fastapi.database.field_types import int_pk, str_256, str_512, username, auto_utcnow, name
from sqlalchemy.orm import Mapped, mapped_column

from backend_fastapi.database.models import AvatarBase


class Channel(Base):
    __tablename__ = "channels"
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    name: Mapped[name]
    short_description: Mapped[str_256]
    description: Mapped[str_512]
    username: Mapped[username]
    created_at: Mapped[auto_utcnow]

    def __repr__(self) -> str:
        return f"<Channel (id: {self.id}, name: {self.name}, user_id: {self.user_id})>"


class ChannelAvatar(AvatarBase):
    __tablename__ = "channels_avatars"
    channel_id: Mapped[int] = mapped_column(ForeignKey('channels.id', ondelete="CASCADE"))
