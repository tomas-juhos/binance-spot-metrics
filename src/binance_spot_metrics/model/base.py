"""Base data model."""

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple


class BaseModel(ABC):
    """Base state."""

    @classmethod
    @abstractmethod
    def build_record(cls, records: List[List]) -> "BaseModel":
        """Creates object from source record."""

    @abstractmethod
    def as_tuple(self) -> Tuple:
        """Returns object values as a tuple."""
