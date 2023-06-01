from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from vpic_api import get_vehicle_by_vin

class Base(DeclarativeBase):
    pass

class Vehicle(Base):
    __tablename__ = "vehicles"
    id: Mapped[int] = mapped_column(primary_key=True)
    vin: Mapped[str] = mapped_column(String(17), unique=True)
    make: Mapped[str] = mapped_column(String(30))
    model: Mapped[str] = mapped_column(String(30))
    year: Mapped[str] = mapped_column(String(4))
    body_class: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Vehicle(id={self.id!r}, vin={self.vin!r}, make={self.make!r}, model={self.model!r}, year={self.year!r}, body_class={self.body_class!r})"

    @classmethod
    def find(cls, session, vin):
      vehicle = cls._find_in_cache(session, vin)
      if not vehicle:
          vehicle = cls._find_in_vpic(vin)
          session.add(vehicle)
          session.commit()

      return vehicle

    @classmethod
    def _find_in_cache(cls, session, vin):
      return session.query(Vehicle).filter(Vehicle.vin == vin).first()

    @classmethod
    def _find_in_vpic(cls, vin):
        response = get_vehicle_by_vin(vin)
        return Vehicle(make=response["Make"], model=response["Model"], year=response["ModelYear"], body_class=response["BodyClass"], vin=vin)