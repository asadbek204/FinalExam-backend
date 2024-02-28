from datetime import datetime
from backend_fastapi.database.database import Base
from backend_fastapi.database.field_types import int_pk, auto_utcnow
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int_pk]
    token_id: Mapped[int] = mapped_column(ForeignKey("tokens.id", ondelete="SET NULL"), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
    last_entered_at: Mapped[datetime] = mapped_column(default=None, nullable=True, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Session (id: {self.id}, user: {self.user_id})>"
