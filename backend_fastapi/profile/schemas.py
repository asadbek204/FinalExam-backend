from datetime import datetime
from pydantic import BaseModel
from backend_fastapi.auth.schemas import User, Token


class Session(BaseModel):
    user: User
    token: Token
    created_at: datetime
    last_entered_at: datetime | None
    is_active: bool
    request_password: str
