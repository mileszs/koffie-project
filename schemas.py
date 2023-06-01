from typing import List, Union

from pydantic import BaseModel


class VehicleBase(BaseModel):
    make: str
    model: str
    year: str
    body_class: str


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    id: int

    class Config:
        orm_mode = True