from decimal import Decimal

from binance_spot_metrics.model.base import BaseModel

class Metrics(BaseModel):
    delta: Decimal
    avg: Decimal
    exp_avg: Decimal
    max: Decimal
    min: Decimal
    range: Decimal
    total: Decimal