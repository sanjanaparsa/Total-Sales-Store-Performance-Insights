# End-to-End DWBI Project: Real-Life Data Integration with Snowflake, Python, SQL & Sigma


#  Project Overview
This project demonstrates a complete Data Warehouse and Business Intelligence (DWBI) solution, showcasing real-world data integration and analytics practices. The solution involves the extraction, transformation, and loading (ETL) of data from an Oracle database using Python, followed by its integration into Snowflake, where it is modeled using a Star Schema. The project then performs analytical queries using SQL and visualizes the results through Sigma and PowerBI.

By simulating a business scenario with 10 years of historical data, including customer transactions, store operations, product information, and loyalty programs, this project provides a comprehensive learning experience for anyone interested in the modern data stack and business intelligence.

#  Dataset & Tools

The dataset for this project includes:

1. Sales transactions data including customer details, product purchases, and transaction amounts.
2. Store Operations: Data about store locations, types, and performance metrics.
3. Product Information: Information on products, categories, brands, and pricing.
4. Customer Loyalty Programs: Data related to customer engagement and loyalty program membership.
The dataset simulates a real-world business environment with 10 years of historical data.




#  Tools and Technologies Used
Python: For data extraction, transformation, and loading (ETL), and data generation using Pandas.

Snowflake: Cloud data warehouse to store and process large datasets.

SQL: For querying and analyzing data stored in Snowflake.

Sigma: Cloud-based Business Intelligence tool for creating interactive dashboards and visualizations.

PowerBI: Used to create an alternative dashboard with KPIs and detailed insights.

SnowSQL: Command-line interface for managing Snowflake databases and loading data.



# Project Walkthrough
Step 1: Data Extraction & Generation
Data is first extracted from an Oracle database using Python and loaded into Snowflake.
In the absence of real-world data, synthetic data is generated using Python and Pandas.
This data includes customer transaction records, store operational data, product details, and loyalty program information.

Step 2: Snowflake Database Setup & Data Modeling
A Snowflake database is configured to store the data efficiently.
Star Schema is used for data modeling, where dimensions such as customers, stores, products, and dates are related to a central Fact Table (e.g., FACTORDERS).
SnowSQL is used to load data into Snowflake tables.


Step 3: Data Analysis Using SQL
Over 25+ analytical SQL queries are written to derive insights from the data, such as total sales, revenue per store, and customer segmentation.

Step 4: Interactive Dashboards
Sigma is used to create a Sales Performance Dashboard with interactive visualizations.
Key metrics are displayed in Key Metric Cards (KPIs) such as total sales, customer count, average order value, and sales by store type.
PowerBI is also used to create a comprehensive dashboard showcasing similar KPIs and detailed performance insights.
# Snapshot of Dashboard

Dashboard created using Sigma and PowerBI, providing key performance insights such as sales trends, store performance, and customer behavior.

![WhatsApp Image 2025-01-05 at 12 34 44 PM](https://github.com/user-attachments/assets/19a6884d-ecaa-40a4-a2a4-cacc3dc63917)



# Key Insights and Outcomes
Sales Performance:                                Total sales trends, segmented by time periods (daily, monthly, quarterly), store type, and region.

Customer Insights: Analysis of customer behavior and loyalty program engagement.

Store Performance: Store-specific performance, helping understand which store types or regions perform better in terms of sales, revenue, and average order value.

Product Insights: Categorization and analysis of 
product sales to identify top-performing categories and products.

Loyalty Program: The performance of customers enrolled in loyalty programs vs. non-loyalty program customers.


# Conclusion
This project serves as a comprehensive end-to-end example of modern data integration and business intelligence. It provides hands-on experience with data extraction, cloud data warehousing, ETL processing, SQL analysis, and visualization using Sigma and PowerBI. By simulating a real-world business context, it showcases how to create a fully functional BI solution that integrates data from multiple sources, models it for easy reporting, and provides insights through interactive dashboards. This project is ideal for anyone looking to learn about the modern data stack and business intelligence workflows.




