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

#build a set of the candidates,
candidates_set = sorted({*voting_data}, key=voting_data.count, reverse=True)

#get candidate data
for candidate in candidates_set: 
    candidate_votes = voting_data.count(candidate)
    candidate_percent = round((candidate_votes/total_votes)*100)
    #put results in the list
    all_results.append(f"{candidate}: {candidate_percent}% ({candidate_votes})")
    #build dictionary for winner 
    most_votes.update({candidate:candidate_votes})

winner = max(most_votes, key=most_votes.get)


    #Compare final numbers and make candidate with highest votes the Winner 
        #How do I compare values in a list as I go? 
        #Do I build the place winners as I go? 
            #review list work - ??  

# if correy_votecount > khan_votecount and correy_votecount > li_votecount and correy_votecount> otooley_votecount:
#     winner = "Correy"

# if li_votecount > khan_votecount and li_votecount > correy_votecount and li_votecount> otooley_votecount:
#     winner = "Li"

# if khan_votecount > otooley_votecount and khan_votecount > li_votecount and khan_votecount> correy_votecount:
#     winner = "Khan"

# if otooley_votecount > khan_votecount and otooley_votecount > li_votecount and otooley_votecount> correy_votecount:
#     winner = "O'TOoley"


# print("Election Results")
# print(candidate_list) 
print(str(total_votes))
print(candidates_set)

print("______________________")

# print(str(total_votecount) +" total votes")

# print("Khan:  " +str(khan_votecount)+" votes. (" +str((khan_votecount/total_votecount)*100)+ "%)")
# print("Li received " +str(li_votecount)+" votes. (" +str((li_votecount/total_votecount)*100)+ "%)")
# print("O'Tooley received " +str(otooley_votecount)+" votes. (" +str((otooley_votecount/total_votecount)*100)+ "%)")
# print("Correy received " +str(correy_votecount)+" votes. (" +str((correy_votecount/total_votecount)*100)+ "%)")

# print("The winner is " + winner)

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------


# khan_votecount = 0
# li_votecount = 0
# otooley_votecount = 0
# correy_votecount = 0
# winner = ""

#function to find the names of the different candidates from column 1 and put in a dictionary? 

#For Loop thru file 
# #Add each unique candidate to list - append to list both a name and a vote count for that name
