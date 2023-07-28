"""Entity data model."""

from enum import Enum


class Entity(str, Enum):
    """Type of Entity."""

    SPOT_1H_PRICE = "SPOT_1H_PRICE"
    SPOT_1H_VOLUME = "SPOT_1H_VOLUME"

    def __repr__(self) -> str:
        return str(self.value)
