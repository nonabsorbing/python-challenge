import os
import csv

#Create empty dictionary for candidates - build dictionary from dataset


# candidates_dict = {"name" = #something from }

candidate_list = []
votes = []


total_votecount = 0
khan_votecount = 0
li_votecount = 0
otooley_votecount = 0
correy_votecount = 0
winner = ""

#Pull from CSV 

electioncsv = os.path.join("election_data.csv")

with open(electioncsv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

# #skip header row 

    header = next(csvreader)

#function to find the names of the different candidates from column 1 and put in a dictionary? 

#For Loop thru file and

    for row in csvreader:

        candidate_name = row[2]
                
        #count the total votes
        # total_votecount = total_votecount + 1 

        if candidate_name not in candidate_list:
            candidate_list.append(row[2])



        #count khan's votes

        # if row[2] == "Khan":
        #     khan_votecount = khan_votecount + 1

        # if row[2] == "Li":
        #     li_votecount = li_votecount + 1

        # if row[2] == "O'Tooley":
        #     otooley_votecount = otooley_votecount + 1

        # if row[2] == "Correy":
        #     correy_votecount = correy_votecount + 1


    #Add each unique candidate to list - append to list both a name and a vote count for that name
            # if row[0] not in candidate_list:
            #     candidate_list.append(row[0])


    #Tally the number of votes each got - run a counter 
    #Tally the total number of votes - run a counter 
    #Calculate total candidate votes over total votes - % - calculate on the fly? 

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
print(candidate_list) 
print(candidate_list[1])

print("______________________")

# print(str(total_votecount) +" total votes")

# print("Khan received " +str(khan_votecount)+" votes. (" +str((khan_votecount/total_votecount)*100)+ "%)")
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
