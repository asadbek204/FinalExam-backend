from sqlalchemy import ForeignKey, String
from backend_fastapi.database.field_types import str_512, auto_utcnow, name, updated_at, int_pk
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.auth.models import User
from backend_fastapi.database.models import AvatarBase, BaseModel, AbstractConcreteBase, Chat, Base
from backend_fastapi.group.models import Group


class Channel(Chat):
    __tablename__ = "channels"

    chat_group_id: Mapped[int] = mapped_column(ForeignKey(Group.id, ondelete="SET NULL"), nullable=True)


class ChannelAvatar(AvatarBase):
    __tablename__ = "channels_avatars"

    channel_id: Mapped[int] = mapped_column(ForeignKey(Channel.id, ondelete="CASCADE"))


class Subscribers(BaseModel):
    __tablename__ = "subscribers"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    channel_id: Mapped[int] = mapped_column(ForeignKey(Channel.id, ondelete="CASCADE"))
    subscribed_at: Mapped[auto_utcnow]


class Post(BaseModel):
    __tablename__ = "posts"

    author_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="SET NULL"))
    channel_id: Mapped[int] = mapped_column(ForeignKey(Channel.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
    edited_at: Mapped[updated_at]

    title: Mapped[name]
    description: Mapped[str_512]


class TagBase(AbstractConcreteBase, Base):
    __abstract__ = True

    id: Mapped[int_pk]
    author_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="SET NULL"))
    post_id: Mapped[int] = mapped_column(ForeignKey(Post.id, ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[auto_utcnow]


class Tag(TagBase):
    __tablename__ = "tags"


class TaggedUsers(TagBase):
    __tablename__ = "tagged_users"

    tagged_user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))


class TaggedPosts(BaseModel):
    __tablename__ = "tagged_posts"

    tagged_post_id: Mapped[int] = mapped_column(ForeignKey(Post.id, ondelete="CASCADE"))


class TaggedChannels(BaseModel):
    __tablename__ = "tagged_channels"

    tagged_channel_id: Mapped[int] = mapped_column(ForeignKey(Channel.id, ondelete="CASCADE"))


class TaggedGroups(BaseModel):
    __tablename__ = "tagged_groups"

    tagged_group_id: Mapped[int] = mapped_column(ForeignKey(Group.id, ondelete="CASCADE"))
