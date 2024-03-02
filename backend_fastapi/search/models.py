from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.database.models import BaseModel, Media, NodeListModel, node
from backend_fastapi.database.field_types import auto_utcnow
from backend_fastapi.auth.models import User
from backend_fastapi.channel.models import Post


class SearchHistory(BaseModel):
    __tablename__ = "search_history"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
    updated_at: Mapped[auto_utcnow]
    query: Mapped[str] = mapped_column(String(128))


class History(BaseModel):
    __abstract__ = True

    search_history: Mapped[int] = mapped_column(ForeignKey(SearchHistory.id, ondelete="CASCADE"), default=None, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
    last_seen_at: Mapped[auto_utcnow]


class SeenPostsList(NodeListModel):
    __tablename__ = "seen_posts"

    prev_id: Mapped[node("seen_posts")]
    current_id: Mapped[int] = mapped_column(ForeignKey(Post.id, ondelete="RESTRICT"))
    next_id: Mapped[node("seen_posts")]


class SeenMediasList(NodeListModel):
    __tablename__ = "seen_medias"

    prev_id: Mapped[node("seen_medias")]
    current_id: Mapped[int] = mapped_column(ForeignKey(Media.id, ondelete="RESTRICT"))
    next_id: Mapped[node("seen_medias")]
