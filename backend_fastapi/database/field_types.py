from datetime import datetime
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
import typing

str_64 = typing.Annotated[str, String(64)]
str_256 = typing.Annotated[str, String(256)]
str_512 = typing.Annotated[str, String(512)]
name = str_64 | None
username = typing.Annotated[str, String(32)]
int_pk = typing.Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
auto_utcnow = typing.Annotated[datetime, mapped_column(default_factory=datetime.utcnow)]
bool_default_false = typing.Annotated[bool, False]
