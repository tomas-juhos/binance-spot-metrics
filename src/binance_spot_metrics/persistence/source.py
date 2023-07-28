"""Source."""

import logging

from binance_spot_metrics.persistence.db_connector import DBConnector

logger = logging.getLogger(__name__)


class Source(DBConnector):
    """Source class."""

    def __init__(self, connection_string: str) -> None:
        """Postgres' data source.

        Args:
            connection_string: Definitions to connect with data source.
        """
        super().__init__(connection_string)
