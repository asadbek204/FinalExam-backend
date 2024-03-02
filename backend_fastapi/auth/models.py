from datetime import datetime
from typing import Never
from _sha256 import sha256
from sqlalchemy import ForeignKey, String
from backend_fastapi.database.field_types import str_256, auto_utcnow, bool_default_false, username, name, str_512
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.database.models import Avatar, BaseModel, Media


class Token(BaseModel):
    __tablename__ = "tokens"

    access: Mapped[str_256]
    refresh: Mapped[str_256]
    blacklisted: Mapped[bool_default_false]
    expires: Mapped[datetime]

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", blacklisted: {self.blacklisted})>"


class AbstractUser(BaseModel):
    __abstract__ = True

    username: Mapped[username]
    first_name: Mapped[name]
    last_name: Mapped[name]
    bio: Mapped[str_512]
    token_id: Mapped[Token] = mapped_column(ForeignKey("tokens.id", ondelete="SET NULL"), nullable=True)
    created_at: Mapped[auto_utcnow]
    is_bot: Mapped[bool_default_false]


class User(AbstractUser):
    __tablename__ = "users"

    password: Mapped[str_256]
    phone_number: Mapped[str] = mapped_column(String(15))
    is_online: Mapped[bool_default_false]
    is_anonymous: Mapped[bool] = mapped_column(default=True)
    is_active: Mapped[bool_default_false]
    is_superuser: Mapped[bool_default_false]

    @property
    def pwd(self) -> Never:
        """
        :return: not implemented because nobody can get a password
        """
        raise NotImplemented("nobody can get a password")

    @pwd.setter
    def pwd(self, value: str) -> None:
        """
        :param value: str value for hashing and changing password
        """
        if not isinstance(value, str):
            raise TypeError(f"type of pwd must be a string, not {type(value)}")
        if len(value) < 8:
            raise ValueError(f"value must be at least 8 characters, not {len(value)}")
        self.password = sha256(value).hexdigest()

    def verify_password(self, password: str) -> bool:
        return self.password == sha256(password).hexdigest()

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

    permission_id: Mapped[int] = mapped_column(ForeignKey(UserPermission.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]


class UserAvatar(UserProperties):
    __tablename__ = "users_avatars"

    avatar_id: Mapped[int] = mapped_column(ForeignKey(Avatar.id, ondelete="CASCADE"))


class UserPublish(UserProperties):
    __abstract__ = True

    media_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]


class UserStories(UserPublish):
    __tablename__ = "user_stories"


class UserMoments(UserPublish):
    __tablename__ = "user_moments"
