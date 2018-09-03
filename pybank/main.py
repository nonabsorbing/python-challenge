# In this challenge, you are tasked with creating a Python script for 
# analyzing the financial records of your company. You will give a set of 
# financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the 
# records are simple.)

# Your task is to create a Python script that analyzes the records to calculate 
# each of the following:


#import functions

import csv
import os

#define screenprint function 
# def screenprint():
   

    #Copy and paste...will work.

#define textfile output function 


#set counter variables to 0 
month_count = 0

lastmonth = 0
net_amount = 0

monthly_change = 0 
monthly_change_sum = 0

best_month_amt = 0
best_month_date = ""

worst_month_amt = 0
worst_month_date= ""


budgetcsv = os.path.join("budget_data.csv")

with open(budgetcsv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

# #skip header row 

    header = next(csvreader)

#start for loop 

    for row in csvreader:

        net_amount = net_amount + int(row[1])
    
# average change in "Profit/Losses" between months over the entire period
    #output - need to loop and store - (month 2 - month 1)

       #the change is the value in column 2 minus the amount from last month 
        monthly_change = (int(row[1]) - lastmonth)

        #store the value in column 2 for the next loop 

        lastmonth = int(row[1])
        
        #store the month count ever loop 
        month_count = month_count + 1
        
        #running sum of the total change 
        monthly_change_sum = monthly_change_sum + monthly_change

        #the running total is running sum of monthly changes divided by months 
        average_change = monthly_change_sum/month_count

        average_change 

        #compare each row as you go - if it beats the best month, update the best month to that tag and assign the month to a new variable
        #The greatest increase in profits (date and amount) over the entire period

        if int(row[1]) > best_month_amt:
            best_month_amt = int(row[1])
            best_month_date =  row[0]
        # The greatest decrease in losses (date and amount) over the entire period
        #likewise - if it's lower than the worst amount, update the variable 

        if int(row[1]) < worst_month_amt:
            worst_month_amt = int(row[1]) 
            worst_month_date = row[0] 
    

# screenprint

print("Financial Analysis")
print("____________________________")

print("Total Months: " + str(month_count))
print("Net Gain/Loss: $" + str(net_amount))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + best_month_date + "/ $" + str(best_month_amt))
print("Greatest Decrease in Profits: " + worst_month_date + "/ $" + str(worst_month_amt))

#export above to text file





#Aug 31 - successful screen outputs! Need to check my work - on a much smaller sheet? 
#also need to figure out rounding error thing 
#mostly need to figure out text function - for another day! 
