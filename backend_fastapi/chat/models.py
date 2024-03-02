from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from backend_fastapi.database.models import BaseModel, Message
from backend_fastapi.auth.models import User
from backend_fastapi.database.field_types import bool_default_false


class PersonalChat(BaseModel):
    __tablename__ = "chat"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    friend_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    blocked: Mapped[bool_default_false]


class ChatMessage(BaseModel):
    __tablename__ = "chat_messages"

    chat_id: Mapped[int] = mapped_column(ForeignKey(PersonalChat.id, ondelete="CASCADE"))
    message_id: Mapped[int] = mapped_column(ForeignKey(Message.id, ondelete="CASCADE"))
