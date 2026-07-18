# SEN 401 Lab 3: Inventory Stock Value

This Python application stores inventory items and calculates the total value
of all stock. It also identifies the items with the highest and lowest stock
quantities.

## Project Structure

```text
sen_401_lab_3/
├── app.py
├── inventory.py
├── requirements.txt
├── README.md
└── utils/
    ├── __init__.py
    └── helpers.py
```

- `inventory.py` contains the inventory records.
- `app.py` displays the inventory and its total stock value.
- `utils/helpers.py` contains reusable inventory calculations.
- `requirements.txt` lists the project's dependencies.

Each inventory record has an `item_name`, `quantity`, and `price`. An item's
stock value is its quantity multiplied by its price.

## Requirements

- Python 3.9 or newer
- No third-party packages

## Run the Application

From the project folder, run:

```bash
python3 app.py
```

The application prints an inventory table, the total stock value, and the
items with the highest and lowest quantities.
