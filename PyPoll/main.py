# # In this challenge, you are tasked with helping a small, rural town modernize 
# # its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying \
# # them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# # You will be give a set of poll data called election_data.csv. 
# # The dataset is composed of three columns: Voter ID, County, and Candidate. 
# # Your task is to create a Python script that analyzes the votes and calculates each of the following:


# # The total number of votes cast
# # A complete list of candidates who received votes
# # The percentage of votes each candidate won
# # The total number of votes each candidate won
# # The winner of the election based on popular vote.


#Pull from CSV 
#For Loop thru file and
    #Add each unique candidate to list - append to list both a name and a vote count for that name
    #Tally the number of votes each got - run a counter 
    #Tally the total number of votes - run a counter 
    #Calculate total candidate votes over total votes - % - calculate on the fly? 

    #Compare final numbers and make candidate with highest votes the Winner 
        #How do I compare values in a list as I go? 
        #Do I build the place winners as I go? 
            #review list work - ??  




print("Election Results")

print("______________________")


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
