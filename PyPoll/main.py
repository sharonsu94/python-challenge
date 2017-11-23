#import modules
import os
import csv

#file path
election_data = os.path.join("election_data_2.csv")
summary_data = os.path.join("summary_data.txt")

#open file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    #create lists
    votes = []
    candidates = []
    unique_candidates = []

    for row in csvreader:

        #calculate total number of votes
        votes.append(row[0])
        total_votes = len(votes)

        #creating list of candidates
        candidates.append(row[2])

#generating unique list of candidates
unique_candidates = []
for name in candidates:
    if name not in unique_candidates:
        unique_candidates.append(name)

#print results
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(total_votes))
print("---------------------------")

#total number of votes & percentages for each candidate
candidates_votes_list = []
candidate_votes = 0
for x in unique_candidates:
    for i in candidates:
        if i == x:
            candidate_votes = candidate_votes + 1
            candidate_votes_percentage = round((candidate_votes / total_votes) * 100, 1)
    print (x + ": " + str(candidate_votes_percentage) + "% (" + str(candidate_votes) + ")")
    candidates_votes_list.append(candidate_votes)
    candidate_votes = 0

#create dictionary of candidates and number of vote
candidate_dict = {}
for i in range(len(unique_candidates)):
    candidate_dict[unique_candidates[i]] = candidates_votes_list[i]

#get winner
winner = max(candidate_dict, key=candidate_dict.get)

#print splitter line
print("---------------------------")

#Calculating winner
print("Winner: " + winner)
print("---------------------------")

#writes to textfile
summaryfile = open(summary_data, "w")
summaryfile.write("Election Results\n")
summaryfile.write("---------------------------\n")
summaryfile.write("Total Votes: " + str(total_votes) + "\n")
summaryfile.write("---------------------------\n")
candidates_votes_list = []
candidate_votes = 0
for x in unique_candidates:
    for i in candidates:
        if i == x:
            candidate_votes = candidate_votes + 1
            candidates_votes_list.append(candidate_votes)
            candidate_votes_percentage = round((candidate_votes / total_votes) * 100, 1)
    summaryfile.write(x + ": " + str(candidate_votes_percentage) + "% (" + str(candidate_votes) + ")\n")
    candidate_votes = 0
summaryfile.write("---------------------------\n")
summaryfile.write("Winner: " + winner + "\n")
summaryfile.write("---------------------------\n")
