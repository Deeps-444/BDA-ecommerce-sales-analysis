-- ============================================================
-- E-COMMERCE SALES ANALYTICS
-- Hive Table Creation
-- ============================================================

CREATE DATABASE IF NOT EXISTS ecommerce_db;

USE ecommerce_db;


-- ------------------------------------------------------------
-- Create external table
-- ------------------------------------------------------------

CREATE EXTERNAL TABLE IF NOT EXISTS ecommerce_transactions (
    order_id STRING,
    order_date DATE,
    customer_id STRING,
    product_id STRING,
    product_name STRING,
    category STRING,
    quantity INT,
    unit_price DOUBLE,
    city STRING,
    state STRING,
    payment_method STRING,
    order_status STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/ecommerce'
TBLPROPERTIES (
    'skip.header.line.count' = '1'
);


-- ------------------------------------------------------------
-- Display table structure
-- ------------------------------------------------------------

DESCRIBE ecommerce_transactions;