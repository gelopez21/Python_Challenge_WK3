#import os and csv files
import os
import csv

#initialize variables
candidates_list = []
total_votes = 0
vote_counts = []

#set path
PyPoll = os.path.join('..', 'Resources', 'election_data.csv')

#open the file
with open(PyPoll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    #print("CSV Header: {csv_header}")

 
    for row in csvreader:
        total_votes = total_votes + 1 #count of total votes       
        candidate_name = row[2]
#1. identify the candidate_name. 2 if condition: create index 3. count votes on the index
        if candidate_name in candidates_list:
            candidate_list_index = candidates_list.index(candidate_name)
            vote_counts[candidate_list_index] = vote_counts[candidate_list_index] + 1
        else:
            candidates_list.append(candidate_name)
            vote_counts.append(1)
#calculate percentage
percentages = []
winning_counts = vote_counts[0]
winning_index = 0

for i in range(len(candidates_list)):
    vote_percentage = round(vote_counts[i]/total_votes*100,1)
    percentages.append(vote_percentage)
#define the highest index count to define winner
    if vote_counts[i] > winning_counts:
        winning_counts = vote_counts[i]
        winning_index = i
winner = candidates_list[winning_index]

print("Election Results")
print("----------------------------------------------------------")
print(f"Total Votes: {total_votes}")
for i in range(len(candidates_list)):
    print(f"{candidates_list[i]}: {percentages[i]}% ({vote_counts[i]})")
print("----------------------------------------------------------")
print(f"Winner: {winner}")

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

text_file2 = open("PyPoll_file.txt","w")
text_file2.write("Election Results:" + '\n')
text_file2.write("----------------------------------------------------------"+ '\n')
text_file2.write(f"Total Votes: {total_votes}"+ '\n')
for i in range(len(candidates_list)):
    text_file2.write(f"{candidates_list[i]}: {percentages[i]}% ({vote_counts[i]})"+ '\n')
text_file2.write("----------------------------------------------------------"+ '\n')
text_file2.write(f"Winner: {winner}"+ '\n')
text_file2.close
