import os
import csv
from pathlib import Path 
path_1 = os.getcwd()
print(path_1)
csvpath = Path("/Users/evinskibenjamin/python-homework/PyBank/budget_data.csv")

total_months= 0
total_PnL= 0
value = 0
change = 0
dates = []
profits = []
line=0
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    head=next(csvreader)
    for row in csvreader:
            dates.append(row[0])
            change = int(row[1])- value
            profits.append(change)
            value = int(row[1])
            total_months += 1
            total_PnL = total_PnL + int(row[1])
            avg_change = sum(profits)/len(profits)
            greatest_increase = max(profits)
            greatest_index = profits.index(greatest_increase)
            greatest_date = dates[greatest_index]
            greatest_decrease = min(profits)
            worst_index = profits.index(greatest_decrease)
            worst_date = dates[worst_index]
            
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_PnL)}")
print(f"Average Change: ${str(round(avg_change))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")