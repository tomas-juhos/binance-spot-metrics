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

    @classmethod
    def build_record(cls, values: List) -> "Metrics":
        """Build record object."""
        # THE VALUES HAVE TO BE ORDERED (BY TIME)
        res = cls()
        n = len(values)

        res.delta = values[-1] - values[0]
        res.avg = sum(values) / n
        res.max = max(values)
        res.min = min(values)
        res.range = res.max - res.min

        return res
