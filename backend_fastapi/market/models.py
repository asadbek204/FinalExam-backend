from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from backend_fastapi.auth.models import User
from backend_fastapi.database.models import BaseModel, Avatar
from backend_fastapi.database.field_types import *


class ProductType(Enum):
    account = "A"
    channel = "C"
    group = "G"
    bot = "B"


class Product(BaseModel):
    __tablename__ = "products"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    avatar: Mapped[int] = mapped_column(ForeignKey(Avatar.id, ondelete="CASCADE"))
    username: Mapped[username]
    name: Mapped[name]
    subscribers_count: Mapped[int | None]
    product_id: Mapped[int]
    product_type: Mapped[ProductType]
    price: Mapped[int]
    created_at: Mapped[auto_utcnow]
    updated_at: Mapped[datetime | None]


class Order(BaseModel):
    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    product_id: Mapped[int] = mapped_column(ForeignKey(Product.id, ondelete="CASCADE"))
    suggested_price: Mapped[int]
    ordered_at: Mapped[auto_utcnow]
    updated_at: Mapped[datetime | None]
