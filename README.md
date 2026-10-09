# 🛒 Big Data Analytics for E-Commerce Sales Trend Analysis

> **A Hadoop-based Big Data Analytics project for processing, analyzing,
> and visualizing 100,000 e-commerce transactions using HDFS, Hive, Pig,
> Python, Pandas, and Matplotlib.**

------------------------------------------------------------------------

## 📌 Project Overview

E-commerce platforms generate large volumes of transactional data
containing information about orders, customers, products, locations,
payment methods, and order statuses. Extracting meaningful business
insights from such data requires scalable storage and processing
techniques.

This project develops a complete **Big Data analytics pipeline for
e-commerce sales trend analysis**. A synthetic but realistic dataset of
**100,000 e-commerce transactions** is generated and validated using
Python, stored in **Hadoop Distributed File System (HDFS)**, and
analyzed using **Apache Hive** and **Apache Pig**. Python is then used
to transform the analytical data into visual insights.

The project focuses on answering practical business questions such as:

-   Which product categories generate the most sales?
-   Which products are the top performers?
-   How do sales change over time?
-   Which cities contribute the most sales?
-   Which payment methods are most frequently used?
-   What is the distribution of delivered, returned, cancelled, and
    pending orders?
-   Which customers and products contribute the highest transaction
    value?

------------------------------------------------------------------------

## 🎯 Aim

To design and implement a Hadoop-based Big Data Analytics system that
processes large-scale e-commerce transaction data and extracts
meaningful **sales trends, product performance patterns, customer
insights, geographical patterns, and operational insights**.

------------------------------------------------------------------------

## 🧩 Problem Statement

Traditional spreadsheet-based analysis becomes difficult to manage as
the volume of e-commerce transactions increases. A scalable analytics
pipeline is required to store, process, aggregate, and visualize large
datasets efficiently.

This project addresses the problem by combining:

**Python → HDFS → Hive/Pig → Analytics → Visualization → Business
Insights**

------------------------------------------------------------------------

## 🎯 Objectives

1.  Generate a large and realistic e-commerce transaction dataset.
2.  Validate data quality, completeness, and consistency.
3.  Store the transaction dataset in Hadoop HDFS.
4.  Create a structured Hive table over the HDFS data.
5.  Perform SQL-based analytics using HiveQL.
6.  Perform data-flow processing using Apache Pig.
7.  Apply filtering, grouping, aggregation, sorting, and transformation
    operations.
8.  Analyze product, category, customer, location, payment, and
    order-status trends.
9.  Generate meaningful visualizations using Python.
10. Demonstrate how Big Data tools can support e-commerce business
    decision-making.

------------------------------------------------------------------------

# 🏗️ System Architecture

![Alt Text](C:\BDA_Ecommerce_Project\screenshots\bda_sys_arch.png)



------------------------------------------------------------------------

# 🛠️ Technology Stack

  Layer                     Technology
  ------------------------- ---------------------
  Operating Environment     Ubuntu Linux
  Virtualization            Oracle VirtualBox
  Big Data Framework        Apache Hadoop 3.3.6
  Distributed Storage       HDFS
  SQL Analytics             Apache Hive 3.1.3
  Data Flow Processing      Apache Pig 0.17.0
  Programming Language      Python 3
  Data Processing           Pandas
  Visualization             Matplotlib
  Development Environment   Visual Studio Code
  Dataset Format            CSV

------------------------------------------------------------------------

# 📊 Dataset

The project uses a **synthetic but realistic e-commerce transaction
dataset** containing:

**100,000 transactions**

### Dataset attributes

  Attribute          Description
  ------------------ ---------------------------
  `order_id`         Unique order identifier
  `order_date`       Date of transaction
  `customer_id`      Customer identifier
  `product_id`       Product identifier
  `product_name`     Product name
  `category`         Product category
  `quantity`         Number of units purchased
  `unit_price`       Price per unit
  `city`             Customer/order city
  `state`            Customer/order state
  `payment_method`   Payment method used
  `order_status`     Current order status

### Categories

-   Electronics
-   Fashion
-   Sports
-   Home & Kitchen
-   Books

### Payment Methods

-   UPI
-   Credit Card
-   Debit Card
-   Net Banking
-   COD
-   Wallet

### Order Statuses

-   Delivered
-   Returned
-   Cancelled
-   Pending

### Dataset validation

The generated dataset was validated before Big Data processing.

``` text
Total records:        100,000
Missing values:       0
Earliest date:        2026-01-01
Latest date:          2026-12-31
Total quantity sold:  174,893
Transaction value:    ₹314,024,770
```

------------------------------------------------------------------------

# 🗂️ Project Structure

``` text
BDA_Ecommerce_Project/
│
├── data/
│   ├── raw/
│   │   └── ecommerce_transactions.csv
│   └── sample/
│
├── python/
│   ├── generate_dataset.py
│   ├── validate_dataset.py
│   └── visualize_results.py
│
├── hive/
│   ├── create_table.hql
│   ├── queries.hql
│   └── key_results.hql
│
├── pig/
│   └── sales_analysis.pig
│
├── results/
│   ├── tables/
│   └── visualizations/
│       ├── monthly_sales_trend.png
│       ├── revenue_by_category.png
│       ├── top_10_products.png
│       ├── sales_by_city.png
│       ├── payment_method_distribution.png
│       └── order_status_distribution.png
│
├── screenshots/
│
├── docs/
│
└── README.md
```

------------------------------------------------------------------------

# 🔄 Project Workflow

## 1. Dataset Generation

Python is used to generate 100,000 e-commerce transactions with
realistic combinations of:

-   Products
-   Categories
-   Customers
-   Cities
-   States
-   Quantities
-   Prices
-   Payment methods
-   Order statuses
-   Transaction dates

Run:

``` bash
python python/generate_dataset.py
```

------------------------------------------------------------------------

## 2. Dataset Validation

The generated dataset is checked for:

-   Record count
-   Missing values
-   Date range
-   Category distribution
-   City distribution
-   Payment-method distribution
-   Order-status distribution
-   Total quantity
-   Transaction value

Run:

``` bash
python python/validate_dataset.py
```

------------------------------------------------------------------------

# 🐘 Hadoop & HDFS

The dataset is transferred from the shared Windows/Ubuntu project
directory into HDFS.

### Start Hadoop

``` bash
start-dfs.sh
start-yarn.sh
```

Verify Hadoop processes:

``` bash
jps
```

Typical processes include:

``` text
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager
```

### Create HDFS directory

``` bash
hdfs dfs -mkdir /ecommerce
```

### Upload dataset

``` bash
hdfs dfs -put /media/sf_BDA_Ecommerce_Project/data/raw/ecommerce_transactions.csv /ecommerce/
```

### Verify

``` bash
hdfs dfs -ls /ecommerce
```

The transaction data is now available in HDFS for distributed
processing.

------------------------------------------------------------------------

# 🐝 Hive Analytics

Hive provides a structured SQL-like interface over the e-commerce data
stored in HDFS.

## Create database and table

The script:

``` text
hive/create_table.hql
```

creates the `ecommerce_db` database and the `ecommerce_transactions`
table.

Execute:

``` bash
hive -f /media/sf_BDA_Ecommerce_Project/hive/create_table.hql
```

## Run analytical queries

The main Hive analysis is stored in:

``` text
hive/queries.hql
```

Execute:

``` bash
hive -f /media/sf_BDA_Ecommerce_Project/hive/queries.hql
```

### Hive analyses include

-   Total transactions
-   Total quantity sold
-   Gross transaction value
-   Average order value
-   Sales by category
-   Top products
-   Monthly sales trends
-   Sales by city
-   Sales by state
-   Payment-method analysis
-   Order-status analysis
-   Unique customers
-   Top customers
-   Low-performing products
-   Category-wise order status
-   Payment method vs. order status
-   Monthly category sales

Revenue is calculated as:

``` text
Revenue = Quantity × Unit Price
```

Hive queries are executed through the Hadoop processing environment,
demonstrating Big Data processing over the HDFS dataset.

------------------------------------------------------------------------

# 🐷 Apache Pig Analytics

Apache Pig is used to demonstrate data-flow based Big Data processing
using Pig Latin.

The main script is:

``` text
pig/sales_analysis.pig
```

Execute:

``` bash
pig -x mapreduce /media/sf_BDA_Ecommerce_Project/pig/sales_analysis.pig
```

### Pig operations demonstrated

``` text
LOAD
FILTER
FOREACH
GROUP
SUM
COUNT
ORDER
LIMIT
DUMP
```

### Pig analyses include

-   Loading the HDFS dataset
-   Removing the CSV header
-   Filtering delivered orders
-   Calculating transaction revenue
-   Category-wise sales
-   City-wise sales
-   Payment-method analysis
-   Order-status analysis
-   Product-wise sales
-   Top products by revenue

The Pig pipeline demonstrates how the same e-commerce dataset can be
processed using a data-flow programming model.

------------------------------------------------------------------------

# 📈 Data Visualization

Python, Pandas, and Matplotlib are used to create visual representations
of the e-commerce analytics.

Run:

``` bash
python python/visualize_results.py
```

Generated visualizations:

### 1. Monthly Sales Trend

Shows how transaction value changes across the twelve months of 2026.

### 2. Revenue by Category

Compares the contribution of each product category.

### 3. Top 10 Products by Revenue

Identifies the products generating the highest transaction value.

### 4. Sales by City

Shows geographical differences in transaction value.

### 5. Payment Method Distribution

Shows the number of orders associated with each payment method.

### 6. Order Status Distribution

Shows the distribution of delivered, returned, cancelled, and pending
orders.

All visualizations are stored under:

``` text
results/visualizations/
```

------------------------------------------------------------------------

# 💡 Business Insights

The project enables an e-commerce business to identify:

### Product Performance

Identify high-performing and low-performing products based on sales
value and units sold.

### Category Performance

Compare product categories and determine which categories contribute
most to overall transaction value.

### Temporal Trends

Analyze monthly changes in sales and identify periods of higher or lower
demand.

### Geographical Trends

Identify cities and states contributing significantly to sales.

### Customer Behavior

Analyze unique customers and identify high-value customers.

### Payment Preferences

Understand which payment methods are most frequently used.

### Operational Performance

Analyze delivered, returned, cancelled, and pending orders.

These insights can support decisions related to:

-   Inventory planning
-   Product promotions
-   Regional marketing
-   Payment optimization
-   Sales strategy
-   Product assortment
-   Operational improvement

------------------------------------------------------------------------

# 🧪 Big Data Concepts Demonstrated

This project demonstrates practical use of:

-   Distributed storage using HDFS
-   Hadoop ecosystem components
-   NameNode and DataNode architecture
-   YARN resource management
-   MapReduce-based execution
-   Hive data warehousing
-   HiveQL analytical queries
-   Apache Pig data-flow processing
-   Filtering and transformation
-   Grouping and aggregation
-   Sorting and ranking
-   Large-scale dataset validation
-   Data visualization
-   Business-oriented Big Data analytics

------------------------------------------------------------------------

# 🔁 End-to-End Execution Flow

``` text
1. Generate Dataset
        ↓
2. Validate Dataset
        ↓
3. Start Hadoop
        ↓
4. Create HDFS Directory
        ↓
5. Upload CSV to HDFS
        ↓
6. Create Hive Database & Table
        ↓
7. Execute Hive Analytics
        ↓
8. Execute Pig Analytics
        ↓
9. Generate Python Visualizations
        ↓
10. Interpret Business Insights
```

------------------------------------------------------------------------

# ▶️ Quick Start

### Windows

Generate and validate the dataset:

``` powershell
cd C:\BDA_Ecommerce_Project

python python/generate_dataset.py
python python/validate_dataset.py
```

Generate visualizations:

``` powershell
python python/visualize_results.py
```

### Ubuntu / Hadoop

Start Hadoop:

``` bash
start-dfs.sh
start-yarn.sh
```

Verify:

``` bash
jps
```

Create HDFS directory:

``` bash
hdfs dfs -mkdir /ecommerce
```

Upload dataset:

``` bash
hdfs dfs -put /media/sf_BDA_Ecommerce_Project/data/raw/ecommerce_transactions.csv /ecommerce/
```

Verify:

``` bash
hdfs dfs -ls /ecommerce
```

Run Hive:

``` bash
hive -f /media/sf_BDA_Ecommerce_Project/hive/create_table.hql
hive -f /media/sf_BDA_Ecommerce_Project/hive/queries.hql
```

Run Pig:

``` bash
pig -x mapreduce /media/sf_BDA_Ecommerce_Project/pig/sales_analysis.pig
```

------------------------------------------------------------------------

# 🖥️ Development Environment

The project uses a hybrid development workflow:

``` text
Windows
│
├── VS Code
├── Python
├── Dataset generation
├── Dataset validation
├── Visualization
└── Project documentation
        │
        │ VirtualBox Shared Folder
        ▼
Ubuntu VM
│
├── Hadoop
├── HDFS
├── YARN
├── Hive
└── Pig
```

The Windows project directory is shared with the Ubuntu virtual machine
through a VirtualBox shared folder. This allows the same project files
to be edited from VS Code and executed inside the Hadoop environment.

------------------------------------------------------------------------

# 📚 Project Learning Outcomes

By completing this project, the following practical skills are
demonstrated:

-   Setting up and working with Hadoop in a virtualized Linux
    environment
-   Managing files using HDFS
-   Understanding Hadoop services and YARN
-   Creating Hive databases and tables
-   Writing HiveQL analytical queries
-   Performing aggregation and grouping over large datasets
-   Writing Pig Latin data-processing pipelines
-   Running Pig using Hadoop MapReduce
-   Connecting Big Data processing with Python-based visualization
-   Converting analytical results into business insights

------------------------------------------------------------------------

# 🚀 Future Scope

The current system focuses on batch-oriented e-commerce sales analytics.
It can be extended with:

-   Apache Spark for faster large-scale processing
-   Kafka for real-time transaction streaming
-   Real-time fraud detection
-   Customer segmentation
-   Product recommendation systems
-   Sales forecasting using machine learning
-   Demand prediction
-   Anomaly detection
-   Interactive dashboards using Power BI, Tableau, or Streamlit
-   Cloud-based Hadoop/Spark deployment

------------------------------------------------------------------------

# 📌 Limitations

-   The current dataset is synthetic rather than collected from a live
    e-commerce platform.
-   The analysis is primarily batch-oriented.
-   No real-time streaming pipeline is implemented.
-   Predictive machine learning is outside the current project scope.
-   Results represent the generated dataset and should not be
    interpreted as actual market statistics.

------------------------------------------------------------------------

# 👩‍💻 Project

**Project:** Big Data Analytics for E-Commerce Sales Trend Analysis and
Business Insights

**Domain:** Big Data Analytics / E-Commerce

**Primary Technologies:** Hadoop, HDFS, Hive, Pig, Python

**Dataset Size:** 100,000 transactions

**Processing Approach:** Batch Analytics

------------------------------------------------------------------------

## ⭐ Summary

This project demonstrates an end-to-end Big Data analytics workflow for
e-commerce transactions:

> **Generate → Validate → Store → Process → Analyze → Visualize →
> Interpret**

By combining **Hadoop HDFS, Hive, Apache Pig, Python, Pandas, and
Matplotlib**, the project transforms a large transaction dataset into
structured analytical results and business-oriented insights.

The project provides a practical demonstration of how the Hadoop
ecosystem can be used to move from **raw transactional data to
actionable information**.
