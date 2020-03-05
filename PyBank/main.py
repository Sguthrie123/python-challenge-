# import modules 
import os 
import csv

# Get the paths for reading and writing 
dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, '03-Python_homework_assignment_PyBank_Resources_budget_data.csv' )
output_path = os.path.join(dir_path, "output.csv")

# Declare needed variables and create list of unknown amount 
total_months = 0 
total_made = 0
average = 0
profit = []
monthly_profit = []
months = []

# read row by row and add the total amount of months. I know I couldve just taken the count of the list but wanted to use this way.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    row1 = next(csvreader)
    for row in csvreader:
        total_months = total_months + 1 
        total_made = int(row[1]) + total_made
        profit.append(row[1])
        months.append(row[0])

    # Go through list and get the current and next difference 
    for i in range(len(profit)-1):
        monthly_profit.append(int(profit[i+1]) - int(profit[i]))
    # using the postion in the list of the monthly profit use that as a index to find the months. And calculate the average
    minpos = monthly_profit.index(min(monthly_profit))
    maxpos = monthly_profit.index(max(monthly_profit))
    average = sum(monthly_profit) / (total_months - 1)
    average = round(average, 2)
    
    # Print what was needed 
    print("Finacial Analysis")
    print("------------------------")

    print('Total Months: ' + str(total_months))
    print('Total: $' + str(total_made))
    print('Average Change: ' + str(average))
    print('Greatest Increase in Profits: ' + str(months[maxpos + 1]) + "  $" + str(max(monthly_profit)))
    print('Greatest Decrease in Profits: ' + str(months[minpos + 1]) + "  $" + str(min(monthly_profit)))
    
    # I was not sure why when I tried to zip my orginal tuple it would not let me unless they were list. So i made a list that has just the values for this case 
    # But if i wanted could just make it so its a list of unknown size and just append the values. 
    tuple_month = [total_months]
    tuple_total = [total_made]
    tuple_average = [average]
    tuple_max = [max(monthly_profit)]
    tuple_min = [min(monthly_profit)]
    tuple_max_month = [months[maxpos+1]]
    tuple_min_month = [months[minpos+1]]
    mytuple = zip(tuple_month, tuple_total, tuple_average, tuple_max_month, tuple_max, tuple_min_month , tuple_min )
    # Write in the output file our values found 
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits Month/Year', 'Greatest Increase in Profits $', 'Greatest Decrease in Profits Month/Year', 'Greatest Decrease in Profits $' ])
    csvwriter.writerows(mytuple)