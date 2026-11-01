# Sales Data Analysis Using Python and SQL

## Project overview
This beginner-friendly data analytics project studies a sample retail sales dataset. It uses Python (Pandas and Matplotlib) to clean data, calculate business metrics, summarize sales, and create charts. It also includes SQL queries for common business questions.

## Objectives
- Clean and prepare sales data.
- Calculate revenue, cost, and profit.
- Compare performance by product category and city.
- Review monthly revenue.
- Export analysis summaries and charts.

## Tools
- Python 3
- Pandas
- Matplotlib
- SQL (MySQL-compatible examples)

## Project structure
```text
Sales-Data-Analysis/
├── dataset/
│   └── sales_data.csv
├── notebooks/
│   └── sales_analysis.py
├── reports/
├── images/
├── sql_queries.sql
├── requirements.txt
└── README.md
```

## How to run
1. Install Python 3.
2. Open Command Prompt or a terminal in this project folder.
3. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the analysis:
   ```bash
   python notebooks/sales_analysis.py
   ```
5. Open the `reports/` folder to see the CSV summaries and PNG charts.

## Metrics
- Revenue = Quantity × Unit Price
- Total Cost = Quantity × Unit Cost
- Profit = Revenue − Total Cost

## Dataset
The included CSV is a small sample dataset created for learning and demonstration. It is not real customer or company data.

## SQL practice
See [`sql_queries.sql`](sql_queries.sql) for queries to calculate revenue, profit, category performance, city performance, and best-selling products.

## Future improvements
- Connect the analysis to a real database.
- Build an interactive Power BI dashboard.
- Add filters and more detailed KPIs.
- Test the workflow with a larger real-world dataset.

## Author
Add your name and portfolio links here.
