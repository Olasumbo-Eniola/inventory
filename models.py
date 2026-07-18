"""Shared inventory data types."""

from decimal import Decimal
from typing import TypedDict


class InventoryItem(TypedDict):
    """Describe one inventory record."""

    item_name: str
    quantity: int
    price: Decimal
