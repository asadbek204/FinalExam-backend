import uuid
from backend_fastapi.auth.schemas import User, Token
from pydantic import BaseModel


class Wallet(BaseModel):
    id: uuid.UUID
    token: Token
    name: str
    user: User
    balance: int
    password: str
