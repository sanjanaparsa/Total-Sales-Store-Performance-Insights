import pandas as pd
import numpy as np
import os

DATEID = '20240728'
directory = r"C:\Users\sanjana parsa\OneDrive\Desktop\DWBI\EndtoEndSalesProject-master\Landing Directory"  # Using raw string

# Ensure the directory exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(1, 101):  # Loop over 100 stores
    num_rows = np.random.randint(100, 1000)  # Random number of rows between 100 and 1000

    # Create a dictionary for the data to be used to create the DataFrame
    data = {
        'DateID': [DATEID] * num_rows,
        'ProductID': np.random.randint(1, 1001, size=num_rows),  # Random ProductID between 1 and 1000
        'StoreID': [i] * num_rows,  # StoreID is the same for each store in this iteration
        'CustomerID': np.random.randint(1, 1001, size=num_rows),  # Random CustomerID
        'QuantityOrdered': np.random.randint(1, 21, size=num_rows),  # Random quantity ordered between 1 and 20
        'OrderAmount': np.random.randint(100, 1001, size=num_rows),  # Random order amount between 100 and 1000
    }

    # Create DataFrame from the generated data
    df = pd.DataFrame(data)

    # Randomly generate discount and shipping cost percentages
    discount_perc = np.random.uniform(0.02, 0.15, size=num_rows)  # Discount percentage between 2% and 15%
    shipping_cost = np.random.uniform(0.05, 0.15, size=num_rows)  # Shipping cost percentage between 5% and 15%

    # Calculate dependent columns
    df['DiscountAmount'] = df['OrderAmount'] * discount_perc
    df['Shipping Cost'] = df['OrderAmount'] * shipping_cost
    df['TotalAmount'] = df['OrderAmount'] - (df['DiscountAmount'] + df['Shipping Cost'])

    # Print a preview of the data
    print(f"Store {i} Data Preview:")
    print(df.head())  # Print only the first few rows for preview
    print("\n")  # Add a newline for better readability

    # Construct the filename and file path
    file_name = f'Store_{i}_{DATEID}.csv'
    file_path = os.path.join(directory, file_name)

    # Remove existing file if it exists, then write new CSV
    if os.path.exists(file_path):
        os.remove(file_path)

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

print("All files have been generated successfully.")
