import csv
import random
from datetime import datetime, timedelta


# ============================================================
# DATASET CONFIGURATION
# ============================================================

NUM_RECORDS = 100_000

START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2026, 12, 31)

OUTPUT_FILE = "../data/raw/ecommerce_transactions.csv"

# Makes the generated dataset reproducible
random.seed(42)


# ============================================================
# PRODUCT INFORMATION
# ============================================================

products = [
    ("P001", "Wireless Mouse", "Electronics", 500, 1200),
    ("P002", "Bluetooth Headphones", "Electronics", 1200, 3500),
    ("P003", "Smart Watch", "Electronics", 1800, 6000),
    ("P004", "USB-C Charger", "Electronics", 500, 1500),
    ("P005", "Laptop Backpack", "Electronics", 1000, 3000),
    ("P006", "Mechanical Keyboard", "Electronics", 2500, 7000),

    ("P007", "Running Shoes", "Sports", 1800, 4500),
    ("P008", "Yoga Mat", "Sports", 600, 1800),
    ("P009", "Cricket Bat", "Sports", 1500, 5000),
    ("P010", "Football", "Sports", 700, 1800),

    ("P011", "Cotton Kurti", "Fashion", 600, 1500),
    ("P012", "Denim Jeans", "Fashion", 1000, 2500),
    ("P013", "Casual Shirt", "Fashion", 700, 1800),
    ("P014", "Women's Handbag", "Fashion", 1000, 3500),

    ("P015", "Bedsheet Set", "Home & Kitchen", 800, 2200),
    ("P016", "Non-Stick Cookware Set", "Home & Kitchen", 1800, 5000),
    ("P017", "Electric Kettle", "Home & Kitchen", 900, 2500),
    ("P018", "Storage Organizer", "Home & Kitchen", 400, 1500),

    ("P019", "Python Programming Book", "Books", 500, 1200),
    ("P020", "Data Science Handbook", "Books", 700, 1800),
    ("P021", "Novel Collection", "Books", 500, 1500),
    ("P022", "Business Management Book", "Books", 600, 1600),
]


# ============================================================
# CITY AND STATE INFORMATION
# ============================================================

locations = {
    "Pune": "Maharashtra",
    "Mumbai": "Maharashtra",
    "Nagpur": "Maharashtra",
    "Nashik": "Maharashtra",
    "Delhi": "Delhi",
    "Bengaluru": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Kolkata": "West Bengal",
    "Ahmedabad": "Gujarat",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh",
    "Surat": "Gujarat",
    "Indore": "Madhya Pradesh",
    "Bhopal": "Madhya Pradesh"
}


# ============================================================
# PAYMENT METHODS
# ============================================================

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "COD",
    "Wallet"
]


# ============================================================
# ORDER STATUSES
# ============================================================

order_statuses = [
    "Delivered",
    "Cancelled",
    "Returned",
    "Pending"
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def random_date(start_date, end_date):
    """
    Generate a random date between start_date and end_date.
    """

    days_difference = (end_date - start_date).days

    random_days = random.randint(0, days_difference)

    return start_date + timedelta(days=random_days)


def generate_customer_id():
    """
    Generate a random customer ID.
    """

    return f"C{random.randint(1, 10000):05d}"


def choose_product():
    """
    Select a product using popularity weights.

    Higher weight = product is more likely to be selected.
    """

    weights = [
        8,   # Wireless Mouse
        7,   # Bluetooth Headphones
        5,   # Smart Watch
        6,   # USB-C Charger
        5,   # Laptop Backpack
        3,   # Mechanical Keyboard

        6,   # Running Shoes
        5,   # Yoga Mat
        3,   # Cricket Bat
        4,   # Football

        7,   # Cotton Kurti
        6,   # Denim Jeans
        5,   # Casual Shirt
        4,   # Women's Handbag

        5,   # Bedsheet Set
        3,   # Non-Stick Cookware Set
        4,   # Electric Kettle
        5,   # Storage Organizer

        4,   # Python Programming Book
        3,   # Data Science Handbook
        5,   # Novel Collection
        3    # Business Management Book
    ]

    return random.choices(products, weights=weights, k=1)[0]


def choose_city():
    """
    Select a city based on approximate order volume.
    Larger cities receive more orders.
    """

    cities = list(locations.keys())

    weights = [
        12,  # Pune
        12,  # Mumbai
        6,   # Nagpur
        5,   # Nashik
        12,  # Delhi
        11,  # Bengaluru
        9,   # Hyderabad
        7,   # Chennai
        6,   # Kolkata
        6,   # Ahmedabad
        4,   # Jaipur
        4,   # Lucknow
        3,   # Surat
        2,   # Indore
        1    # Bhopal
    ]

    return random.choices(cities, weights=weights, k=1)[0]


def choose_payment_method():
    """
    Select payment method using realistic probabilities.
    """

    methods = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "COD",
        "Wallet"
    ]

    weights = [
        40,   # UPI
        18,   # Credit Card
        12,   # Debit Card
        8,    # Net Banking
        17,   # COD
        5     # Wallet
    ]

    return random.choices(methods, weights=weights, k=1)[0]


def choose_order_status():
    """
    Select order status using realistic probabilities.
    """

    statuses = [
        "Delivered",
        "Cancelled",
        "Returned",
        "Pending"
    ]

    weights = [
        85,   # Delivered
        5,    # Cancelled
        7,    # Returned
        3     # Pending
    ]

    return random.choices(statuses, weights=weights, k=1)[0]


def choose_quantity():
    """
    Generate an order quantity.

    Most orders contain 1-3 items.
    """

    quantities = [1, 2, 3, 4, 5]

    weights = [55, 25, 12, 6, 2]

    return random.choices(quantities, weights=weights, k=1)[0]


def get_seasonal_multiplier(order_date):
    """
    Increase sales probability during major Indian
    festive shopping months.

    October and November receive higher activity.
    """

    month = order_date.month

    if month in [10, 11]:
        return 1.5

    if month in [8, 9, 12]:
        return 1.15

    return 1.0


# ============================================================
# DATASET GENERATION
# ============================================================

def generate_dataset():

    print("Generating e-commerce transaction dataset...")
    print(f"Number of records: {NUM_RECORDS:,}")

    import os

    output_directory = os.path.dirname(OUTPUT_FILE)

    if output_directory:
        os.makedirs(output_directory, exist_ok=True)

    fieldnames = [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "city",
        "state",
        "payment_method",
        "order_status"
    ]

    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        # ----------------------------------------------------
        # Generate transactions
        # ----------------------------------------------------

        for i in range(1, NUM_RECORDS + 1):

            order_id = f"ORD{i:06d}"

            # Generate a date
            order_date = random_date(
                START_DATE,
                END_DATE
            )

            # Apply seasonal demand
            seasonal_multiplier = get_seasonal_multiplier(
                order_date
            )

            # Some generated dates are rejected and regenerated
            # according to the seasonal demand.
            if random.random() > (1 / seasonal_multiplier):

                order_date = random_date(
                    START_DATE,
                    END_DATE
                )

            customer_id = generate_customer_id()

            # Select product
            product = choose_product()

            product_id = product[0]
            product_name = product[1]
            category = product[2]
            minimum_price = product[3]
            maximum_price = product[4]

            # Generate price
            unit_price = random.randint(
                minimum_price,
                maximum_price
            )

            # Generate quantity
            quantity = choose_quantity()

            # Select location
            city = choose_city()
            state = locations[city]

            # Select payment method
            payment_method = choose_payment_method()

            # Select order status
            order_status = choose_order_status()

            # Write transaction
            writer.writerow({
                "order_id": order_id,
                "order_date": order_date.strftime("%Y-%m-%d"),
                "customer_id": customer_id,
                "product_id": product_id,
                "product_name": product_name,
                "category": category,
                "quantity": quantity,
                "unit_price": unit_price,
                "city": city,
                "state": state,
                "payment_method": payment_method,
                "order_status": order_status
            })

            if i % 10000 == 0:
                print(f"Generated {i:,} records...")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    generate_dataset()

    print()
    print("Dataset generation completed!")
    print(f"File created: {OUTPUT_FILE}")