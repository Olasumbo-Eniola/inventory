"""Reusable inventory validation and calculation functions."""

from collections.abc import Sequence
from decimal import Decimal

from models import InventoryItem


def validate_item(item: InventoryItem) -> None:
    """Raise a clear error when an inventory record contains invalid data."""
    if not item["item_name"].strip():
        raise ValueError("Item name cannot be empty.")
    if type(item["quantity"]) is not int or item["quantity"] < 0:
        raise ValueError("Item quantity must be a non-negative integer.")
    if not isinstance(item["price"], Decimal) or item["price"] < 0:
        raise ValueError("Item price must be a non-negative Decimal value.")


def calculate_item_value(item: InventoryItem) -> Decimal:
    """Return the monetary value of an item's available stock."""
    validate_item(item)
    return item["quantity"] * item["price"]


def calculate_total_stock_value(items: Sequence[InventoryItem]) -> Decimal:
    """Return the combined value of all valid inventory items."""
    return sum((calculate_item_value(item) for item in items), start=Decimal("0"))


def highest_stock_item(items: Sequence[InventoryItem]) -> InventoryItem | None:
    """Return the item with the greatest quantity, if one exists."""
    return max(items, key=lambda item: item["quantity"], default=None)


def lowest_stock_item(items: Sequence[InventoryItem]) -> InventoryItem | None:
    """Return the item with the smallest quantity, if one exists."""
    return min(items, key=lambda item: item["quantity"], default=None)


def low_stock_items(
    items: Sequence[InventoryItem], threshold: int = 10
) -> list[InventoryItem]:
    """Return items whose quantities are at or below the supplied threshold."""
    if threshold < 0:
        raise ValueError("Low-stock threshold cannot be negative.")
    return [item for item in items if item["quantity"] <= threshold]
