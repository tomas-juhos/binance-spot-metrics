"""Transaction Metrics model."""

from datetime import datetime
from decimal import Decimal
from typing import List, Tuple

from binance_spot_metrics.model.base import BaseModel
from binance_spot_metrics.model.kline import Kline
from binance_spot_metrics.model.metrics import Metrics


class TransactionMetrics(BaseModel):
    """Transaction Metrics class."""

    id: int
    prev_id: int
    symbol: str
    open_time: datetime
    lag: int

    volume_metrics: Metrics
    taker_buy_volume_metrics: Metrics
    taker_buy_volume_pct: Decimal

    quote_volume_metrics: Metrics
    taker_buy_quote_volume_metrics: Metrics
    taker_buy_quote_volume_pct: Decimal

    trades_metrics: Metrics
    avg_volume_per_trade: Decimal
    avg_taker_buy_volume_per_trade: Decimal
    avg_quote_volume_per_trade: Decimal
    avg_taker_buy_quote_volume_per_trade: Decimal

    @classmethod
    def build_record(cls, records: List[Kline]) -> "TransactionMetrics":
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

        volume_values = [r.volume for r in records if r.volume]
        taker_buy_volume_values = [r for r in records if r.taker_buy_volume]
        quote_volume_values = [r.quote_volume for r in records if r.quote_volume]
        taker_buy_quote_volume_values = [r for r in records if r.taker_buy_quote_volume]
        trades_values = [r.trades for r in records if r.trades]

        res.volume_metrics = Metrics(values=volume_values)
        res.taker_buy_volume_metrics = Metrics(values=taker_buy_volume_values)
        res.quote_volume_metrics = Metrics(values=quote_volume_values)
        res.taker_buy_quote_volume_metrics = Metrics(values=taker_buy_quote_volume_values)
        res.trades_metrics = Metrics(values=trades_values)

        res.taker_buy_volume_pct = res.taker_buy_volume_metrics.total / res.volume_metrics.total
        res.taker_buy_quote_volume_pct = res.taker_buy_quote_volume_metrics.total / res.quote_volume_metrics.total

        res.avg_volume_per_trade = res.volume_metrics.total / res.trades_metrics.total
        res.avg_taker_buy_volume_per_trade = res.taker_buy_volume_metrics.total / res.trades_metrics.total
        res.avg_quote_volume_per_trade = res.quote_volume_metrics.total / res.trades_metrics.total
        res.avg_taker_buy_quote_volume_per_trade = res.taker_buy_quote_volume_metrics.total / res.trades_metrics.total

        return res

    def as_tuple(self) -> Tuple:
        """Get object as tuple."""
        return (
            self.id,
            self.prev_id,
            self.symbol,
            self.open_time,
            self.lag,
            self.volume_metrics.delta,
            self.volume_metrics.avg,
            self.volume_metrics.max,
            self.volume_metrics.min,
            self.volume_metrics.range,
            self.taker_buy_volume_metrics.delta,
            self.taker_buy_volume_metrics.avg,
            self.taker_buy_volume_metrics.max,
            self.taker_buy_volume_metrics.min,
            self.taker_buy_volume_metrics.range,
            self.taker_buy_volume_pct,
            self.quote_volume_metrics.delta,
            self.quote_volume_metrics.avg,
            self.quote_volume_metrics.max,
            self.quote_volume_metrics.min,
            self.quote_volume_metrics.range,
            self.taker_buy_quote_volume_metrics.delta,
            self.taker_buy_quote_volume_metrics.avg,
            self.taker_buy_quote_volume_metrics.max,
            self.taker_buy_quote_volume_metrics.min,
            self.taker_buy_quote_volume_metrics.range,
            self.taker_buy_quote_volume_pct,
            self.trades_metrics.delta,
            self.trades_metrics.avg,
            self.trades_metrics.max,
            self.trades_metrics.min,
            self.trades_metrics.range,
            self.avg_volume_per_trade,
            self.avg_taker_buy_volume_per_trade,
            self.avg_quote_volume_per_trade,
            self.avg_taker_buy_quote_volume_per_trade,
        )
