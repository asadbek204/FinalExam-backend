from datetime import datetime
from sqlalchemy import ForeignKey, String
from backend_fastapi.database.field_types import str_256, auto_utcnow, bool_default_false, username, name, str_512
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.database.models import AvatarBase, BaseModel


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

    is_anonymous: Mapped[bool] = mapped_column(default=True)
    is_bot: Mapped[bool_default_false]
    is_online: Mapped[bool_default_false]
    is_active: Mapped[bool_default_false]
    is_superuser: Mapped[bool_default_false]
    is_verified: Mapped[bool_default_false]

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", username: {self.username})>"


class UserAvatar(AvatarBase):
    __tablename__ = "users_avatars"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))


class Permission(BaseModel):
    __tablename__ = "permissions"

    title: Mapped[name]
    description: Mapped[str_256]

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", title: {self.title})>"


class UsersPermissions(BaseModel):
    __tablename__ = "users_permissions"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id", ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
