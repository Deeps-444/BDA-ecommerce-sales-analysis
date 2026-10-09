-- ============================================================
-- E-COMMERCE SALES ANALYSIS USING APACHE PIG
-- ============================================================


-- ============================================================
-- 1. LOAD DATA FROM HDFS
-- ============================================================

transactions = LOAD '/ecommerce/ecommerce_transactions.csv'
USING PigStorage(',')
AS (
    order_id:chararray,
    order_date:chararray,
    customer_id:chararray,
    product_id:chararray,
    product_name:chararray,
    category:chararray,
    quantity:int,
    unit_price:double,
    city:chararray,
    state:chararray,
    payment_method:chararray,
    order_status:chararray
);


-- ============================================================
-- 2. REMOVE CSV HEADER
-- ============================================================

data = FILTER transactions BY order_id != 'order_id';


-- ============================================================
-- 3. DISPLAY SAMPLE DATA
-- ============================================================

sample_data = LIMIT data 10;

DUMP sample_data;


-- ============================================================
-- 4. FILTER DELIVERED ORDERS
-- ============================================================

delivered_orders = FILTER data
BY order_status == 'Delivered';

DUMP delivered_orders;


-- ============================================================
-- 5. CALCULATE REVENUE FOR EACH TRANSACTION
-- ============================================================

sales_data = FOREACH data GENERATE
    order_id,
    order_date,
    customer_id,
    product_id,
    product_name,
    category,
    quantity,
    unit_price,
    (quantity * unit_price) AS revenue,
    city,
    state,
    payment_method,
    order_status;


-- ============================================================
-- 6. GROUP SALES BY CATEGORY
-- ============================================================

category_group = GROUP sales_data BY category;


category_sales = FOREACH category_group GENERATE
    group AS category,
    SUM(sales_data.quantity) AS total_units,
    SUM(sales_data.revenue) AS total_sales;


-- ============================================================
-- 7. SORT CATEGORIES BY SALES
-- ============================================================

ordered_categories = ORDER category_sales
BY total_sales DESC;


DUMP ordered_categories;


-- ============================================================
-- 8. GROUP SALES BY CITY
-- ============================================================

city_group = GROUP sales_data BY city;


city_sales = FOREACH city_group GENERATE
    group AS city,
    SUM(sales_data.quantity) AS total_units,
    SUM(sales_data.revenue) AS total_sales;


-- ============================================================
-- 9. SORT CITIES BY SALES
-- ============================================================

ordered_cities = ORDER city_sales
BY total_sales DESC;


DUMP ordered_cities;


-- ============================================================
-- 10. GROUP SALES BY PAYMENT METHOD
-- ============================================================

payment_group = GROUP sales_data BY payment_method;


payment_sales = FOREACH payment_group GENERATE
    group AS payment_method,
    COUNT(sales_data) AS number_of_orders,
    SUM(sales_data.revenue) AS total_sales;


DUMP payment_sales;


-- ============================================================
-- 11. GROUP SALES BY ORDER STATUS
-- ============================================================

status_group = GROUP sales_data BY order_status;


status_analysis = FOREACH status_group GENERATE
    group AS order_status,
    COUNT(sales_data) AS number_of_orders,
    SUM(sales_data.revenue) AS total_transaction_value;


DUMP status_analysis;


-- ============================================================
-- 12. GROUP SALES BY PRODUCT
-- ============================================================

product_group = GROUP sales_data BY product_name;


product_sales = FOREACH product_group GENERATE
    group AS product_name,
    SUM(sales_data.quantity) AS units_sold,
    SUM(sales_data.revenue) AS total_sales;


-- ============================================================
-- 13. TOP PRODUCTS BY SALES
-- ============================================================

ordered_products = ORDER product_sales
BY total_sales DESC;


top_products = LIMIT ordered_products 10;


DUMP top_products;


-- ============================================================
-- END OF PIG ANALYSIS
-- ============================================================