from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Vehicle(Base):
    __tablename__ = "vehicles"
    id: Mapped[int] = mapped_column(primary_key=True)
    make: Mapped[str] = mapped_column(String(30))
    model: Mapped[str] = mapped_column(String(30))
    year: Mapped[str] = mapped_column(String(4))
    body_class: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Vehicle(id={self.id!r}, make={self.make!r}, model={self.model!r}, year={self.year!r}, body_class={self.body_class!r})"