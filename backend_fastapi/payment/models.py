import uuid
from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from backend_fastapi.database.field_types import str_256
from backend_fastapi.database.database import Base
from backend_fastapi.auth.models import User


class Wallet(Base):
    __tablename__ = "payment"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, unique=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(16), unique=True)
    user: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    balance: Mapped[float] = mapped_column(Numeric())
    password: Mapped[str_256]
