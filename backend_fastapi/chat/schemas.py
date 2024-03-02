from pydantic import BaseModel
from backend_fastapi.auth.schemas import User
from backend_fastapi.database.schemas import Message


class PersonalChat(BaseModel):
    user: User
    friend: User
    blocked: bool = False


class ChatMessage(BaseModel):
    chat: PersonalChat
    message: Message
