import mysql.connector
import pandas as pd

# MySQL database connection details
username = 'root'  # Replace with your MySQL username
password = 'root'  # Replace with your MySQL password
host = 'localhost'          # Replace with your MySQL host, e.g., localhost or an IP address
port = '3306'               # Default MySQL port is 3306
database = 'dwbi'  # Replace with your database name

# Establish connection
connection = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    port=port,
    database=database
)

# Define your SQL query
query = "SELECT * FROM DimLoyalty"  # Replace with your SQL query

# Execute the query and load data into a pandas DataFrame
df = pd.read_sql(query, con=connection)

# Display the DataFrame
print(df)

# Close the connection
connection.close()
