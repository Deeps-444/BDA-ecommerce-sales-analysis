import os

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_FILE = "../data/raw/ecommerce_transactions.csv"

OUTPUT_DIRECTORY = "../results/visualizations"

os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)


# ============================================================
# LOAD DATA
# ============================================================

print("Loading e-commerce dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Records loaded: {len(df):,}")


# ============================================================
# DATA PREPARATION
# ============================================================

df["order_date"] = pd.to_datetime(df["order_date"])

# Calculate transaction value
df["revenue"] = df["quantity"] * df["unit_price"]

print("Data preparation completed.")


# ============================================================
# 1. MONTHLY SALES TREND
# ============================================================

monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly E-Commerce Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Value")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIRECTORY}/monthly_sales_trend.png",
    dpi=300
)

plt.close()

print("Created: monthly_sales_trend.png")


# ============================================================
# 2. REVENUE BY CATEGORY
# ============================================================

category_sales = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIRECTORY}/revenue_by_category.png",
    dpi=300
)

plt.close()

print("Created: revenue_by_category.png")


# ============================================================
# 3. TOP 10 PRODUCTS
# ============================================================

top_products = (
    df.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIRECTORY}/top_10_products.png",
    dpi=300
)

plt.close()

print("Created: top_10_products.png")


# ============================================================
# 4. SALES BY CITY
# ============================================================

city_sales = (
    df.groupby("city")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(11, 6))

plt.bar(
    city_sales.index,
    city_sales.values
)

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Revenue")

plt.xticks(rotation=60)
plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIRECTORY}/sales_by_city.png",
    dpi=300
)

plt.close()

print("Created: sales_by_city.png")


# ============================================================
# 5. PAYMENT METHOD DISTRIBUTION
# ============================================================

payment_counts = (
    df["payment_method"]
    .value_counts()
)

plt.figure(figsize=(9, 6))

plt.bar(
    payment_counts.index,
    payment_counts.values
)

plt.title("Orders by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIRECTORY}/payment_method_distribution.png",
    dpi=300
)

plt.close()

print("Created: payment_method_distribution.png")


# ============================================================
# 6. ORDER STATUS DISTRIBUTION
# ============================================================

status_counts = (
    df["order_status"]
    .value_counts()
)

plt.figure(figsize=(8, 6))

plt.bar(
    status_counts.index,
    status_counts.values
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIRECTORY}/order_status_distribution.png",
    dpi=300
)

plt.close()

print("Created: order_status_distribution.png")


# ============================================================
# FINAL SUMMARY
# ============================================================

print()
print("=" * 60)
print("VISUALIZATION COMPLETED")
print("=" * 60)

print(f"Charts saved in:")
print(OUTPUT_DIRECTORY)

print()
print("Generated files:")

for filename in sorted(os.listdir(OUTPUT_DIRECTORY)):
    print(f"  - {filename}")

print("=" * 60)