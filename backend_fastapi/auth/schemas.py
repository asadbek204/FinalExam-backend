from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    phone_number: str
    first_name: str | None
    last_name: str | None
    bio: str | None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    created_at: datetime | None
    is_active: bool
    is_online: bool
    is_bot: bool


class Token(BaseModel):
    access: str
    refresh: str


class UserPermission(BaseModel):
    title: str
    description: str


class User(UserOut):
    is_anonymous: bool
    is_superuser: bool
    token: Token
    permissions: list[UserPermission]


class ContactIn(BaseModel):
    user_id: int
    friend_id: int


class ContactOut(BaseModel):
    friend: UserOut


class UserStoriesIn(BaseModel):
    user_id: int
    media_id: int


class UserMomentsIn(UserStoriesIn):
    ...


class UserStoriesUpdate(BaseModel):
    media_id: int


class UserMomentsUpdate(UserMomentsIn):
    ...


class UserStoriesOut(BaseModel):
    media: int


class UserMomentsOut(UserStoriesOut):
    ...
