#import python libraries 
import csv
import random 
from faker import Faker


#Initialize 

fake=Faker()

#input the number of rows that the csv file should have 

num_rows=int(input(" Enter the number of rows the csv file should have : "))


#input the name of the csv file (e.g data.csv)

csv_file = input ( " enter the name of the csv file like data.csv : ")



#open the csv file 
with open(csv_file,mode='w',newline='') as file:
    writer=csv.writer(file)

#create the header 
    header = ['First Name','Last Name','Gender','DateOfBirth', 'Email', 'Phone Number', 'Address', 'City', 'State', 'Postal Code', 'Country','LoyaltyProgramID']

#write the header to the csv file 
    writer.writerow(header)

#loop and generate multiple rows 
    for _ in range(num_rows):
        row=[
            fake.first_name(),
            fake.last_name(),
            random.choice(['M','F','Others','Not Specified']),
            fake.date(),
            fake.email(),
            fake.phone_number(),
            fake.address().replace(","," ").replace("\n"," "),
            fake.city(),
            fake.state(),
            fake.postcode(),
            fake.country(),
            random.randint(1,5)
        ]

        writer.writerow(row)

#Generate a Single row 


# write the row to the csv file 


#print success statement 

print(" the file has been loaded successfully") 