from datetime import datetime
from backend_fastapi.database.models import BaseModel
from backend_fastapi.database.field_types import auto_utcnow, bool_default_false
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.auth.models import User, Token


class Session(BaseModel):
    __tablename__ = "sessions"

    token_id: Mapped[int] = mapped_column(ForeignKey(Token.id, ondelete="SET NULL"), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"), nullable=True)
    created_at: Mapped[auto_utcnow]
    last_entered_at: Mapped[datetime] = mapped_column(default=None, nullable=True)
    is_active: Mapped[bool_default_false]

    request_password: Mapped[str] = mapped_column(String(8), default=None, nullable=True)
    count_enter_attempts: Mapped[int]

    def __repr__(self) -> str:
        return super().__repr__()[:-2] + f", user: {self.user_id})>"
