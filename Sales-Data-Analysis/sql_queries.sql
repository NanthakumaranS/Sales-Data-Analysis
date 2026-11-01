-- Sales Data Analysis: SQL practice queries
-- Import dataset/sales_data.csv into a table named sales_data first.
-- Expected columns: Order_ID, Order_Date, City, Category, Product,
-- Quantity, Unit_Price, Unit_Cost

-- 1. View all sales records
SELECT * FROM sales_data;

-- 2. Total revenue and profit
SELECT
    SUM(Quantity * Unit_Price) AS total_revenue,
    SUM(Quantity * (Unit_Price - Unit_Cost)) AS total_profit
FROM sales_data;

-- 3. Revenue and profit by category
SELECT
    Category,
    SUM(Quantity * Unit_Price) AS revenue,
    SUM(Quantity * (Unit_Price - Unit_Cost)) AS profit
FROM sales_data
GROUP BY Category
ORDER BY revenue DESC;

-- 4. Revenue by city
SELECT
    City,
    SUM(Quantity * Unit_Price) AS revenue
FROM sales_data
GROUP BY City
ORDER BY revenue DESC;

-- 5. Best-selling products by quantity
SELECT
    Product,
    SUM(Quantity) AS units_sold
FROM sales_data
GROUP BY Product
ORDER BY units_sold DESC;

-- 6. Monthly revenue (syntax works in MySQL)
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS sales_month,
    SUM(Quantity * Unit_Price) AS revenue
FROM sales_data
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY sales_month;
