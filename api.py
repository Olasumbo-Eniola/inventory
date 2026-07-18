"""Expose inventory records and stock calculations through FastAPI."""

from decimal import Decimal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from inventory import inventory
from models import InventoryItem
from utils.helpers import (
    calculate_item_value,
    calculate_total_stock_value,
    highest_stock_item,
    low_stock_items,
    lowest_stock_item,
)


class InventoryItemInput(BaseModel):
    """Validate data received when an inventory item is created."""

    item_name: str = Field(min_length=1)
    quantity: int = Field(ge=0)
    price: Decimal = Field(ge=0)


app = FastAPI(title="Inventory API", version="1.0.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Confirm that the service is available."""
    return {"status": "ok"}


@app.get("/inventory", tags=["inventory"])
def list_inventory() -> list[dict[str, object]]:
    """Return inventory records with their calculated stock values."""
    return [dict(item, stock_value=calculate_item_value(item)) for item in inventory]


@app.get("/inventory/summary", tags=["inventory"])
def inventory_summary(threshold: int = 10) -> dict[str, object]:
    """Return stock totals, extremes, and low-stock records."""
    if threshold < 0:
        raise HTTPException(status_code=422, detail="Threshold cannot be negative.")
    return {
        "count": len(inventory),
        "total_stock_value": calculate_total_stock_value(inventory),
        "highest_stock_item": highest_stock_item(inventory),
        "lowest_stock_item": lowest_stock_item(inventory),
        "low_stock_items": low_stock_items(inventory, threshold),
    }


@app.post("/inventory", status_code=status.HTTP_201_CREATED, tags=["inventory"])
def create_inventory_item(payload: InventoryItemInput) -> InventoryItem:
    """Create and return a validated inventory record."""
    name = payload.item_name.strip()
    if any(item["item_name"].casefold() == name.casefold() for item in inventory):
        raise HTTPException(status_code=409, detail="Inventory item already exists.")
    item: InventoryItem = {
        "item_name": name,
        "quantity": payload.quantity,
        "price": payload.price,
    }
    inventory.append(item)
    return item
