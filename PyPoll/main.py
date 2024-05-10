# Data Analytics and Visualizations Bootcamp 
# Student Name: Thet Win
# Module 3 - Python
# Modified Date: May 10, 2024
#
# Part 2 - PyPoll
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: 
# "Voter ID", "County", and "Candidate".
# This Python script analyzes the votes and calculates each of the following values:
# •	The total number of votes cast
# •	A complete list of candidates who received votes
# •	The percentage of votes each candidate won
# •	The total number of votes each candidate won
# •	The winner of the election based on popular vote
# •	Print the analysis to the terminal and export a text file with the results.

import os
import csv

# Set up relative Paths
cwd = os.path.abspath(__file__)
dir_name=os.path.dirname(cwd)
csvpath=os.path.join(dir_name,'Resources','election_data.csv')
outputpath=os.path.join(dir_name,'analysis','election_results.txt')

# Initialize variables
ttlNumofVotes=0
ttlNumOfVotesPerCandidate=0
percentageOfVotesPerCandidate=0
maxVotes=0
candidateList=[]
votesPerCandidateList=[]

# Custom Function
# Retunrs Number of Votes for Each Candidate (Through Argument called 'name')
def GetVotes(name):
    with open(csvpath,encoding='UTF-8') as csvfile:
    #Exclude the column header row in sum
        headerrow = next(csvfile)
        csvreader=csv.reader(csvfile, delimiter=",")
        
        voteCounter=0
        for row in csvreader:
            if row[2] == candidate:
                voteCounter += 1

        return voteCounter

# Sum Profit/Loss Column
with open(csvpath,encoding='UTF-8') as csvfile:
    #Exclude the column header row in sum
    headerrow = next(csvfile)
    csvreader=csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        # Get row count = Total Number of Votes
        ttlNumofVotes += 1

        # Get unique list of Candidate Names
        if row[2] not in candidateList:
            candidateList.append(row[2])

# Print to Terminal
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(ttlNumofVotes))
print("-------------------------------------")

# Write the results to a txt file
outputfile = open(outputpath,'w') 
outputfile.write("Election Results \n")
outputfile.write("--------------------------- \n")
outputfile.write("Total Votes: " + str(ttlNumofVotes) + "\n") 
outputfile.write("--------------------------- \n")

for candidate in candidateList:
    ttlNumofVotesPerCandidate = GetVotes(candidate)
    percentageOfVotesPerCandidate = round((ttlNumofVotesPerCandidate/ttlNumofVotes) * 100,3)
    votesPerCandidateList.append(ttlNumofVotesPerCandidate)

    # Print to terminal
    print(str(candidate) + ": " +  str(percentageOfVotesPerCandidate) + "%" + "  (" + str(ttlNumofVotesPerCandidate)  +  ")")

    # Write to output file
    outputfile.write(str(candidate) + ": " +  str(percentageOfVotesPerCandidate) + "%" + "  (" + str(ttlNumofVotesPerCandidate)  +  ")\n")

# Find the Candidate with Max Number of Votes by searching for index in Votes Per Candidate List
maxVotes=max(votesPerCandidateList)
winner=candidateList[(votesPerCandidateList.index(maxVotes))]

# Print to Terminal
print("-------------------------------------")
print("Winner: " + winner)

# Write to Output File
outputfile.write("-------------------------------------\n")
outputfile.write("Winner: " + winner + "\n")
outputfile.close()