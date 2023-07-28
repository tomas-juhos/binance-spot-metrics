"""Price Metrics model."""

from datetime import datetime
from typing import List, Tuple

from binance_spot_metrics.model.base import BaseModel
from binance_spot_metrics.model.kline import Kline
from binance_spot_metrics.model.metrics import Metrics


class PriceMetrics(BaseModel):
    """Price Metrics class."""

    id: int
    prev_id: int
    symbol: str
    open_time: datetime
    lag: int

    open_metrics: Metrics
    high_metrics: Metrics
    low_metrics: Metrics
    close_metrics: Metrics

    @classmethod
    def build_record(cls, records: List[Kline]) -> "PriceMetrics":
        """Build record object."""
        curr_record = records[-1]
        # OLDEST RECORD
        prev_record = records[0]
        res = cls()

        res.id = curr_record.id
        res.prev_id = prev_record.id
        res.symbol = curr_record.symbol
        res.open_time = curr_record.open_time
        res.lag = len(records) - 1

        open_values = [r.open_price for r in records if r.open_price]
        high_values = [r.high_price for r in records if r.high_price]
        low_values = [r.low_price for r in records if r.low_price]
        close_values = [r.close_price for r in records if r.close_price]

        res.open_metrics = Metrics(values=open_values)
        res.high_metrics = Metrics(values=high_values)
        res.low_metrics = Metrics(values=low_values)
        res.close_metrics = Metrics(values=close_values)

        return res

    def as_tuple(self) -> Tuple:
        """Get object as tuple."""
        return (
            self.id,
            self.prev_id,
            self.symbol,
            self.open_time,
            self.lag,
            self.open_metrics.delta,
            self.open_metrics.avg,
            self.open_metrics.max,
            self.open_metrics.min,
            self.open_metrics.range,
            self.high_metrics.delta,
            self.high_metrics.avg,
            self.high_metrics.max,
            self.high_metrics.min,
            self.high_metrics.range,
            self.low_metrics.delta,
            self.low_metrics.avg,
            self.low_metrics.max,
            self.low_metrics.min,
            self.low_metrics.range,
            self.close_metrics.delta,
            self.close_metrics.avg,
            self.close_metrics.max,
            self.close_metrics.min,
            self.close_metrics.range,
        )

