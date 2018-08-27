# In this challenge, you are tasked with creating a Python script for 
# analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:


#import functions

import csv
import os

budgetcsv = os.path.join(".." ".." "budget_data.csv")

#oneclick 

with open(budgetcsv, newline="") as csvfile:

#nextclick

    csvreader = csv.reader(csvfile, delimiter = ",")

#skip header row 
    header = next(csvreader)

    def monthcount()

    


# Convert months from strings to numbers? can i convert? 


# The total number of months included in the dataset
    #output - count total months -
        #count rows  
    
# The total net amount of "Profit/Losses" over the entire period
    #output - net gain/loss 
        #add all rows 
    
# average change in "Profit/Losses" between months over the entire period
    #output - add all profits/losses and divide by total months
        #(all rows) / (total rows)

# The greatest increase in profits (date and amount) over the entire period
       #compare rows - if function - go row by row and if the next is bigger than the last, mark it as BIG ONE? 

# The greatest decrease in losses (date and amount) over the entire period
       #compare rows - if function - go row by row and if the next is smaller than the last, mark it as SMALL ONE? 
    

#print("Financial Analysis")
#print("____________________________")

#print totalrows
#print total change
#print average change
#print biggest increase w/ date
#print biggest decrease w/ date

#export above to text file 




