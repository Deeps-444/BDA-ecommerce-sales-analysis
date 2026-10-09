-- ============================================================
-- E-COMMERCE SALES ANALYTICS
-- Complete Hive Analysis Script
-- ============================================================


-- ============================================================
-- 1. SELECT DATABASE
-- ============================================================

USE ecommerce_db;


-- ============================================================
-- 2. BASIC DATA VALIDATION
-- ============================================================

-- Count total transactions
SELECT
    COUNT(*) AS total_transactions
FROM ecommerce_transactions;


-- Display sample transactions
SELECT *
FROM ecommerce_transactions
LIMIT 10;


-- ============================================================
-- 3. OVERALL SALES METRICS
-- ============================================================

-- Gross transaction value
-- Revenue = quantity × unit_price

SELECT
    SUM(quantity * unit_price) AS gross_transaction_value
FROM ecommerce_transactions;


-- Total quantity of products sold

SELECT
    SUM(quantity) AS total_quantity_sold
FROM ecommerce_transactions;


-- Average Order Value

SELECT
    SUM(quantity * unit_price) / COUNT(DISTINCT order_id)
        AS average_order_value
FROM ecommerce_transactions;


-- ============================================================
-- 4. SALES BY CATEGORY
-- ============================================================

SELECT
    category,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY category
ORDER BY total_sales DESC;


-- ============================================================
-- 5. TOP 10 PRODUCTS BY SALES
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
-- 6. TOP 10 PRODUCTS BY QUANTITY SOLD
-- ============================================================

SELECT
    product_id,
    product_name,
    category,
    SUM(quantity) AS units_sold
FROM ecommerce_transactions
GROUP BY
    product_id,
    product_name,
    category
ORDER BY units_sold DESC
LIMIT 10;


-- ============================================================
-- 7. MONTHLY SALES TREND
-- ============================================================

SELECT
    date_format(order_date, 'yyyy-MM') AS month,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY date_format(order_date, 'yyyy-MM')
ORDER BY month;


-- ============================================================
-- 8. SALES BY CITY
-- ============================================================

SELECT
    city,
    state,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY
    city,
    state
ORDER BY total_sales DESC;


-- ============================================================
-- 9. SALES BY STATE
-- ============================================================

SELECT
    state,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY state
ORDER BY total_sales DESC;


-- ============================================================
-- 10. PAYMENT METHOD ANALYSIS
-- ============================================================

SELECT
    payment_method,
    COUNT(*) AS number_of_orders,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY payment_method
ORDER BY number_of_orders DESC;


-- ============================================================
-- 11. ORDER STATUS ANALYSIS
-- ============================================================

SELECT
    order_status,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_transaction_value
FROM ecommerce_transactions
GROUP BY order_status
ORDER BY number_of_orders DESC;


-- ============================================================
-- 12. CUSTOMER ANALYSIS
-- ============================================================

-- Number of unique customers

SELECT
    COUNT(DISTINCT customer_id) AS unique_customers
FROM ecommerce_transactions;


-- Top 10 customers by transaction value

SELECT
    customer_id,
    COUNT(*) AS number_of_orders,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_spending
FROM ecommerce_transactions
GROUP BY customer_id
ORDER BY total_spending DESC
LIMIT 10;


-- ============================================================
-- 13. LOW-PERFORMING PRODUCTS
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
ORDER BY total_sales ASC
LIMIT 10;


-- ============================================================
-- 14. CATEGORY-WISE ORDER STATUS
-- ============================================================

SELECT
    category,
    order_status,
    COUNT(*) AS number_of_orders
FROM ecommerce_transactions
GROUP BY
    category,
    order_status
ORDER BY
    category,
    number_of_orders DESC;


-- ============================================================
-- 15. PAYMENT METHOD BY ORDER STATUS
-- ============================================================

SELECT
    payment_method,
    order_status,
    COUNT(*) AS number_of_orders
FROM ecommerce_transactions
GROUP BY
    payment_method,
    order_status
ORDER BY
    payment_method,
    number_of_orders DESC;


-- ============================================================
-- 16. MONTHLY CATEGORY SALES
-- ============================================================

SELECT
    date_format(order_date, 'yyyy-MM') AS month,
    category,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY
    date_format(order_date, 'yyyy-MM'),
    category
ORDER BY
    month,
    total_sales DESC;


-- ============================================================
-- 17. TOP CITY WITHIN EACH STATE
-- ============================================================

SELECT
    state,
    city,
    COUNT(*) AS number_of_orders,
    SUM(quantity * unit_price) AS total_sales
FROM ecommerce_transactions
GROUP BY
    state,
    city
ORDER BY
    state,
    total_sales DESC;


-- ============================================================
-- END OF E-COMMERCE HIVE ANALYSIS
-- ============================================================