from sqlalchemy import ForeignKey
from backend_fastapi.auth.models import AbstractUser, Token, User
from backend_fastapi.database.models import Avatar, BaseModel, Message
from backend_fastapi.database.field_types import bool_default_false
from sqlalchemy.orm import Mapped, mapped_column


class Bot(AbstractUser):
    __tablename__ = "bots"

    token_id: Mapped[int] = mapped_column(ForeignKey(Token.id, ondelete="CASCADE"))
    owner_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    avatar_id: Mapped[int] = mapped_column(ForeignKey(Avatar.id, ondelete="CASCADE"))


class BotChat(BaseModel):
    __tablename__ = "bot_chats"

    bot_id: Mapped[int] = mapped_column(ForeignKey(Bot.id, ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    blocked: Mapped[bool_default_false]


class BotChatMessage(BaseModel):
    __tablename__ = "bot_chat_messages"

    chat_id: Mapped[int] = mapped_column(ForeignKey(BotChat.id, ondelete="CASCADE"))
    message_id: Mapped[int] = mapped_column(ForeignKey(Message.id, ondelete="CASCADE"))
