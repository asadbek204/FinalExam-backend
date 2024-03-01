from pydantic import BaseModel
from backend_fastapi.auth.schemas import User
from backend_fastapi.database.schemas import MessageBase


class PersonalChat(BaseModel):
    user: User
    friend: User
    blocked: bool = False


class ChatMessage(MessageBase):
    chat: PersonalChat
