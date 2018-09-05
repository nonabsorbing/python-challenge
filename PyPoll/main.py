import os
import csv

csvread= os.path.join("election_data.csv")

#list for candidate names
voting_data = []

#variable for total votes
total_votes = 0

#open/read file 
with open(csvread, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip header
    header = next(csvreader)

    #loop to put voting data in a python list
    for row in csvreader:
        voting_data.append(row[2])

#total votes is the total number of rows in list (len)
total_votes=len(voting_data)

#empty list to populate with final results - candidate name (candidate), % (candidate_percent), and candidiate vots (candidate_votes) 
all_results = []

#empty dict to sort final tallies to determine winner
most_votes = {}

#build a set of the candidates,sorts ascending by number 
candidates_set = sorted({*voting_data}, key=voting_data.count, reverse=True)

#looop through sorted set to get candidate data
for candidate in candidates_set: 
    candidate_votes = voting_data.count(candidate)
    candidate_percent = round((candidate_votes/total_votes)*100)
    #put results in the list
    all_results.append(f"{candidate}: {candidate_percent}% ({candidate_votes})")
    #build dictionary with name and votes for winner 
    most_votes.update({candidate:candidate_votes})

#use max function on dictionary to determine winner 
winner = max(most_votes, key=most_votes.get)

print("Election Results")
print("______________________")
print(str(total_votes) +" total votes")
print(str(all_results)+"\n")
print(winner + " is the winner")



#For Loop thru file 
# #Add each unique candidate to list - append to list both a name and a vote count for that name
