# Import necessary libraries
import pandas as pd
import random
import csv
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()

# Input the number of rows you want to generate in the CSV file
num_rows = int(input("Enter the number of rows that you want to generate in the CSV file: "))

# Input the name of the CSV file (e.g., test_new_store.csv)
csv_file = input("Enter the name of the CSV file: ")

# File path and name of the Excel file with lookup data, File Path and Name, Sheet Name and column name where the data is present
excel_file_path_name = r'C:\Users\sanjana parsa\OneDrive\Desktop\DWBI\EndtoEndSalesProject-master\Lookup Data\LookupFile.xlsx'

# Excel sheet and column names for lookup data
excel_sheet_name = "Store Name Data"  # Corrected sheet name without backtick
adjective_column_name = "Adjectives"
noun_column_name = "Nouns"

# Fetch the data from the Excel file into a pandas dataframe
df = pd.read_excel(excel_file_path_name, sheet_name= excel_sheet_name)

# Print the dataframe to verify the content
print(df)


#open the csv file 

with open(csv_file,mode='w',newline='') as file:
    writer=csv.writer(file)


#create the header 
    header=['StoreName','StoreType','StoreOpeningDate','Address','City','State','Country','Region','Manager Name']


#write the header to the csv file 
    writer.writerow(header)


#loop and generate multiple rows 
    for _ in range(num_rows):

#Select a random Adjective and Noun and we are going to concatenate it with the word "The" and finally use that as our store name 
        random_adjective=df[adjective_column_name].sample(n=1).values[0]
        random_noun=df[noun_column_name].sample(n=1).values[0]
        store_name= f"The {random_adjective} {random_noun}"
        

#Generate a Single row 
        row = [
        store_name,
        random.choice(['Exclusive','MBO','SMB','Outlet Stores']),
        fake.date(),
        fake.address().replace("\n"," ").replace(","," "),
        fake.city(),
        fake.state(),
        fake.country(),
        random.choice(['North','South','East','West']),
        fake.first_name()
        ]


# write the row to the csv file 

        writer.writerow(row)


#print success statement 

print(" the process completed Successfully")