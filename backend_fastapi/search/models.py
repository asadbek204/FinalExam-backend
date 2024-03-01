import typing
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.database.models import BaseModel, Media
from backend_fastapi.database.field_types import auto_utcnow
from backend_fastapi.auth.models import User
from backend_fastapi.channel.models import Post


class SearchHistory(BaseModel):
    __tablename__ = "search_history"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
    updated_at: Mapped[auto_utcnow]
    query: Mapped[str] = mapped_column(String())


class History(BaseModel):
    __abstract__ = True

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    created_at: Mapped[auto_utcnow]
    last_seen_at: Mapped[auto_utcnow]


def node(model_name: str) -> type:
    return typing.Annotated[
        int,
        mapped_column(
            ForeignKey(
                f"{model_name}.id",
                ondelete="RESTRICT"
            ),
            default=None,
            nullable=True
        )
    ]


class NodeListModel(BaseModel):
    __abstract__ = True
    __tablename__ = "seen_posts"
    __type_of_node__ = Post.id

    prev_id: Mapped[node(__tablename__)]
    current_id: Mapped[int] = mapped_column(ForeignKey(__type_of_node__))
    next_id: Mapped[node(__tablename__)]


class SeenPostsList(NodeListModel):
    ...


class SeenMediasList(NodeListModel):
    __tablename__ = "seen_medias"
    __type_of_node__ = Media.id
