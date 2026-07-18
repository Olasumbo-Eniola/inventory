def calculate_item_value(item):
    return item["quantity"] * item["price"]


def calculate_total_stock_value(items):
    return sum(calculate_item_value(item) for item in items)


def highest_stock_item(items):
    return max(items, key=lambda item: item["quantity"], default=None)


def lowest_stock_item(items):
    return min(items, key=lambda item: item["quantity"], default=None)
