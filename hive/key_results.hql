USE ecommerce_db;


-- ============================================================
-- 1. OVERALL BUSINESS METRICS
-- ============================================================

SELECT
    COUNT(*) AS total_transactions,
    SUM(quantity) AS total_quantity_sold,
    SUM(quantity * unit_price) AS gross_transaction_value,
    SUM(quantity * unit_price) / COUNT(DISTINCT order_id)
        AS average_order_value,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM ecommerce_transactions;


-- ============================================================
-- 2. SALES BY CATEGORY
-- ============================================================

SELECT
    category,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS units_sold,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY category
ORDER BY total_sales DESC;


-- ============================================================
-- 3. MONTHLY SALES TREND
-- ============================================================

SELECT
    date_format(order_date, 'yyyy-MM') AS month,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS units_sold,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY date_format(order_date, 'yyyy-MM')
ORDER BY month;


-- ============================================================
-- 4. TOP 10 PRODUCTS
-- ============================================================

SELECT
    product_id,
    product_name,
    category,
    SUM(quantity) AS units_sold,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY
    product_id,
    product_name,
    category
ORDER BY total_sales DESC
LIMIT 10;


-- ============================================================
-- 5. SALES BY CITY
-- ============================================================

SELECT
    city,
    state,
    COUNT(*) AS number_of_orders,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY
    city,
    state
ORDER BY total_sales DESC;


-- ============================================================
-- 6. PAYMENT METHOD ANALYSIS
-- ============================================================

SELECT
    payment_method,
    COUNT(*) AS number_of_orders,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY payment_method
ORDER BY number_of_orders DESC;


-- ============================================================
-- 7. ORDER STATUS ANALYSIS
-- ============================================================

SELECT
    order_status,
    COUNT(*) AS number_of_orders,
    SUM(quantity * unit_price) AS transaction_value
FROM ecommerce_transactions
GROUP BY order_status
ORDER BY number_of_orders DESC;