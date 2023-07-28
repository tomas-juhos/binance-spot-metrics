"""Database Connector."""

import logging
from typing import List, Optional, Tuple

import psycopg2
import psycopg2.extensions
from psycopg2.extras import execute_values

logger = logging.getLogger(__name__)


class DBConnector:
    """DataBase Connector class."""

    def __init__(self, connection_string: str) -> None:
        """Postgres' data source.

        Args:
            connection_string: Definitions to connect with data source.
        """
        self._connection = psycopg2.connect(dsn=connection_string)
        self._connection.autocommit = False
        self._tx_cursor = None

    def connect(self) -> None:
        """Connects to data source."""
        url = self.ping_datasource()
        logger.info(f"{self.__class__.__name__} connected to: {url}.")

    def ping_datasource(self) -> str:
        """Pings data source."""
        cursor = self.cursor
        cursor.execute(
            "SELECT CONCAT("
            "current_user,'@',inet_server_addr(),':',"
            "inet_server_port(),' - ',version()"
            ") as v"
        )
        ping = cursor.fetchone()
        return ping[0] if ping else None

    @property
    def cursor(self) -> psycopg2.extensions.cursor:
        """Gets cursor."""
        if self._tx_cursor is not None:
            cursor = self._tx_cursor
        else:
            cursor = self._connection.cursor()

        return cursor

    def commit_transaction(self) -> None:
        """Commits a transaction."""
        self._connection.commit()

    def get_next_value(self, sequence: str) -> Optional[int]:
        """Get next id for the given interval."""
        cursor = self.cursor
        query = ("SELECT NEXTVAL('spot_{interval}_id_seq');").format(interval=sequence)
        cursor.execute(query)
        res = cursor.fetchone()

        return res[0] if res else None

    def fetch(self, query: str) -> Optional[List[Tuple]]:
        """Get latest persisted open time for the available symbols."""
        cursor = self.cursor
        cursor.execute(query)
        res = cursor.fetchall()

        return res if res else None

    def fetch_execute(self, instruction: str, records: List[Tuple]) -> Optional[List[Tuple]]:
        """Execute values.

        Args:
            instruction: sql query.
            records: records to persist.
        """
        if records:
            cursor = self.cursor
            res = execute_values(cur=cursor, sql=instruction, argslist=records, fetch=True)
            return res if res else None

    def execute(self, instruction: str, records: List[Tuple]) -> None:
        """Execute values.

        Args:
            instruction: sql query.
            records: records to persist.
        """
        if records:
            cursor = self.cursor
            execute_values(cur=cursor, sql=instruction, argslist=records)
