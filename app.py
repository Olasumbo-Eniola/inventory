from inventory import inventory
from utils.helpers import (
    calculate_item_value,
    calculate_total_stock_value,
    highest_stock_item,
    lowest_stock_item,
)


def display_inventory(items):
    if not items:
        print("No inventory items available.")
        return

    print(f"{'Item':<20}{'Quantity':>10}{'Price':>15}{'Stock Value':>18}")
    print("-" * 63)

    for item in items:
        value = calculate_item_value(item)
        print(
            f"{item['item_name']:<20}"
            f"{item['quantity']:>10}"
            f"{item['price']:>15,.2f}"
            f"{value:>18,.2f}"
        )

    print("-" * 63)
    print(f"{'Total stock value:':<45}{calculate_total_stock_value(items):>18,.2f}")

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    print(f"Highest stock item: {highest['item_name']} ({highest['quantity']} units)")
    print(f"Lowest stock item: {lowest['item_name']} ({lowest['quantity']} units)")


def main():
    display_inventory(inventory)


if __name__ == "__main__":
    main()
