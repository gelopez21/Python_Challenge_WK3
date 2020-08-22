import os
import csv
PyBank = os.path.join('..', 'Resources', 'budget_data.csv')

count = 0
total_profit = 0
profit_1 = 0
average_change_profit = 0

profit =[]
difference_changes =[]
change_sum = []

with open(PyBank, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    #print("CSV Header: {csv_header}")
    #for row in csvreader:
        #print(row)

    for row in csvreader:
        count = count + 1 
        #Append will add a row down the line
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        #total_revenue = total_revenue + int(row["Revenue"]
        #average_change_profit = 1. calculate the difference between row 2 and 1,
        #and then row 3 and 2, and then row 4 and 3 and so on.
        profit_2 = int(row[1]) #row of 1, means that it should look column B the first number
        difference_profit = profit_2 - profit_1
        #2. sum that difference
        difference_changes.append(difference_profit)
        profit_1 = profit_2
        # 1.identify the greatest change in the first step above, #2. take the month and value and display   
        greatest_increase_profits = max(difference_changes)
        #greatest_decrease_losses = same as above, but lowest number
        greatest_decrease_losses = min(difference_changes)
             
print("Financial Analysis: ")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print(f"Average change in Profits $ {(sum(difference_changes)-difference_changes[0])/(len(difference_changes)-1)}")
print("Greatest Increase in Profits " + "$" + str(greatest_increase_profits))
print("Greatest Decrease in Losses" + "$" + str(greatest_decrease_losses))

 # In addition, your final script should both print the analysis to the terminal and export a text file with the results.
 
text_file = open("PyBank_file.txt","w")
text_file.write("Financial Analysis:" + '\n')
text_file.write("----------------------------------------------------------" + '\n') 
text_file.write("Total Months: " + str(count) + '\n')
text_file.write("Total Profits: " + "$" + str(total_profit)+ '\n')
text_file.write(f"Average change in Profits $ {(sum(difference_changes)-difference_changes[0])/(len(difference_changes)-1)}" + '\n')
text_file.write("Greatest Increase in Profits " + "$" + str(greatest_increase_profits) + '\n')
text_file.write("Greatest Decrease in Losses" + "$" + str(greatest_decrease_losses) + '\n')
text_file.close 
