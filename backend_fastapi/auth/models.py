from datetime import datetime
from sqlalchemy import ForeignKey, String
from backend_fastapi.database.database import Base
from backend_fastapi.database.field_types import int_pk, str_256, auto_utcnow, bool_default_false, username, name
from sqlalchemy.orm import Mapped, mapped_column

from backend_fastapi.database.models import AvatarBase
from settings import settings
from enum import Enum

parser = {
    "D": "default",
    "B": "blogger",
    "M": "manager",
    "A": "admin",
    "G": "gamer",
    "P": "premium"
}


class UserPriorityEnum(Enum):
    default: str = "D"
    blogger: str = "B"
    manager: str = "M"
    admin: str = "A"
    gamer: str = "G"
    premium: str = "P"

    def parse(self) -> str:
        return parser[self.value]


class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[int_pk]
    access: Mapped[str_256]
    refresh: Mapped[str_256]
    blacklisted: Mapped[bool_default_false]
    expires: Mapped[datetime]

    def __repr__(self) -> str:
        return f"<Token (id: {self.id}, blacklisted: {self.blacklisted})>"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    username: Mapped[username]
    first_name: Mapped[name]
    email: Mapped[str]
    password: Mapped[str_256]
    phone_number: Mapped[str] = mapped_column(String(15))
    created_at: Mapped[auto_utcnow]
    priorities: Mapped[UserPriorityEnum]
    token_id: Mapped[Token] = mapped_column(ForeignKey("tokens.id", ondelete="SET NULL"), nullable=True)

    is_online: Mapped[bool_default_false]
    is_active: Mapped[bool_default_false]
    is_superuser: Mapped[bool_default_false]
    is_verified: Mapped[bool_default_false]

    def __repr__(self) -> str:
        return f"<User (id: {self.id}, username: {self.username})>"


class UserAvatar(AvatarBase):
    __tablename__ = "users_avatars"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
