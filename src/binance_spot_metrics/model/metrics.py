"""Metrics model."""

from decimal import Decimal
from typing import List


class Metrics:
    """Metrics class."""

    delta: Decimal
    avg: Decimal
    exp_avg: Decimal
    max: Decimal
    min: Decimal
    range: Decimal

    def __init__(self, values: List) -> None:
        """Build record object."""
        # THE VALUES HAVE TO BE ORDERED (BY TIME)
        n = len(values)
        self.total = sum(values)

        self.delta = values[-1] - values[0]
        self.avg = self.total / n
        self.max = max(values)
        self.min = min(values)
        self.range = self.max - self.min
