"""Inventory data used by the application."""

from decimal import Decimal

from models import InventoryItem


# Decimal values avoid the rounding errors associated with binary floats.
inventory: list[InventoryItem] = [
    {"item_name": "Laptop", "quantity": 5, "price": Decimal("450000.00")},
    {"item_name": "Keyboard", "quantity": 12, "price": Decimal("15000.00")},
    {"item_name": "Mouse", "quantity": 20, "price": Decimal("8000.00")},
    {"item_name": "Monitor", "quantity": 7, "price": Decimal("120000.00")},
    {"item_name": "USB Cable", "quantity": 30, "price": Decimal("3500.00")},
]
