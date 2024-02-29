from datetime import datetime
from sqlalchemy import ForeignKey, String
from backend_fastapi.database.field_types import str_256, auto_utcnow, bool_default_false, username, name, str_512
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.database.models import AvatarBaseABS, BaseModel, Media


class Token(BaseModel):
    __tablename__ = "tokens"

    access: Mapped[str_256]
    refresh: Mapped[str_256]
    blacklisted: Mapped[bool_default_false]
    expires: Mapped[datetime]

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", blacklisted: {self.blacklisted})>"


class User(BaseModel):
    __tablename__ = "users"

    username: Mapped[username]
    first_name: Mapped[name]
    last_name: Mapped[name]
    bio: Mapped[str_512]
    password: Mapped[str_256]
    phone_number: Mapped[str] = mapped_column(String(15))
    token_id: Mapped[Token] = mapped_column(ForeignKey("tokens.id", ondelete="SET NULL"), nullable=True)
    created_at: Mapped[auto_utcnow]

    is_online: Mapped[bool_default_false]
    is_anonymous: Mapped[bool] = mapped_column(default=True)
    is_bot: Mapped[bool_default_false]
    is_active: Mapped[bool_default_false]
    is_superuser: Mapped[bool_default_false]

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", username: {self.username})>"


class UserProperties(BaseModel):
    __abstract__ = True

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))

    def __repr__(self):
        return "UserProperty: " + super().__repr__()[:-2] + f", user_id: {self.user_id}))>"


class Contacts(UserProperties):
    __tablename__ = "contacts"

    friend_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"), nullable=True, default=None)


class UserPermission(UserProperties):
    __tablename__ = "permissions"

    title: Mapped[name]
    description: Mapped[str_256]

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", title: {self.title})>"


class UsersPermissions(UserProperties):
    __tablename__ = "users_permissions"

    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id", ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]


class UserAvatar(AvatarBaseABS):
    __tablename__ = "users_avatars"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))


class UserPublish(UserProperties):
    __abstract__ = True

    media_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]


class UserStories(UserPublish):
    __tablename__ = "user_stories"


class UserMoments(UserPublish):
    __tablename__ = "user_moments"
