# SEN 401 Lab 3: Inventory Stock Value

This Python application stores inventory items and calculates the total value
of all stock. It also identifies the items with the highest and lowest stock
quantities.

## Project Structure

```text
sen_401_lab_3/
├── app.py
├── inventory.py
├── models.py
├── requirements.txt
├── README.md
└── utils/
    ├── __init__.py
    └── helpers.py
```

- `inventory.py` contains the inventory records.
- `models.py` defines the shared inventory item structure.
- `app.py` displays the inventory and its total stock value.
- `utils/helpers.py` contains reusable inventory calculations.
- `requirements.txt` lists the project's dependencies.

Each inventory record has an `item_name`, `quantity`, and `price`. Prices use
Python's `Decimal` type for accurate monetary calculations. An item's stock
value is its quantity multiplied by its price.

## Maintenance Changes

- **Corrective:** validates names, quantities, and prices and uses `Decimal` to
  prevent invalid values and floating-point rounding errors.
- **Adaptive:** adds a configurable low-stock alert as a new feature.
- **Perfective:** improves the report heading, alignment, naira currency
  formatting, and summary labels.
- **Preventive:** adds shared types, type hints, docstrings, focused comments,
  constants, and reusable validation helpers.

## Requirements

- Python 3.9 or newer
- No third-party packages

## Run the Application

From the project folder, run:

```bash
python3 app.py
```

## FastAPI

Install dependencies and start the API:

```bash
python3 -m pip install -r requirements.txt
uvicorn api:app --reload --port 8001
```

Open `http://localhost:8001/docs` for the interactive API documentation.
Available routes are `GET /health`, `GET /inventory`,
`GET /inventory/summary`, and `POST /inventory`.

The application prints an inventory table, the total stock value, the items
with the highest and lowest quantities, and a low-stock alert for items with
10 units or fewer. Change `LOW_STOCK_THRESHOLD` in `app.py` to use a different
limit.
