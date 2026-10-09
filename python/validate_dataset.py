import csv
from collections import Counter
from datetime import datetime


FILE_PATH = "../data/raw/ecommerce_transactions.csv"


def validate_dataset():

    print("=" * 60)
    print("E-COMMERCE DATASET VALIDATION")
    print("=" * 60)

    with open(
        FILE_PATH,
        mode="r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        rows = list(reader)

    # --------------------------------------------------------
    # Basic information
    # --------------------------------------------------------

    print(f"\nTotal records: {len(rows):,}")

    print("\nColumns:")
    for column in reader.fieldnames:
        print(f"  - {column}")

    # --------------------------------------------------------
    # Missing values
    # --------------------------------------------------------

    print("\nMissing values:")

    missing_values = {}

    for column in reader.fieldnames:

        missing_count = sum(
            1 for row in rows
            if not row[column].strip()
        )

        missing_values[column] = missing_count

        print(
            f"  {column}: {missing_count}"
        )

    # --------------------------------------------------------
    # Date validation
    # --------------------------------------------------------

    dates = [
        datetime.strptime(
            row["order_date"],
            "%Y-%m-%d"
        )
        for row in rows
    ]

    print("\nDate range:")
    print(f"  Earliest: {min(dates).date()}")
    print(f"  Latest:   {max(dates).date()}")

    # --------------------------------------------------------
    # Categories
    # --------------------------------------------------------

    categories = Counter(
        row["category"]
        for row in rows
    )

    print("\nCategories:")

    for category, count in categories.items():
        print(f"  {category}: {count:,}")

    # --------------------------------------------------------
    # Cities
    # --------------------------------------------------------

    cities = Counter(
        row["city"]
        for row in rows
    )

    print("\nTop 10 cities by orders:")

    for city, count in cities.most_common(10):
        print(f"  {city}: {count:,}")

    # --------------------------------------------------------
    # Payment methods
    # --------------------------------------------------------

    payments = Counter(
        row["payment_method"]
        for row in rows
    )

    print("\nPayment methods:")

    for method, count in payments.items():
        print(f"  {method}: {count:,}")

    # --------------------------------------------------------
    # Order statuses
    # --------------------------------------------------------

    statuses = Counter(
        row["order_status"]
        for row in rows
    )

    print("\nOrder statuses:")

    for status, count in statuses.items():
        print(f"  {status}: {count:,}")

    # --------------------------------------------------------
    # Revenue calculation
    # --------------------------------------------------------

    total_revenue = sum(
        int(row["quantity"]) * int(row["unit_price"])
        for row in rows
    )

    total_quantity = sum(
        int(row["quantity"])
        for row in rows
    )

    print("\nBasic metrics:")
    print(f"  Total quantity sold: {total_quantity:,}")
    print(f"  Total revenue: ₹{total_revenue:,.2f}")

    # --------------------------------------------------------
    # Sample records
    # --------------------------------------------------------

    print("\nFirst 5 records:")

    for row in rows[:5]:
        print(row)

    # --------------------------------------------------------
    # Final result
    # --------------------------------------------------------

    print("\n" + "=" * 60)

    if len(rows) == 100_000:
        print("✓ Record count is correct.")
    else:
        print("✗ Record count is NOT 100,000.")

    if all(
        count == 0
        for count in missing_values.values()
    ):
        print("✓ No missing values found.")
    else:
        print("✗ Missing values found.")

    print("=" * 60)


if __name__ == "__main__":
    validate_dataset()