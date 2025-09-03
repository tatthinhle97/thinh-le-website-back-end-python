from typing import List
from sqlalchemy import VARCHAR, NVARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class StateModel(BaseModel):
    __tablename__ = "states"

    id: Mapped[str] = mapped_column(VARCHAR(2), primary_key=True)
    name: Mapped[str] = mapped_column(NVARCHAR(25))

    # One state has many cities
    cities: Mapped[List["CityModel"]] = relationship(
        back_populates = "state",
        cascade = "all, delete-orphan"
    )

class CityModel(BaseModel):
    __tablename__ = "cities"

    # Composit key
    state_id: Mapped[str] = mapped_column(VARCHAR(2), ForeignKey('states.id'), primary_key=True)
    county: Mapped[str] = mapped_column(NVARCHAR(30), primary_key=True)
    city: Mapped[str] = mapped_column(NVARCHAR(45), primary_key=True)

    state: Mapped["StateModel"] = relationship(back_populates="cities")