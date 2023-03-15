import csv
import os

csvpath = os.path.join('onedrive', 'Data Science', 'Resources', 'Module_3', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

total_months = 0
net_total = 0 
change_total = 0 
previous_month = 0 
greatest_increase = 0 
greatest_increase_month = ""
greatest_decrease = 0 
greatest_decrease_month = ""

with open (csvpath, newline = " ") as csvfile:
csvreader = csv.reader(csvfile, delimiter = ",")

csv_header = next(csvreader)

total_months = total_months + 1 

net_total = net_total + int(newline = [1])

change = int(newline = [1]) - previous_month
change_total = change_total + change
previous_month = int(newline = [1])

greatest_increase = change 
greatest_increase_month = newline = [0]

greatest_decrease = change 
greatest_decrease_month = 0 

average_change = change_total/total_months

print("Financial Analysis")
print ("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Losses: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")