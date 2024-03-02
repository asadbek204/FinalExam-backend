from pydantic import BaseModel
from backend_fastapi.auth.schemas import User, Token
from backend_fastapi.database.models import Message
from backend_fastapi.database.schemas import Avatar, ChatBase


class Bot(BaseModel):
    username: str
    first_name: str
    last_name: str
    bio: str
    token: Token
    owner: User
    avatar: Avatar
    is_bot: bool


class BotChat(ChatBase):
    bot: Bot
    user: User
    blocked: bool = False


class BotChatMessage(BaseModel):
    chat: BotChat
    message: Message
