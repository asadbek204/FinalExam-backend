import uuid
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.auth.models import User
from backend_fastapi.database.models import BaseModel, Base
from backend_fastapi.database.field_types import auto_utcnow


class LiveStream(Base):
    __tablename__ = "live_streams"

    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(2048))
    created_at: Mapped[auto_utcnow]
    starting_at: Mapped[auto_utcnow]


class Viewer(BaseModel):
    __tablename__ = "stream_viewers"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    stream_id: Mapped[int] = mapped_column(ForeignKey(LiveStream.id, ondelete="CASCADE"))
    joined_by: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="SET NULL"))
    created_at: Mapped[auto_utcnow]


class Donate(BaseModel):
    __tablename__ = "stream_donates"

    viewer_id: Mapped[int] = mapped_column(ForeignKey(Viewer.id, ondelete="CASCADE"))
    description: Mapped[str] = mapped_column(String(128))
    amount: Mapped[int]
    created_at: Mapped[auto_utcnow]
