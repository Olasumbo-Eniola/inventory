"""Display an inventory value report in the console."""

from collections.abc import Sequence

from inventory import inventory
from models import InventoryItem
from utils.helpers import (
    calculate_item_value,
    calculate_total_stock_value,
    highest_stock_item,
    low_stock_items,
    lowest_stock_item,
)

TABLE_WIDTH = 67
LOW_STOCK_THRESHOLD = 10


def format_currency(amount: object) -> str:
    """Format a monetary value in Nigerian naira."""
    return f"₦{amount:,.2f}"


def display_inventory(items: Sequence[InventoryItem]) -> None:
    """Print the inventory table and a concise stock summary."""
    if not items:
        print("No inventory items available.")
        return

    print("INVENTORY STOCK REPORT".center(TABLE_WIDTH))
    print("=" * TABLE_WIDTH)
    print(f"{'Item':<20}{'Quantity':>10}{'Unit Price':>17}{'Stock Value':>20}")
    print("-" * TABLE_WIDTH)

    for item in items:
        value = calculate_item_value(item)
        print(
            f"{item['item_name']:<20}"
            f"{item['quantity']:>10}"
            f"{format_currency(item['price']):>17}"
            f"{format_currency(value):>20}"
        )

    print("-" * TABLE_WIDTH)
    total = calculate_total_stock_value(items)
    print(f"{'Total stock value:':<47}{format_currency(total):>20}")

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    if highest is not None and lowest is not None:
        print(f"Highest stock: {highest['item_name']} ({highest['quantity']} units)")
        print(f"Lowest stock:  {lowest['item_name']} ({lowest['quantity']} units)")

    low_items = low_stock_items(items, LOW_STOCK_THRESHOLD)
    if low_items:
        names = ", ".join(item["item_name"] for item in low_items)
        print(f"Low-stock alert (≤ {LOW_STOCK_THRESHOLD} units): {names}")


def main() -> None:
    """Run the inventory report."""
    display_inventory(inventory)


if __name__ == "__main__":
    main()
