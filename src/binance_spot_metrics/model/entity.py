"""Entity data model."""

from enum import Enum


class Entity(str, Enum):
    """Type of Entity."""

    SPOT_1H_PRICE_METRICS = "SPOT_1H_PRICE_METRICS"
    SPOT_1H_VOLUME_METRICS = "SPOT_1H_VOLUME_METRICS"

    def __repr__(self) -> str:
        return str(self.value)
