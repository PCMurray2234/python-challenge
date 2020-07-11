#PyBank
import os
import csv

# Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set Path For File
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader= csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate Total Number Months, P and L , Set row variables
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = [row[0]]
    
    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Months 
        total_months += 1
        # Calculate  "Profit/Losses" 
        net_amount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
<<<<<<< HEAD
print(f"Financial Analysis")
print(f"---------------------------")
=======
print("Financial Analysis")
print("---------------------------")
>>>>>>> 2f1e221bbb68fca6a456a9586d942cd38f41e921
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Specify File To Write To
output_file = os.path.join('Resources','analysis.txt')

# Open File Using "Write" Mode. 
f = open(output_file, "w")

# Write New Data
<<<<<<< HEAD
f.write(f"Financial Analysis\n")
f.write(f"---------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: ${net_amount}\n")
f.write(f"Average Change: ${average_change}\n")
f.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
f.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")

f.close()

# People I read and took ideas and pieces of code from for both PyPoll and PyBank:
# bigbluey, AllenRayC, blueskiesatx, 
# # https://stackoverflow.com/questions/42847440/in-python-writing-to-a-text-file-not-working In Python, writing to a text file not working
# Kahn Acaddemy \ Philip Guo, Python Tutor and Writer
# YK Sugishita \ CS Dojo
=======
f.write("Financial Analysis\n")
f.write("---------------------------\n")
f.write("Total Months: {total_months}\n")
f.write("Total: ${net_amount}\n")
f.write("Average Change: ${average_change}\n")
f.write("Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
f.write("Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")

f.close()
>>>>>>> 2f1e221bbb68fca6a456a9586d942cd38f41e921
